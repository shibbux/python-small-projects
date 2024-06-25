import random

def compu():
    #    w  g  s
    i = [1, 2, 3]
    j = random.choice(i)
    return j

def comp(a,b):
    #  coputer value a user val b
    if (a==b):
        print("it's a draw")
    elif (a == 1 and  b == 2):
        print("computer choose water", "lose")
    elif (a == 1 and b == 3):
        print("computer choose water", "win")
    elif (a == 2 and b == 1):
        print("computer choose gun", "win")
    elif (a == 2 and b == 3):
        print("computer choose gun", "lose")
    elif (a == 3 and b == 1):
        print("computer choose snake", "lose")
    elif (a == 3 and b == 2):
        print("computer choose snake", "win")
    else:
        print("wrong input")

# @@@@@@@@@@@@@@@@@@@@  main section start @@@@@@@@@@@@@

f = int(input("press 5 to start:\t"))
print("Welcome to the Snake, water and gun game\n")
while f != 0:
    print("================================================================================")
    print(
          "please press 1 if you want to choose water\n",
          "please press 2 if you want to choose gun\n",
          "please press 1 if you want to choose water\n")
    d = int(input("enter  "))
    v = d
    c = compu()
    comp(c, v)
    f = int(input("Press '0' if you want to exit press any no to replay the game\n"))
else:
    print("wrong key")
