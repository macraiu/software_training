using System;

namespace working_with_date_and_time
{
    public class StringUtility
    {
        public static string SummarizeText(string Text, int maxLen = 20){
            
            var words = Text.Split(' ');
            var total_letters = 0;

            if (Text.Length < maxLen)
                return Text;

            foreach(var i in words){

                var len = i.Length + 1;
                if (total_letters + len > maxLen){
                    break;
                }
                else{
                    total_letters += len;
                }
            }

            return Text.Substring(0, total_letters) + "...";

        }
    }
}
