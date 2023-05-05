# python_assignment

git and github:

Git is a distributed version control system that allows users to keep track of changes made to their code over time. It was developed by Linus Torvalds in 2005 to manage the development of the Linux kernel. Git is free and open-source, making it a popular choice for both personal and commercial projects.

Git uses a decentralized approach to version control, which means that each user has a local copy of the entire repository, including its complete history. This allows users to work offline and makes collaboration easier, as each user can make changes to their local copy of the code without affecting the code on the remote repository until they choose to push their changes.

GitHub is a web-based platform that provides a hosting service for Git repositories. It was launched in 2008 and quickly became one of the most popular platforms for open-source projects. GitHub provides a range of features that make it easier for developers to collaborate and manage their code, including pull requests, issue tracking, and code reviews.

Some of the key features of GitHub include:
1.Repository Hosting: GitHub provides hosting for Git repositories, making it easy for developers to store and manage their code online. Users can create public or private repositories, depending on their needs.

2.Pull Requests: GitHub makes it easy for developers to collaborate on code changes by allowing them to create pull requests. Pull requests are a way for developers to propose changes to a repository and get feedback from other users.

3.Issue Tracking: GitHub provides a built-in issue tracking system that allows developers to track bugs, feature requests, and other issues related to their code. Users can create issues, assign them to team members, and track their progress.

4.Code Reviews: GitHub makes it easy for developers to review each other's code before it is merged into the main repository. This helps ensure that code is of high quality and free of bugs.

5.Integrations: GitHub integrates with a range of other tools and services, including continuous integration and deployment tools, chat platforms, and project management tools.

6.Community: GitHub has a large and active community of developers who share code, collaborate on projects, and provide support to each other. This community is one of the key strengths of GitHub, and it has helped make the platform one of the most popular places for open-source development.

In addition to these features, GitHub also provides a range of tools for managing and organizing code, including code search, code hosting, and code sharing. It also offers various pricing plans, including free plans for personal and small team projects, and paid plans for larger teams and enterprises.

Overall, Git and GitHub are powerful tools for managing code and collaborating with other developers. They have become essential for software development and have helped to facilitate the growth of open-source software.


                         **************************************************************************************************************


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

