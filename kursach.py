import re
import random

def random_choice (nameoffile):
    with open(nameoffile, 'r', encoding='utf-8') as story_text:
        text = str(story_text.read())
        var = text.split('\n')
        choice = random.choice(var)
        number = var.index(choice)

    return choice, number

P1 = input("грустная или веселая: ")

def make_a_story(file1, file2, file3, file4, file5):
    char = random_choice (file1)
    act = random_choice (file2)
    pro = random_choice(file3)
    sol = random_choice(file4)
    fin = random_choice(file5)
    if P1 == 'в':
        if pro[1] <=1:
            while sol[1] !=0:
                sol = random_choice(file4)
        else:
            while (sol[1] == 0 or sol[1] == 1):
                sol = random_choice(file4)
    elif P1 == 'г':
        while sol[1] != 1:
            sol = random_choice(file4)
    else: print ("Некорректные данные")

    massive = ['Жили были',char[0],act[0],pro[0],sol[0],fin[0]]
    return massive

files = ('characters.txt','actions.txt', 'problems.txt','solution.txt','final.txt')
massive = make_a_story(*files)
massive = str(massive).replace('(', '').replace('\'', '').replace(')', '').replace(',', '').replace('[', '').replace(']', '')
print (massive)

with open('new_story.txt', 'w', encoding='utf-8') as f:
    f.write(massive)
