import random
krewes = {2:["Kevin", "Joe", "Mama"] , 7:["Marc", "Ian", "Samantha"], 8:["Jason", "Emilia", "Bobby"]}

keys = list(krewes.keys())
def choose(d):
    l = list(d.keys())
    key = random.randint(0,len(d)-1)
    value = random.randint(0,len(d[l[key]])-1)
    return d[l[key]][value]
print(choose(krewes))
    