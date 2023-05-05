# python_assignment
1.arithmetic operators in python:
    a. The first two lines use the input() function to prompt the user to enter the values of a and b. The int() function is used to          convert the input string to an integer.
    b.The next few lines use the arithmetic operators to perform the following operations on a and b:
             Addition (a + b)
             Subtraction (a - b)
             Multiplication (a * b)
             Division (a / b)
             Modulus (a % b) - returns the remainder of the division operation
             Floor Division (a // b) - returns the quotient of the division operation, rounded down to the nearest integer
             Exponentiation (a ** b) - raises a to the power of b
    c. The results of each operation are printed to the console using the print() function.
    d. Note that the floor division operation a // b returns 0 in this case because 3 / 4 is less than 1, so the quotient is rounded  down to 0.
    
    
 2.fibonacis  series:
 
    This Python code prints the first n numbers of the Fibonacci sequence, where n is entered by the user. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The code initializes the first two numbers of the sequence (a and b) to 0 and 1, respectively, and uses a for loop to print each number of the sequence up to the nth number. The loop calculates the next number of the sequence by adding a and b, assigns b to a, and assigns the sum to b for the next iteration. The code handles cases where n is 0 or 1 as special cases, and prints an error message or the single number, respectively.

   
3. python program to find the given year a leap year or not:

    a.A year is a leap year if it is divisible by 4, except for years that are               divisible by 100 but not by 400.
  
    b.The code prompts the user to enter a year, and checks if it satisfies the above         conditions using modulo operators and if/elif statements.

    c.The code prints a message indicating whether the year is a leap year or not,           based on the result of the checks.


4.matrix script:
    This Python code transposes a matrix of alphanumeric characters and spaces, concatenates each row into a single string, removes any non-alphanumeric characters except spaces, and replaces consecutive non-alphanumeric characters with a single space. The result is a decoded string that represents the original message encoded in the matrix.
 
 
 5.maximize:
     This Python code takes user input for a number of lists (n) to create and a multiplication factor (mul). It reads n lists of integers, with each list having at most 7 elements and each element at most 10^9. It calculates the maximum number from each list and creates a new list m with these maximum numbers. Then, it calculates the sum of the squares of the numbers in m and takes the modulo with mul. The result is the maximized number.
 
 
6.palindrome:
    This Python code checks if the user input string (s) is a palindrome or not. It initializes two variables, i and n, to the length of the string minus one and zero, respectively. It then compares the characters of the string from the start and end using a while loop. If any of the characters don't match, it prints that the string is not a palindrome and exits the loop. Otherwise, it increments a counter variable p. If p equals the length of the string, it means that all characters have matched and the string is a palindrome. In that case, it prints that the string is a palindrome.


7.percentage:
     This code prompts the user to enter two integer values: the numerator (i) and denominator (t) to calculate the percentage. It then calculates the percentage as percentage = (i/t) * 100, where i/t represents the fraction of the total and multiplying it by 100 converts it to a percentage. Finally, it prints the calculated percentage value using the print() function.
     
8.postel code:
    This Python program uses regular expressions to validate a postal code entered by the user. The program defines two regular expressions: one to check if the postal code is a 6-digit integer in the range 100000 to 999999, and the other to check if the postal code does not contain any two alternating repetitive digits. It then prompts the user to enter a postal code, validates it using the regular expressions, and prints whether the postal code is valid or invalid.
  
9.pyramid:
     This is a Python program to print a triangle of asterisks (*) with a given number of rows. It takes user input for the number of rows, and then uses nested loops to print the asterisks in the shape of a triangle. The outer loop is used to iterate through the rows, while the inner loops are used to print spaces and asterisks in each row. The program uses a variable k to keep track of the number of asterisks printed in each row.
 
 
10.swap with function:
    This program defines a function called swap that takes in two arguments a and b. It then swaps the values of a and b using a temporary variable c. The function returns a and b with their values swapped.

The program then prompts the user to enter two values a and b, and prints them out before swapping. It calls the swap function to swap the values of a and b, and then prints out the swapped values.



what is git and github:

Git is a version control system that allows developers to track changes in their code and collaborate with others. It was created by Linus Torvalds in 2005 and is widely used in the software development industry.

GitHub is a web-based platform that provides hosting for Git repositories. It allows developers to store, manage, and share their code with others. It also provides tools for issue tracking, code review, and project management. GitHub has become a popular platform for open source projects and is used by millions of developers around the world.




   
    

     










   


