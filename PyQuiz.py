## James Cullen - @CullenIO
## Written in Python 3.4.3
## See LICENSE for usage

def main():
    print("PyQuiz V1\n-------------------------------")
    print("To answer a question, simply type the corresponding letter (E.g. A, B, C, etc.)")
    points = 0;

    questions = [
        ["What is the capital of England?", ["London","Birmingham","Manchester", "Leeds"], 0],
        ["Which country is Berlin the capital of?", ["France", "Spain", "Germany", "Norway"], 2],
        ["Which year did the Second World War start?", ["1987", "1928", "1945", "1939"], 3],
        ["Sharks are mammals.", ["True", "False"], 1]
    ]

    
    NumberOfQuestions = int(input("How many questions would you like(1-%s)? " % (len(questions)) ))
    
    if (NumberOfQuestions < 1):
        print("You need aleast one question to play!")
        main()
    elif (NumberOfQuestions > len(questions)):
        print("There arn't that many questions! Please choose between 1 and %s!" % (len(questions)))
        main()
    else:
        for x in range(NumberOfQuestions):
            question = questions[x][0]
            answers = questions[x][1]
            correct = questions[x][2]
            
            answer = RunQuestion(question, answers, correct)
            if (answer == True):
                points = points + 1;

        print("----------------------------------------------")
        print("Quiz Over! You scored %s out of %s points!" % (points, NumberOfQuestions))
    
def RunQuestion(question, answers, correct):
    print(question + "\n")
    FormatAnswers(answers)
    
    user_answer = input().lower();

    user_answer = ConvertAnswer(user_answer)

    if (user_answer <= -1):
        print("Please pick an answer: A, B, C or D")
    elif (user_answer == correct):
        print("Correct")
        return True
    else:
        return False


def ConvertAnswer(answer):
    answer = ord(answer)
    return answer - 97;
    

def FormatAnswers(answers):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(len(answers)):
        print(letters[x] + ". " + answers[x])

main()
