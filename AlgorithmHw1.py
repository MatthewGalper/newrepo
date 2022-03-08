#HW1
"1.1 Compute the sum of digits in all numbers from 1 to n"


#n = int (input ("Enter any natural number: "))

#if n < 0:

#              print ("Wrong input. Please enter a positive number.")

#else:

 #             sum = 0

  #            while (n > 0):

   #                          sum +=n

    #                         n -=1

     #         print ("The sum of the natural numbers is: ", sum)

#"1.2 Find max number from 3 values, entered manually from a keyboard"
#def maximum(a, b, c):
 #  list = [a, b, c]
  # return max(list)
# Driven code
#x = int(input("Enter First number"))
#y = int(input("Enter Second number"))
#z = int(input("Enter Third number"))
#print("Maximum Number is ::>",maximum(x, y, z))

"1.3 Count odd and even numbers. Count odd and even digits of the whole number."

#number = int (input ("Enter any natural number: "))

#even = [int(x) for x in str(number) if int(x)%2 == 0]
#odd = [int(x) for x in str(number) if int(x)%2 != 0]
#print(even)
#print(odd)