#Where I stole this from - https://www.geeksforgeeks.org/recursion-in-python/
# Program to print the fibonacci series up to n_terms and factoral up to n terms
 
def factorial(n): 
     
    # Checking the number
    # is 1 or 0 then
    # return 1
    # other wise return
    # factorial
    if (n==1 or n==0):
         
        return 1
     
    else:
         
        return (n * factorial(n - 1)) 
 

# Recursive function
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
 
n_terms = 10
 
# Driver Code for factoral

print("number : ",n_terms)
print("Factorial : ",factorial(n_terms))

#Code for fibonacci 
# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))