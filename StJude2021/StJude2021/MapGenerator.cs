using System;
using System.Collections.Generic;
using System.Numerics;
using SoulsFormats;
using StJude2021.Extensions;

namespace StJude2021
{
    class MapGenerator
    {
        string GamePath { get; }
        Dictionary<string, MapPointManager> PointManagers { get; } = new Dictionary<string, MapPointManager>()
        {
            ["m10_00_00_00"] = null,
            ["m10_01_00_00"] = null,
            // ["m10_02_00_00"] = null,  // no points
            ["m11_00_00_00"] = null,
            ["m12_00_00_00"] = null,
            ["m12_01_00_00"] = null,
            ["m13_00_00_00"] = null,
            ["m13_01_00_00"] = null,
            ["m13_02_00_00"] = null,
            ["m14_00_00_00"] = null,
            ["m14_01_00_00"] = null,
            ["m15_00_00_00"] = null,
            ["m15_01_00_00"] = null,
            ["m16_00_00_00"] = null,
            ["m17_00_00_00"] = null,
            ["m18_00_00_00"] = null,
            // ["m18_01_00_00"] = null,  // no points
        };
        Random Rand { get; }
        PARAM NPCParam { get; }
        
        string PackageMSBPath { get; } = @"Package\map\MapStudio";
        double MinPatrolDistanceSq { get; } = 5.0 * 5.0;
        double MaxPatrolDistanceSq { get; } = 15.0 * 15.0;

        // Entity IDs of enemies that should NOT be randomly moved.
        static List<int> DoNotMove { get; } = new List<int>()
        {
            1000800,  // Gaping Dragon
            1010300,  // Hellkite Wyvern
            1010302,  // Hellkite Wyvern
            1010700,  // Taurus Demon
            1010750,  // Capra Demon
            1010800,  // Bell Gargoyle
            1010801,  // Bell Gargoyle
            1010802,  // Bell Gargoyle
            1100160,  // Crossbreed Priscilla
            1100170,  // Undead Dragon
            1100171,  // Undead Dragon butt
            1100172,  // Undead Dragon wing
            1200010,  // Darkroot Basin Hydra
            1200800,  // Sif
            1200801,  // Moonlight Butterfly
            1210400,  // Kalameet
            1210401,  // Kalameet
            1210402,  // Kalameet
            1210800,  // Sanctuary Guardian
            1210820,  // Artorias
            1210840,  // Manus
            1300800,  // Pinwheel
            1310800,  // Nito
            1310810,  // Nito (sleeping)
            1320700,  // Ash Lake Hydra
            1320800,  // Stone Dragon
            1400000,  // Parasitic Wall Hugger
            1400700,  // Fair Lady
            1400800,  // Quelaag
            1410400,  // Demon Firesage
            1410600,  // Ceaseless Discharge
            1410700,  // Centipede Demon
            1410800,  // Bed of Chaos (spirit)
            1410801,  // Bed of Chaos (tree)
            1410802,  // Bed of Chaos (bug)
            1500100,  // Bomb Giant
            1500101,  // Boulder Giant
            1500800,  // Iron Golem
            1510600,  // Gwynevere
            1510650,  // Gwyndolin
            1510800,  // Ornstein
            1510810,  // Smough
            1510801,  // Super Ornstein
            1510811,  // Super Smough
            1600500,  // Undead Dragon (Valley of Drakes)
            1600800,  // Four Kings
            1600801,  // Four Kings
            1600802,  // Four Kings
            1600803,  // Four Kings
            1600804,  // Four Kings
            1700100,  // Sleeping serpent guard
            1700350,  // Moonlight Butterfly (Crystal Cave)
            1700351,  // Moonlight Butterfly (Crystal Cave)
            1700352,  // Moonlight Butterfly (Crystal Cave)
            1700700,  // Seath (tower)
            1700800,  // Seath
            1800800,  // Gwyn
        };

        // Maps Mimic entity IDs to their nest region entity IDs, which need to move along with them.
        static Dictionary<int, int> MimicNests { get; } = new Dictionary<int, int>
        {
            [1210600] = 1212180,
            [1210601] = 1212181,
            [1500010] = 1502010,
            [1510200] = 1512010,
            [1510201] = 1512011,
            [1510202] = 1512012,
            [1510203] = 1512013,
            [1700400] = 1702010,
            [1700401] = 1702011,
        };
        
        public MapGenerator(string gamePath, Random rand, PARAM npcParam)
        {
            // Primes an instance ready to execute a particular modifier, like
            // moving all enemies or replacing all enemy models.
            GamePath = gamePath;
            Rand = rand;
            NPCParam = npcParam;
        }

        void InitializeManager(string msbStem)
        {
            Console.Write($"---> Initializing point manager for {msbStem}... ");
            PointManagers[msbStem] = new MapPointManager(msbStem, Rand);
            Console.WriteLine("Done.");
        }

        static bool SkipEnemy(MSB1.Part.Enemy enemy)
        {
            return DoNotMove.Contains(enemy.EntityID)
                   || enemy.ModelName == "c1000"  // bonfires and other interactions
                   || enemy.EntityID < 10000  // NPCs and special characters
                   || (3900 <= enemy.EntityID % 10000 && enemy.EntityID % 10000 < 4000)  // Vagrants
                   || (900 < enemy.EntityID % 10000 && enemy.EntityID % 10000 < 1000);  // Black Phantoms
        }

        public void WriteMSB(MSB1 msb, string msbStem)
        {
            msb.Write(GamePath + $@"map\MapStudio\{msbStem}.msb");
        }

