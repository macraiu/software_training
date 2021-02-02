using System;
using System.Collections.Generic;
    
namespace classes
{
    public class Customer
    {
        // you don't need all the constructors
        public string Name = "Mark";
        public int Id;
        // fields
        // data about the class

        // use readonly keyword when you want to improve a field to be initialised either in constructor or 
        // field initialiser and not anywhere else. 

        // access modifiers
        // public, private, protected, internal, protected interanal.
        // control access to a class or members.

        // OOP programming:
        // encapsulation, inheritance, polymorphism

        // Encapsulation:
        // information hiding
        // why using the encapsulation? because obejcts should hide their implementation
        // whoudl reveal what they can do ratehr then how they are doing it.
        // Define fields as private, and use getter/setter methods as public

        // private field should start with underscore _name for example
        // setting them by this._name = name; and return _name
        // actually without accessing the field you make mathods for retriving the fields.
        // it defines a method which you can also modify or check validity of the field. 

        // write property: less code.
        // if you have 10 fields for each are you writing getter and setter? time consuming
        // method parameters or private fields shoudl be camel case birthDate
        // all the rest: class names and method name should be pascal case Person, BirthDate

        // private DateTime _birthdate;
        // public DateTime BirthDate{get{return _birthdate;} set{_birthdate = value;}}
        // no logic in the get and set so you can use an AUTOIMPLEMENTED PROPERTY
        // for using even less code
        public DateTime BirthDate {get; set;}
        
        public List<Order> Orders = new List<Order>();
        // some developers find the use of a constructor only when you pass arguments from the outside

        public Customer(int id)
        {
            this.Id = id;
        }

        public Customer(int id, string name)
            :this(id)
        {
            this.Name = name;
        }


    }

    public class Order
    {

    }


    class Program
    {
        static void Main(string[] args)
        {


            // object initializer in action
            // for not having 
            Customer c = new Customer(100, "Martin");
            // default constructor will be called with the fields passed
            c.BirthDate = new DateTime(1998, 1, 1);
            System.Console.WriteLine(c.BirthDate);
            
            System.Console.WriteLine("{0}", c.Name);
            
        }
    }

}
