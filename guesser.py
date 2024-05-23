print("Kon Banega MEME pati")

playing = input("khelna hai(type yes or no)? ")


if playing.lower() != "yes":
    quit()

print("thik hai bhai khelte hai")
score = 0

answer = input("south delhi girls ka evening snack? ")
if answer.lower() == "spermicide": 
    print("Sahi jawab!")
    score += 1 
else: 
    print("aap mumbai nahi aa sakte")

answer = input("Modi ji opponent? ")
if answer.lower() == "dhruv rathee": 
    print("Sahi jawab!")
    score += 1
else: 
    print("aap mumbai nahi aa sakte")


    answer = input("maxtern ko chata kisne mara? ")
if answer.lower() == "elvish yadav": 
    print("Sahi jawab!")
    score += 1
else: 
    print("aap mumbai nahi aa sakte")


    answer = input("takla hu but lambi choti gau mai besura batao kaun? ")
if answer.lower() == "chahat fate ali khan": 
    print("Sahi jawab!")
    score += 1
else: 
    print("aap mumbai nahi aa sakte")


answer = input("tum logo ki? ")
if answer.lower() == "mkc": 
    print("Sahi jawab!")
    score += 1
else: 
    print("aap mumbai nahi aa sakte")



print("you got" + str(score) + "sahi jawabs")
print("you got" + str((score/5) * 100) + "%")




print("you win the meme award")
claim = input("do you want it(yes or no)? ")
if claim.lower() == "yes":
    print("nahi dunga hehe")
else: 
    print("ha ha aap toh bade log hai kyu he lenge award")



                