#1.1 Implement a recursive to calculate the factorial of given number.

def fact_rect(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rect(n-1)

number = int(input("Enter a value:"))
res =fact_rect(number)

print("The factorial of {}". format (number,res))