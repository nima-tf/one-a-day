using System;
using System.Collections.Generic;

namespace CsharpTest
{
    public class DuplicateTest {
        
        public static void main(string[] args) {
        for (int i=0; i<5; i++) {
            Console.Writeline("hello!");
        }
        }
        private bool ContainsDuplicate(int[] nums) {
            HashSet<int> uniqueSet = new HashSet<int>(nums);
            return uniqueSet.Count != nums.Length;
        }
    }
}