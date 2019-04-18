import pprint

s = ['mission statement',
    'mission impossible',
    'a man on a mission',
    'mission fake',
    ]

"""
def bree(s):
    rel = {}

    for i in s:
        wInP = i.split()
        rel[wInP[len(wInP)-1]] = i

    solution = []

    for j in s:
        wInP = j.split()

        first = wInP[0]

        if first in rel:
            string1 = rel[wInP[0]]
            string2 = ' '
"""

def rev(s: 'List')-> 'List':
    temp = []
    for i in s:
        splitted = i.split()
        lastWord = splitted[-1]

        for j in s:
            split = j.split()
            firstWord = split[0]

            if firstWord == lastWord:
                del splitted[-1]
                first_str = ' '.join(splitted)
                second_str = ' '.join(split)
                temp.append(first_str + ' ' + second_str)

    return temp

print(rev(s))
