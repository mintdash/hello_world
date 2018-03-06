num = input("Please type an integer: ")
num = int(num)
if num%4 == 0:
    print ("Your number is multiple of four.")
elif num%2 ==0:
    print("Your number is an even number.")
elif num%2 == 1:
    print("Your chose an odd number.")
else:
    print("What were you thinking?")
