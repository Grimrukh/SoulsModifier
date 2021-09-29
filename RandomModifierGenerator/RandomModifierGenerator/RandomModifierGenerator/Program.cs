using System;
using System.IO;

namespace RandomModifierGenerator
{
    class Program
    {
        static void Main()
        {
            Random rand = new Random();
            string index = rand.Next(1, 101).ToString();
            File.WriteAllText("StJude2021.txt", index + "\n");
        }
    }
}
