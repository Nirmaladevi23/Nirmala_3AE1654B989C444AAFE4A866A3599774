#Program to find factorial of a given number
def factoiral (n):
  if n==0 or n==1:
    return 1
  else:
    return n*factoiral(n-1)
num=6
result=factoiral(num)
print("Factorial of",num,"is",factoiral(num))