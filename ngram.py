import re
import random

words = {}

with open('sentences.txt', 'r') as file:
    text = file.read()
    text_token = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", text.lower())

with open('sentences.txt', 'r') as files:
    spec = files.readlines()

def count_sublist(lst, sublst):
    n = len(lst)
    m = len(sublst)
    r = []
    i = 0
    while i <= n - m:
        if lst[i:i + m] == sublst:
            r.append(tuple(lst[i:i + m + 1]))
        i += 1
    return r

def predict(lst, sub):
    specialcase = False
    edtlst = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", sub.lower())
    while True:
        t = len(count_sublist(lst, edtlst))
        if t == 0: #Just like how ~~~the_meaning_of_my_existence == 0~~~ ;(
            edtlst = edtlst[1:]
        else:
            break
    
    prob_dict = {}
    advd_token = []
    
    if edtlst == ["<ans>"]:
        edtlst = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", sub.lower())
        for b in spec:
            c = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", b.lower())
            for y in edtlst:
                x = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", re.search(r'(.*?)<ans>', b).group(1).lower())
                t = len(count_sublist(x, [y]))
                if t == 1:
                    specialcase = True
                    advd_token.extend(c)

    if specialcase == True:
        edtlst[:] = advd_token[:advd_token.index("<ans>") + 1]

    for item in count_sublist(lst, edtlst):
        if item == tuple():
            lst = text_token
            specialcase = False
            edtlst = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", sub.lower())
            while True:
                t = len(count_sublist(lst, edtlst))
                if t == 0: #Just like how ~~~the_meaning_of_my_existence == 0~~~ ;(
                    edtlst = edtlst[1:]
                else:
                    break
            
            prob_dict = {}
            advd_token = []
            
            if edtlst == ["<ans>"]:
                edtlst = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", sub.lower())
                for b in spec:
                    c = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", b.lower())
                    for y in edtlst:
                        x = re.findall(r"<[^>]*>|['a-z]+|[^\w\s]", re.search(r'(.*?)<ans>', b).group(1).lower())
                        t = len(count_sublist(x, [y]))
                        if t == 1:
                            specialcase = True
                            advd_token.extend(c)

            if specialcase == True:
                edtlst[:] = advd_token[:advd_token.index("<ans>") + 1]

    for item in count_sublist(lst, edtlst):
        if item[-1] not in prob_dict:
            prob_dict[item[-1]] = 1
        else:
            prob_dict[item[-1]] += 1
    
    for items in list(prob_dict):
        if items in words:
            prob_val = (prob_dict[items]) / len(edtlst)
            if prob_val < 0:
                prob_val = 0
        else:
            prob_val = prob_dict[items] / len(edtlst)
        prob_dict[item] = prob_val
    largest_value = 0
    largest_key = None

    #print(prob_dict)
    
    for key, value in prob_dict.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    
    if largest_key not in words:
        words[largest_key] = 1
    else:
        words[largest_key] += 1

    #largest_key = random.choice(list(prob_dict.keys()))
    #print(largest_key)

    if largest_key == None:
        largest_key = "I"
    
    if largest_key.isalpha():
        if sub[-1] == "'":
            return [largest_key, advd_token]
        elif sub[-1] in [".", ":", ";", "!", "?"]:
            return [" " + largest_key.title(), advd_token]
        elif sub[-5:] in ["<ans>"]:
            return [largest_key.title(), advd_token]
        else:
            return [" " + largest_key, advd_token]
    else:
        return [largest_key, advd_token]

while True:
    cmd_value = input("Prompt: ")
    cmd_total = None
    cmd_append = cmd_value + "<ans>"
    tokens_use = text_token
    for j in range(0, 400):
        cmd_total = predict(tokens_use, cmd_append)
        cmd_value = cmd_total[0]
        tokens_use = cmd_total[1]
        cmd_append += " " + cmd_value
        if cmd_value == "<end>":
            break
        print(cmd_value, end="")
    print()
