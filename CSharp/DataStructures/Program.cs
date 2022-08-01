using System;
using System.Collections.Generic;

namespace CSharp
{
    public class Program {
        public static void Main(string[] args) {

            List<int> usersList = new List<int>();

            for (int i=0; i<5; i++) {
                Console.WriteLine("Enter a number: ");
                int userEntry = Int32.Parse(Console.ReadLine());
                usersList.Add(userEntry); 
            }
            PrintUserList(usersList);
            
            Console.WriteLine(ContainsDuplicate(usersList));
        }

        public static void PrintUserList(List<int> list) {
            list.ForEach(number => Console.Write(number));
        }

        public static bool ContainsDuplicate(List<int> nums) {
            HashSet<int> uniqueSet = new HashSet<int>(nums);
            return uniqueSet.Count != nums.Count;
        }
    }

    //TODO: Fix the printing issue
    //TODO: Fix the project to contain Main in program.cs and each challenge should have a separate class
    //TODO: Do the same for cpp
}