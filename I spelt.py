#it asks to user his/her name
name = input("What is your name : ")
#our variable > we will know letter number of his/her name with this variable
x=0
#while x is less than letter number of name print the letter and add 1 to x
while x < len(name):
    print(name[x])
    x += 1
#when program spelt the name it will write to screen I spelt
else:
    print("I spelt")
