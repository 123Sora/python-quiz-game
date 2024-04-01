# Python Quiz Game 

questions =("Who was the first king of Israel?: ",
           "Who was Jesus's apostles once a tax collector?: ",
           "What does Jesus's name, Immanuel, mean?: ",
           "How many people did Jesus feed with 5 loaves of bread and 2 fish ?: "
           )
options = (("A. Solomon ","B. Jesus","C. David","D. Saul"),
           ("A. James","B. Andrew","C. Matthew","D. Phillip"),
           ("A. Carpenter","B. God is gracious","C. God with us","D. Strong man"),
           ("A. 2000","B. About 5000","C. 500","D. 70000")
           )
answers = ("D","C","C","B")

guesses = []
score = 0 
question_num = 0 

for question in questions : 
    print("-------------------------------------------------------------")
    print(question)
    for option in options[question_num] : 
        print(option)

    guess = input("Enter (A, B, C, D, ): ").upper()
    guesses.append(guess)
    if guess == answers[question_num] : 
        score += 1 
        print("CORRECT!")
    else : 
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer ")
    question_num += 1
    
print("-------------------------------------------------------------")    
print("                      RESULT                                 ")    
print("-------------------------------------------------------------")

print("answer   : ", end="")
for answer in answers : 
    print(answer, end=" ")
print()

print("guesses : ",end="")
for guess in guesses : 
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is {score}%")    