/*
""" 
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 """
*/


using System;

namespace _33_Search_in_Rotated_Sorted_Array
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Search(new int[]{10,15,20,25,-5,0,5}, 25));
        }
    
        public static int Search(int[] nums, int target) {
            
            var l = 0;
            var r = nums.Length - 1;

            while (r - l > 1){

                var m = (int)(r + l)/ 2;

                if (nums[m] < nums[r]){
                    if (nums[m] < target & target <= nums[r])
                        l = m;
                    else
                        r = m;
                }
                else{
                    if (nums[l] <= target & target < nums[m])
                        r = m;
                    else
                        l = m;
                }
            }
            if (nums[l] == target) 
                return l;
            else if (nums[r] == target)
                return r;
            else 
                return -1;        
        }
    }
}
