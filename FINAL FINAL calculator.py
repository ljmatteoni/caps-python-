#printing name
n = input('type name here .')

print ("hello your name is"" "+ n)

#password
password = 1
p = int(input("Type Password now..." " "))
while password == 1:
    if p == 1234:
        print("correct!")
        break

    if p > 1234:
        print("INCORRECT")

    if p < 1234:
        print ("INCORRECT")
    p = int(input("Type Password now..." " "))

# code disclamer
print("I got this code: https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3")

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
^2 to squere first number 
^2^ to squere secound number 
''')

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(a,b))
    print(a + b)

elif operation == '-':
    print('{} - {} = '.format(a,b))
    print(a - b)

elif operation == '*':
    print('{} * {} = '.format(a,b))
    print(a * b)

elif operation == '/':
    print('{} / {} = '.format(a,b))
    print(a / b)
elif operation =="^2":
    print('{} *a {} = ' .format(a,b))
    print(a * a)
elif operation == "^2^":
    print ('{} *b {} =' .format(a,b))
    print (b * b)
else:
    print('please run the program again.')

print ("if you want to move on to the stats print password now!")

#password
password = 1
p = int(input("Type Password now..." " "))
while password == 1:
    if p == 1234:
        print("correct!")
        break

    if p > 1234:
        print("INCORRECT")

    if p < 1234:
        print ("INCORRECT")
    p = int(input("Type Password now..." " "))

# greater then or equal to b

if a > b:
    print("a is greater then b ")

if a < b:
    print ("a is less then b ")
if a == b:
    print ("a is equal to b")


#a as a positive negative or zero

if a > 0:
    print("Number 1  is positive number")

if a == 0:
    print("Number 1  is Zero")

if a < 0:
    print("Number 1  is a negative number")



# b as a positive negitive or zero

if b > 0:
  print("Number 2 is positive number")

if b == 0:
  print("Number 2  is Zero")

if b < 0:
  print("Number 2 is a negative number")

