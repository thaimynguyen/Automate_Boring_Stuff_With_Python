"""
Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. 
You’d like to randomize the order of questions so that each quiz is unique.

Here is what the program does:
- Creates 35 different quizzes on US state capitals
- Creates 50 multiple-choice questions for each quiz, in random order
- Provides the correct answer and three random wrong answers for each question, in random order
- Writes the quizzes to 35 text files
- Writes the answer keys to 35 text files

"""

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files:
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open(f'CapitalQuiz/capitalsquiz{quizNum + 1}.txt', 'w')
    answerFile = open(f'CapitalQuiz/capitalsquiz_answers{quizNum + 1}.txt', 'w')
    # Write out the header for the quiz.
    quizFile.write('Name:')
    quizFile.write('\n\n')
    quizFile.write('Date:')
    quizFile.write('\n\n')
    quizFile.write('Period:')
    quizFile.write('\n\n')
    quizFile.write(f'            State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through all 50 states, making a question for each.
    for question_num in range(50):
        
        # Assign right and wrong answers
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        options = random.sample(wrong_answers, k=3) + [correct_answer]
        random.shuffle(options)
        
        # Write question and answer options to the quiz file
        quizFile.write(f'{question_num + 1}. What is the capital of {states[question_num]}? \n')
        for i in range(4):
            quizFile.write(f'    {"ABCD"[i]}. {options[i]}\n')
        quizFile.write('\n')
        
        # Write the answer key to the answer key file.
        answerFile.write(f'{question_num + 1}. {"ABCD"[options.index(correct_answer)]}\n')

answerFile.close()
quizFile.close()
