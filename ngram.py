from nltk.tokenize import word_tokenize
from collections import Counter
words = {}
with open('sentences.txt', 'r') as file:
    text = file.read()
    text_token = word_tokenize(text)
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
    edtlst = word_tokenize(sub)
    while True:
        t = len(count_sublist(lst, edtlst))
        if t == 0: #Just like how ~~~the_meaning_of_my_existence == 0~~~ ;(
            edtlst = edtlst[1:len(edtlst)]
        else:
            break
    prob_dict = {}
    for item in count_sublist(lst, edtlst):
        if item[-1] not in prob_dict:
            prob_dict[item[-1]] = 1
        else:
            prob_dict[item[-1]] += 1
    for items in list(prob_dict):
        if items in words:
            prob_val = (prob_dict[items] - words[items]) / len(edtlst)
            if prob_val < 0:
                prob_val = 0
        else:
            prob_val = prob_dict[items] / len(edtlst)
        prob_dict[item] = prob_val
    largest_value = 0
    largest_key = None
    for key, value in prob_dict.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    if largest_key not in words:
        words[largest_key] = 1
    else:
        words[largest_key] += 1
    return largest_key
cmd_value = input("Enter string: ")
words_to_predict = int(input("Enter number: "))
for j in range(0, words_to_predict):
    cmd_value = predict(text_token, cmd_value)
    print(cmd_value, end=" ")
