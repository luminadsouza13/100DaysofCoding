/*Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"


*/

package com.company;

import java.util.Arrays;
import java.util.Scanner;

public class SpinWords {
  public static void main(String args[])
  {
   System. out. print( "Enter a Sentence with spaces : ");
   Scanner scanner = new Scanner(System.in);

  String Sentence=scanner.nextLine();
  String strArr[]=spinWords(Sentence);

  StringBuilder sb=new StringBuilder();
  
  for(String str : strArr)
      sb.append(str.toString()).append(" ");
  System.out.println(sb);
  }

  public static String[] spinWords(String Sentence)
  {


   String[] stringArray = Sentence.split(" ");
   for (int i=0;i<stringArray.length;i++)
   {
    int length=stringArray[i].length();
    String reverse=new String();
    if(length >= 5)
    {
     for (int j=length-1;j>=0;j--){
         reverse=reverse + stringArray[i].charAt(j);
     }
     stringArray[i]=reverse;
    }
   }

   return stringArray;
   
  }
}

