print('Welcome to the Quiz')
print("Use space in every separation to part your answer")
answer = input('Are you ready to play the Quiz ? (Y/N): ')
score = 0
total_questions = 3

if answer.lower() == 'y':
    answer = input('Question 1: Who is the founder of DC comics?: ')
    if answer.lower() == 'malcolm wheeler nicholson':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 2:  Who is the founder of Python?: ')
    if answer.lower() == 'guido van rossum':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input(
        "Question 3: Who is the founder of Rubki's Cube?: ")
    if answer.lower() == 'erno rubik':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thankyou for Playing this small quiz game, you attempted',
      score, "questions correctly!")
mark = (score/total_questions)*100
print('Marks obtained:', mark)
print('BYE!')
