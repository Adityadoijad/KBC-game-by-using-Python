#KBC TYPE GAME USING PYTHON
#Aditya Doijad
questions=["1.What is the capital of France?",
           "2.What is the chemical symbol for gold?",
           "3.What is the largest planet in our solar system?",
           '4.Who wrote "Hamlet"?']

option1=["a. Delhi","b. Paris","c. New York"]
option2=["a) Au","b) Ag","c) Fe"]
option3=["a) Earth", "b) Saturn"," c) Jupiter"]
option4=["a) Dickens"," b) Shakespeare"," c) Tolstoy"]


print(questions[0])
print(option1)
answer1=input("Your answer is : ")
if(answer1=="b") or (answer1=="B"):
    print("Correct answer\nAnd you next question is \n")
    print(questions[1])
    print(option2)
    answer2=input("Your answer is : ")
    if(answer2=="a") or (answer2=="A"):
        print("Correct answer\nAnd you next question is \n")
        print(questions[2])
        print(option3)
        answer3=input("Your answer is : ")
        if(answer3=="c") or (answer3=="C"):
            print("Correct answer\nAnd you next question is \n")
            print(questions[3])
            print(option4)
            answer4=input("Your answer is : ")
            if(answer4=="b") or (answer4=="B"):
               print("YOU ANSWERED ALL CORRECT\nYOU WON 1000😎")
            else:
               print("OOPS! wrong answer\nYOU GOT 750")
        else:
            print("OOPS! wrong answer\nYOU GOT 500")
    else:
        print("OOPS! wrong answer\nYOU GOT 250")
else:
    print("OOPS! wrong answer\nYOU GOT ZERO\nBETTER LUCK NEXT TIME👍🏻")



