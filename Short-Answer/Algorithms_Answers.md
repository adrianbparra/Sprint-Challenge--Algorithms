#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The runtime is O(n) since n * n * n will just give one int back and depending on that int the while loop will repeat as long as it is greater than a

b)
The runtime is O(n^2) since the nested while loop has to run until it j is greater than n. Then the while loop exist and the for loop goes to the next value. Then the process repeats and gets longer and longer.

c)
The runtime is O(n) since each call is repeater based on the value of n. The n value is then subtracted by one and a new recursion is called until n goes to 0.

## Exercise II


We would create a loop starting at the first floor since the lower the less chance of breaking an egg. We will the check on each floor if a dropped egg is broken. 
    If a dropped egg breaks on the f floor. We will have the f floor the egg is broken.
    Else if the egg does not break we will continue to the next f floor. 

This is a O(n) since it depends on the size of n-story buildings as it escalates up higher.