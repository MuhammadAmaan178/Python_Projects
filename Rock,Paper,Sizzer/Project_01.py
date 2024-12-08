"""
ROCK , PAPER AND SIZZER GAME USING PYTHON
"""


import random
options = ["rock","paper", "sizzer"]
comp_c = random.choice(options)
user_c_short = input("Choose your choise...(using rock(r) , paper(p) , sizzer(s) ) :- ")
dict = {"r":"rock" , "p":"paper" , "s":"sizzer"}
user_c = dict[user_c_short]


if (comp_c == user_c):
    print(f"You and Comp Both Choose {comp_c}...Its a tie")

elif(user_c == "rock"):
    if (comp_c == "paper"):
        print(f"You Choose rock & comp choose {comp_c}....You Lose!!!")
    if (comp_c == "sizzer"):
        print(f"You Choose rock & comp choose {comp_c}....You Win!!!")


elif(user_c == "paper"):
    if (comp_c == "rock"):
        print(f"You Choose paper & comp choose {comp_c}....You Win!!!")
    if (comp_c == "sizzer"):
        print(f"You Choose paper & comp choose {comp_c}....You Lose!!!")

elif(user_c == "sizzer"):
    if (comp_c == "paper"):
        print(f"You Choose sizzer & comp choose {comp_c}....You Win!!!")
    if (comp_c == "rock"):
        print(f"You Choose sizzer & comp choose {comp_c}....You Lose!!!")

else:
    print("An Error Occurred")