using System;


namespace working_with_date_and_time
{
    class Program
    {
        static void Main(string[] args)
        {

            string a = "Martin Craiu Muller ";
            string b = a.Trim();

            Console.WriteLine("'{0}'", b);
            Console.WriteLine("'{0}'", b.ToUpper());

            var indices = b.IndexOfAny(new char[]{'M'});
            Console.WriteLine("'{0}'", indices);
            
            var substr = b.Substring(2, 2);
            Console.WriteLine("'{0}'", substr);

            var splitted = a.Split(' ');
            foreach (var s in splitted){
                Console.Write("'{0}'", s);
            }

            a.Replace("Martin", "deeeh");
            Console.WriteLine("'{0}'", a);

            float price = 29.99f;
            var strprice = price.ToString("C");
            Console.WriteLine("'{0}'", strprice);

            var sentence = "This is going to be a really reallly really long text.";


            Console.WriteLine("'{0}'", StringUtility.SummarizeText(sentence));
            
            
        }


    }
}
