def enc(a):
    n = len(a)
    if (n<4):
        print(a[::-1])
    # for big letters
    add = a + a[:1]
    sub = add[1:]
    # adding random letters to end and starting
    added = "dft" + sub + "std"
    return added
#decoding of the word with function unenc
def unenc(b):
    sub1 = b[3:]
    sub2 = sub1[:-3]
    add = sub2[-1:]+sub2
    add2 = add[:-1]
    return add2

#main section********************
word = ""
i = 0
while i!=3:
    print("please choose an option \n1. to encrypt \n 2. to decrypt \n 3. to exit")
    i = int(input("\n"))
    match i:
        case 1:
            word = input("enter your word")
            enc1 = enc(word)
            print(" this is the encrypted ", enc1)
        case 2:
            decription = unenc(enc1)
            print("this is decrypted", decription)
        case 3:
            print("ok code exited")

        case _:
            print("sorry wrong option")