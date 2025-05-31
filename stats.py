import string

def word_count(text):
    count = len(text.split())
    
    return count

def char_count(words):
    lower_words = words.lower()
    # all_words = lower_words.split()
    alpha_chars = list(string.printable)
    count_dict = {}

    for char in alpha_chars:
        c_count = 0
        for l in lower_words:
            if l == char:
                c_count += 1
    
        if c_count == 0 :
            pass
        elif c_count >0 :
            count_dict.update({char: c_count})
    
   
    return count_dict

def sort_on(dict):
    return dict["num"]

def org_stats(dict):
    dictionaries = []
    
    for entry in dict:
        # print(f"{entry} is {dict[entry]}") 
        if entry.isalpha():
            dictionaries.append({"char":entry, "num":dict[entry]})
    
    dictionaries.sort(reverse=True, key=sort_on)
    
    return dictionaries

# f = open("books/frankenstein.txt")
# a_wor = f.read()
# test_text = a_wor.lower()
# alpha_chars = list(string.printable)
# count_dict = {}

# for char in alpha_chars:
#     c_count = 0
#     for l in test_text:
#         if l == char:
#             c_count += 1
    
#     if c_count == 0 :
#         pass
#     elif c_count >0 :
#         count_dict.update({char: c_count})
#         print(f"there are {c_count} of {char}")
        
# print(alpha_chars)

# for i in test_text:
#     special = 0
#     regular = 0
#     if ord(i) > 127:
#         special += 1

# print(special)    


# f.close

# org_stats(count_dict)