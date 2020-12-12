import re
import random

def random_choice(file):
    with open(file, 'r', encoding='utf-8') as story_text:
        text = str(story_text.read())
    #ok = []
        var = text.split('\n')
        choice = random.choice(var)
    return choice

ok = ['Жили-были', random_choice('characters.txt'), random_choice('actions.txt'), random_choice('problems.txt'), random_choice('solution.txt'),random_choice('final.txt')]
ok = str(ok).replace('[', '').replace('\'', '').replace(']', '').replace(',', '')
print (ok)

with open('new_story.txt', 'w', encoding='utf-8') as f:
    f.write(ok)
