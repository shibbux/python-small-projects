def quiz(a, b, c, d):
    i = 0
    j =0
    for k in range(1, 11):
        print("=====================QUIZ NO. ", k, "==============================")
        print(b[i])
        inp = input("enter your answer : ")
        if inp in a[j]:
            print("Hurray ", d, "you won 1000 ₹/-")
            c = c + 1000
            print("your balance is ", c, "₹/- \n Here is another question for you!!")
            print("************************************************************************")
        else:
            print("Wrong answer you lost your money :-(")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break
        k = k + 1
        i = i + 1
        j= j+1

#main portion started here
ans = ["c", "d", "b", "c", "c", "d", "d"]
ques = ["What is the capital of France?\n A) Madrid\n - B) Rome\n- C) Paris\n- D) Berlin\n- E) London",
        "Who wrote the play 'Romeo and Juliet'?   \n - A) Charles Dickens\n- B) J.K. Rowling\n- C) Jane Austen\n- D) William Shakespeare\n- E) Mark Twain",
        "Which planet is known as the Red Planet? \n  - A) Venus\n- B) Mars\n- C) Jupiter\n- D) Saturn\n- E) Mercury",
        "What is the largest mammal in the world?\n - A) Elephant- B) Giraffe\n- C) Blue Whale\n- D) Rhino\n- E) Hippo\n",
        "In which year did India gain independence?\n   - A) 1945- B) 1946\n- C) 1947\n- D) 1948\n- E) 1949",
        "What is the chemical symbol for water?\n   - A) CO2- \nB) NaCl\n- C) H2O2\n- D) H2O\n- E) O2",
        "Who is known as the Father of the Nation in India? \n  - A) Jawaharlal Nehru\n- B) Subhas Chandra Bose\n- C) Bhagat Singh\n- D) Mahatma Gandhi\n- E) Sardar Patel"]


print("welcome to the KBC. \n In this game you have to answer every question\n If you answer wrong \n you will lost all your money ")
print("*******To start the game you have to enter your name first********")
name = input()
rupees = 0
print("Here is the first question for you .", name, " \n GOOD LUCK !!")

quiz(ans, ques, rupees, name)








