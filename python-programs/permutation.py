import math 
def fact(n):  
    if (n <= 1): 
        return 1
          
    return n * fact(n - 1)  
  
def Permutation(n, r):  
      
    return math.floor(fact(n) /
                fact(n - r))  
      

n = 5
r = 2
print("N is", n)
print("R is", r)
print("Permutation is ", Permutation(n, r)) 
