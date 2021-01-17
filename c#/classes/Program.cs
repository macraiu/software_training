using System;

namespace classes
{

    public class Person{
        
        public string Name;
        public int Age;

        public Person(string name){
            this.Name = name;
        }

        public Person(string name, int age){
            this.Name = name;
            this.Age = age;
        }


    }

    public class 


    class Program
    {
        static void Main(string[] args)
        {

            var person =  new Person("John Smith", 23);
            Console.WriteLine("Name: {0} Age: {1}", person.Name, person.Age);

        }
    }
}