        public void ReplaceAllEnemies(string msbStem, string modelName, int npcParam, int npcThinkParam, double odds = 1.0)
        {
            // AI is updated (scripts pre-loaded in Common in package), but NPC param is not, so health, soul reward, etc. stay the same.
            MSB1 msb = MSB1.Read($@"{PackageMSBPath}\{msbStem}.msb");
            foreach (MSB1.Part.Enemy enemy in msb.Parts.Enemies)
            {
                if (SkipEnemy(enemy))
                    continue;
                if (odds == 1.0 || Rand.NextDouble() < odds)
                {
                    enemy.ModelName = modelName;
                    int existingNpcParamId = enemy.NPCParamID;
                    PARAM.Row existingNpcParam = NPCParam[existingNpcParamId];
                    int level = Convert.ToInt32(existingNpcParam["spEffectID4"].Value);
                    enemy.NPCParamID = npcParam + 50 + (level - 7000);
                    enemy.ThinkParamID = npcThinkParam;
                }
            }
            WriteMSB(msb, msbStem);
        }

        public void MoveAllEnemies(string msbStem, double maxDistance)
        {
            // Move all enemies to a point within `maxDistance` of their default position.
            // This may screw with certain event triggers (e.g. ambushes), but that's all part of the fun.
            // Also a 20% chance of giving the enemy some patrol points.

            if (!PointManagers.ContainsKey(msbStem))
                return;  // cannot move enemies in this map
            if (PointManagers[msbStem] == null)
                InitializeManager(msbStem);
            
            MapPointManager points = PointManagers[msbStem];
            points.ClearAllPoints();

            MSB1 msb = MSB1.Read($@"{PackageMSBPath}\{msbStem}.msb");

            double maxDistanceSq = maxDistance * maxDistance;
            foreach (MSB1.Part.Enemy enemy in msb.Parts.Enemies)
            {
                if (SkipEnemy(enemy))
                    continue;

                GamePoint point = points.CheckOutRandomPointWithinDistance($"{enemy.Name}", enemy.Position, maxDistanceSq: maxDistanceSq);
                if (point == null)
                {
                    continue;  // no valid nearby points; skip enemy (e.g. enemies in the air)
                }
                enemy.Position = point.Position;
                enemy.CollisionName = point.CollisionName;
                if (MimicNests.ContainsKey(enemy.EntityID))
                {
                    MSB1.Region mimicNest = FindRegionWithEntityID(msb, MimicNests[enemy.EntityID]);
                    if (mimicNest != null)
                    {
                        mimicNest.Position = point.Position;
                        // Don't need to change rotation (enemy rotation doesn't change).
                    }
                }
                else if (Rand.NextDouble() < 0.2)
                {
                    // Create random patrol points.
                    int patrolPointCount = Rand.Next(2, 5);
                    GamePoint lastPoint = point;
                    List<string> patrolPointNames = new List<string>();
                    for (int j = 0; j < patrolPointCount; j++)
                    {
                        string patrolPointName = $"{enemy.Name} Patrol {j}";
                        GamePoint patrolPoint;
                        try
                        {
                            patrolPoint = points.CheckOutRandomPointWithinDistance(
                                patrolPointName, lastPoint, MinPatrolDistanceSq, MaxPatrolDistanceSq
                            );
                        }
                        catch (ArgumentException)
                        {
                            // Can't find next patrol point. No more patrol points.
                            break;
                        }

                        MSB1.Region patrolRegion = new MSB1.Region()
                        {
                            Name = patrolPointName,
                            Shape = new MSB1.Shape.Point(),
                            Position = patrolPoint.Position,
                            EntityID = -1,
                            Rotation = new Vector3(0.0f, Rand.NextAngle(), 0.0f),
                        };
                        msb.Regions.Regions.Add(patrolRegion);
                        patrolPointNames.Add(patrolPointName);
                        lastPoint = patrolPoint;
                    }
                    while (patrolPointNames.Count < 8)
                        patrolPointNames.Add(null);
                    enemy.MovePointNames = patrolPointNames.ToArray();
                }
            }
            WriteMSB(msb, msbStem);
        }

        public void AddTrees(string msbStem, int treeCount = 20)
        {
            if (!PointManagers.ContainsKey(msbStem))
                return;  // cannot move enemies in this map
            if (PointManagers[msbStem] == null)
                InitializeManager(msbStem);

            MapPointManager points = PointManagers[msbStem];
            points.ClearAllPoints();

            MSB1 msb = MSB1.Read($@"{PackageMSBPath}\{msbStem}.msb");

            for (int i = 0; i < treeCount; i++)
            {
                GamePoint treePoint = points.CheckOutRandomPoint($"Tree{i}");
                double treeAngle = Rand.NextDouble() * 360.0 - 180.0;
                MSB1.Part.Enemy tree = new MSB1.Part.Enemy()
                {
                    Name = $"c3350_Tree{i}",
                    ModelName = "c3350",
                    Position = treePoint.Position,
                    Rotation = new Vector3(0.0f, (float)treeAngle, 0.0f),
                    CollisionName = treePoint.CollisionName,
                    NPCParamID = 335000,
                    ThinkParamID = 335000,
                };
                msb.Parts.Enemies.Add(tree);
            }
            WriteMSB(msb, msbStem);
        }

        MSB1.Region FindRegionWithEntityID(MSB1 msb, int entityId)
        {
            foreach (MSB1.Region region in msb.Regions.GetEntries())
            {
                if (region.EntityID == entityId)
                {
                    return region;
                }
            }
            return null;
        }
    }
}
