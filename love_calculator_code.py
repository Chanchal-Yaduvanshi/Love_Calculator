print("Welcome to the Love Calculator")
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

com_name = name1 + name2
l_com_name = com_name.lower()

t = l_com_name.count("t")
r = l_com_name.count("r")
u = l_com_name.count("u")
e = l_com_name.count("e")
true = t+r+u+e

l = l_com_name.count("l")
o = l_com_name.count("o")
v = l_com_name.count("v")
e = l_com_name.count("e")
love = l+o+v+e

love_score = int(str(true) + str(love))


if love_score<10 and love_score>90 :
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score<40 and love_score>50 :
  print(f"Your score is {love_score}, you are alright together.")
else :
  print(f"Your score is {love_score}")