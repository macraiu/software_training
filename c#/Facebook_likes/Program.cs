/*
When you post a message on Facebook, depending on the number of people who like your post, Facebook displays different information.

    If no one likes your post, it doesn't display anything.
    If only one person likes your post, it displays: [Friend's Name] likes your post.
    If two people like your post, it displays: [Friend 1] and [Friend 2] like your post.
    If more than two people like your post, it displays: [Friend 1], [Friend 2] and [Number of Other People] others like your post.

Write a program and continuously ask the user to enter different names, until the user presses Enter (without supplying a name). Depending on the number of names provided, display a message based on the above pattern.
*/

using System;
using System.Collections.Generic;

namespace Facebook_likes
{
    class Program
    {

        static void Main(string[] args)
        {
            
            List<string> friends = new List<string>();

            while(true){

                Console.WriteLine("Enter name: ");
                string userName = Console.ReadLine();
                if (string.IsNullOrEmpty(userName)){
                    break;
                }
                
                friends.Add(userName);

                switch(friends.Count){
                    
                    case 1:
                        Console.WriteLine(string.Format("{0} likes your post.", friends[0]));
                        break;
                    
                    case 2:
                        Console.WriteLine(string.Format("{0} and {1} like your post.", friends[0], friends[1]));
                        break;
                    
                    default:
                        Console.WriteLine(string.Format("{0}, {1} and {2} others like your post.", friends[0], friends[1], friends.Count - 2));
                        break;

                }

            }


        }

    }
}

