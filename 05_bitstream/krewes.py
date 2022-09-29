import random
def choose():
    d = {}
    krewes = open("krewes.txt","r")
    krewes = krewes.read()
    krewes = krewes.strip()
    krewes = krewes.split("@@@")
    """
    for i in krewes:
        i = i.split("$$$")
        d.update({int(i[0]):d[int(i[0])].append(i[1:3])})
        print(d)
    """
    for i in krewes:
        i = i.split("$$$")
        period = i[0]
        name = i[1]
        ducky = i[2]
        if period not in d.keys():
            d.update({period: [[name, ducky]]})
    print(d)
    """
    rand_key = random.choice(list(d.keys()))
    rand_val = random.choice(d[rand_key])
    return rand_val
"""
choose()