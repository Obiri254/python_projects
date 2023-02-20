def add(a, b):
  ans = a + b
  print(str(a) + " + " + str(b) + " = " + str(ans))
  
  
def sub(a, b):
  ans = a - b
  print(str(a) + " - " + str(b) + " = " + str(ans))
  
  
def mul(a, b):
  ans = a * b
  print(str(a) + " * " + str(b) + " = " + str(ans))
  
  
def div(a, b):
  ans = a / b
  print(str(a) + " / " + str(b) + " = " + str(ans))
  
  
while True:
  
  print("A. Addition")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")


  choice = input("Enter your choice: ")


  if choice == "A" or choice == "a":
    print("Addation")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))
    add(a,b)
    
  elif choice == "B" or choice == "b":
    print("Subtraction")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))
    sub(a,b)
    
    
  elif choice == "C" or choice == "c":
    print("Multiplication")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))
    mul(a,b)
    
  elif choice == "D" or choice == "d":
    print("Division")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))
    div(a,b)
    
  elif choice == "E" or choice == "e":
    print("Program ended")
    quit()