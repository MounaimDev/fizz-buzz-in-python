print("Welcome to Fizz Buzz")
for number in range(1,101):
  if(number % 3 == 0 and number % 5 == 0):
    print("FizzBuzz")
  elif(number % 3 == 0):
    print("Fizz")
  elif(number % 5 == 0):
    print("Buzz")
  else:
    print(number)



#For Loop with Lists
#print("loop throught all existing pies")
#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
  #print(fruit)
#  print(fruit + " Pie")

#For Loop with Range
#print("For Loop with Range")
#for number in range(1, 100):
#  print(number)

#for number in range(1, 101):
#  print(number)

#for number in range(1, 11, 3):
#  print(number)

#Calculating the sum of all the numbers from 1 to 100
#print("Calculating the sum of all the numbers from 1 to 100.")
#total = 0
#for number in range(1, 101):
 # total += number
#print(total)