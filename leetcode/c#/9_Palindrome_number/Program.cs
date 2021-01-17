/*

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

*/

using System;
using System.Collections.Generic;

namespace _9_Palindrome_number
{
    class Program
    {
        public static bool IsPalindrome(int x) {
            
            var original_x = x;
            var reverse = 0;
            
            while (x > 0){
                reverse = 10 * reverse + (x % 10);
                x = (int) x / 10;
            }

            return (reverse == original_x);
            
        }

        static void Main(string[] args)
        {
            Console.WriteLine(IsPalindrome(-1));
            Console.WriteLine(IsPalindrome(0));
            Console.WriteLine(IsPalindrome(9));
            Console.WriteLine(IsPalindrome(10));
            Console.WriteLine(IsPalindrome(100));
            Console.WriteLine(IsPalindrome(1001));
        }
    }
}
