questions = [
    {
        "question": "1. A best friend is someone who:",
        "options": [
            "A. Always agrees with you",
            "B. Stays with you only in happy times",
            "C. Supports you in good and bad times",
            "D. Only talks to you at school"
        ],
        "answer": "C"
    },
    {
        "question": "2. Which quality is most important in a best friend?",
        "options": [
            "A. Honesty",
            "B. Money",
            "C. Popularity",
            "D. Appearance"
        ],
        "answer": "A"
    },
    {
        "question": "3. True friendship is based on:",
        "options": [
            "A. Competition",
            "B. Trust and understanding",
            "C. Jealousy",
            "D. Arguments"
        ],
        "answer": "B"
    },
    {
        "question": "4. When you make a mistake, a best friend should:",
        "options": [
            "A. Make fun of you",
            "B. Leave you",
            "C. Help you learn from it",
            "D. Tell everyone"
        ],
        "answer": "C"
    }
]

score = 0

print("****BEST FRIEND MCQ QUIZ****")

for q in questions:
    print("\n" + q["question"])
    
    for opt in q["options"]:
        print(opt)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == q["answer"]:
        print("Correct ")
        score += 1
    else:
        print("Wrong ")

print("\nQuiz Finished!")
print("Your Score:", score, "/", len(questions))
