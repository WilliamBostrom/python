print("Welcome to my rollercoaster!")
weight = int(input("how much is your weight bro?"))
if weight >= 120:
    print("Hmm think you can ride bro")
    height = int(input("how tall are you bro?"))
    if height >= 120:
      print("you can ride bro")
    elif height >= 200:
      print("you cant ride bro")
    else:
      print("sorry you cant ride bro")
    wants_photo = input("do you have a ticket? yes or no")
    if wants_photo == "yes":
      print("$10 then bro")
    else:
      print("$5 doller then bro")
else:
    print("you cant ride bro")







# num = int(input("Choose a number"))
# if num % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")