using System;
using System.IO;
using System.Linq;
using System.Threading;
using System.Windows.Forms;
using GameHook;

namespace StJude2021
{
    class Program
    {
        static string GAME_PATH = null;
        static string MOD_FILE_PATH = null;
        static Random Rand;

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            if (ModifierInfo.ModifierIndices.Count != 100)
            {
                Console.WriteLine($"ERROR: Length of `ModifierIndices` list is {ModifierInfo.ModifierIndices.Count}, not 100!");
                Console.WriteLine("Press any key to quit.");
                Console.ReadLine();
                return;
            }

            PrintModifierInfo();

            if (File.Exists("STJUDE2021.cfg"))
            {
                GAME_PATH = File.ReadAllText("STJUDE2021.cfg");
            }

            if (File.Exists("STJUDE2021_MODFILEPATH.cfg"))
            {
                MOD_FILE_PATH = File.ReadAllText("STJUDE2021_MODFILEPATH.cfg");
            }

            Console.WriteLine(@"

                              ~~~ ST JUDE ~~~

                                EPISODE III

                          REVENGE OF THE WOLFPACK
                                   
                                by Grimrukh
");
            Thread.Sleep(1000);
            Console.WriteLine(@"  
  WELCOME!

     Please install the base files of this mod MANUALLY by COPYING (not cutting)
     the contents of 'Package' into your DS1R game installation. Make a backup
     of existing game files before doing so if you'd like. Please do not remove
     the 'Package' folder and make sure it is always next to this executable.

     You will be prompted once to specify your Dark Souls Remastered installation
     directory, which will then be stored in 'STJUDE2021.cfg' next to this
     executable for automatic future use. Delete that file and restart this mod
     program to be prompted again (or you can edit the file manually).

     A separate config file, 'STJUDE2021_MODFILEPATH.cfg', will contain the path
     to the directory where 'mod{n}.txt' files will be detected for triggering
     modifier `n`. These files will be deleted once detected. Their contents are
     not read. `n` should be between 1 and 100, inclusive. (This is only needed for
     'file' mode.)
");

            GAME_PATH = GetGameDir();
            if (GAME_PATH == null)
            {
                Console.WriteLine("No EXE selected. Ending program.");
                return;
            }
            if (!Directory.Exists(GAME_PATH))
            {
                Console.WriteLine($"Executable path does not exist: {GAME_PATH}");
                Console.WriteLine($"Please correct (or delete) the 'STJUDE2021.cfg' file next to this executable and try again.");
                Console.WriteLine($"Press ENTER to quit.");
                Console.ReadLine();
                return;
            }
            Rand = new Random();

            string mode;
            while (true)
            {
                Console.Write($"Choose mode from 'file', 'input', or 'auto': ");
                mode = Console.ReadLine();
                if (mode != "file" && mode != "input" && mode != "auto")
                    Console.WriteLine("Invalid mode.");
                else
                    break;
            }

            if (mode == "file")
            {
                MOD_FILE_PATH = GetModFileDir();
                if (MOD_FILE_PATH == null)
                {
                    Console.WriteLine("No mod file path selected. Ending program.");
                    return;
                }
                if (!Directory.Exists(MOD_FILE_PATH))
                {
                    Console.WriteLine($"Mod file path does not exist: {MOD_FILE_PATH}");
                    Console.WriteLine($"Please correct (or delete) the 'STJUDE2021_MODFILEPATH.cfg' file next to this executable and try again.");
                    Console.WriteLine($"Press ENTER to quit.");
                    Console.ReadLine();
                    return;
                }
                Console.WriteLine($"Using modifier file path: {MOD_FILE_PATH}");
            }

            DSRHook hook = new DSRHook(5000, 5000);
            hook.Start();

            Console.WriteLine("Waiting for game application to open...");
            while (!hook.Hooked)
                Thread.Sleep(100);
            Console.WriteLine("Waiting for game to be loaded...");
            while (!hook.Loaded)
                Thread.Sleep(100);
            Console.WriteLine("Hooked.");

            Console.WriteLine("Game manager starting...");
            GameManager gameManager = new GameManager(GAME_PATH, hook, Rand);
            gameManager.Run(mode, MOD_FILE_PATH);
        }

        public static void PrintModifierInfo()
        {
            foreach (var it in ModifierInfo.ModifierIndices.Select((Value, Index) => new { Value, Index }))
            {
                string modifierName = ModifierInfo.ModifierNames[it.Value];
                Console.WriteLine($"{it.Index + 1} = {modifierName}");
            }
        }

        static string GetGameDir()
        {
            if (GAME_PATH != null)
            {
                return GAME_PATH;
            }

            Console.WriteLine("\nPress ENTER to select your Dark Souls Remastered executable.");
            Console.ReadLine();
            OpenFileDialog ofd = new OpenFileDialog { Filter = "EXE Files|*.exe" };

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                GAME_PATH = Path.GetDirectoryName(ofd.FileName) + "\\";
                File.WriteAllText("STJUDE2021.cfg", GAME_PATH);
                return GAME_PATH;
            }
            else
            {
                return null;
            }
        }

        static string GetModFileDir()
        {
            if (MOD_FILE_PATH != null)
            {
                return MOD_FILE_PATH;
            }

            Console.WriteLine("\nPress ENTER to select your mod file path directory.");
            Console.ReadLine();
            FolderBrowserDialog fbd = new FolderBrowserDialog { };
            
            if (fbd.ShowDialog() == DialogResult.OK)
            {
                MOD_FILE_PATH = fbd.SelectedPath;
                File.WriteAllText("STJUDE2021_MODFILEPATH.cfg", MOD_FILE_PATH);
                return MOD_FILE_PATH;
            }
            else
            {
                return null;
            }
        }
    }
}
