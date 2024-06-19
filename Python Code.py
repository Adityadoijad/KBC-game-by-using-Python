#KBC TYPE GAME USING PYTHON
#Aditya Doijad
questions=[
["1.What is the capital of France?","a. Delhi","b. Paris","c. New York",2],
["2.What is the chemical symbol for gold?","a) Au","b) Ag","c) Fe",1],
["3.What is the largest planet in our solar system?","a) Earth", "b) Saturn"," c) Jupiter",3],
['4.Who wrote "Hamlet"?',"a) Dickens"," b) Shakespeare"," c) Tolstoy",2],
["5. What is the tallest mountain in the world?", "a. K2", "b. Mount Everest", "c. Kangchenjunga", 2],
["6. What is the currency of Japan?", "a. Yen", "b. Dollar", "c. Euro", 1],
["7. Who painted the Mona Lisa?", "a. Vincent van Gogh", "b. Pablo Picasso", "c. Leonardo da Vinci", 3],
["8. Which element has the atomic number 1?", "a. Helium", "b. Hydrogen", "c. Oxygen", 2],
["9. What is the capital of Australia?", "a. Sydney", "b. Canberra", "c. Melbourne", 2],
["10. Who discovered penicillin?", "a. Marie Curie", "b. Alexander Fleming", "c. Louis Pasteur", 2],
]

level=[10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
money=0
for i in range(10):
    question=questions[i]
    print(f"Here is the question:\n{question[0]}\nFor Rs.{level[i]}")
    print(f"{question[1]}                 {question[2]}")
    print(f"{question[3]}")
    a=int(input("Enter the correct option(1-3) or zero to quit: "))
    if(a<=0 or a>=3):
        raise ValueError("Select between 0 to 3")
    if(a==0):
        money=0
        break
    if(a==questions[i][-1]):
        print(f"Correct answer !! You won{level[i]}\n")
        if(i==3):
            money=level[3]
        elif(i==7):
            money=level[7]
        elif(i==-1):
            money=level[-1]
    else:
        print("Wrong answer")
        break

print(f"You have won Rs.{money}")
