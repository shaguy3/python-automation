import os
import random

capital_dic = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
    'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
    'Indiana': 'Indianapolis', 'Iowa': 'Des Monies', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
    'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg', 'Rhoda Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

for quiz_num in range(35):
    os.makedirs("Quizes/Quiz no'%s" % (quiz_num + 1))
    quiz_file = open("Quizes/Quiz no'%s/Quiz %s" % (quiz_num + 1, quiz_num + 1), 'w')

    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiz_num + 1))
    quiz_file.write('\n\n')

    for question_num in range(50):
        states = list(capital_dic.keys())
        random.shuffle(states)
        capitals = list(capital_dic.values())
        random.shuffle(capitals)
        quiz_file.write((' ' * 10) + 'Question number %s: ' % (question_num + 1))
        quiz_file.write('What is the capital of ' + states[question_num] + '?\n')
        correct_answer = capital_dic[states[question_num]]
        all_answers = capitals
        del all_answers[all_answers.index(correct_answer)]
        wrong_answers = random.sample(all_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
        for i in range(4):
            quiz_file.write((' ' * 15) + str(i + 1) + ': ' + answer_options.pop() + '\n')
        quiz_file.write('\n')
    quiz_file.close()
