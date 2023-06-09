"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Barbora Benešová
email: benes.barbora@seznam.cz
discord: Barbora B.#4707
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
users = {
    "bob": {"password": "123"},
    "ann": {"password": "pass123"},
    "mike": {"password": "password123"},
    "liz": {"password": "pass123"}
}

username_input = input("username: ")
password_input = input("password: ")
if username_input in users:
    if password_input == users[username_input]["password"]:
        print(40 * "-")
        print(f"Welcome to the app, {username_input}")
    else:
        print("Wrong password, terminating the program..")
        exit()
else:
    print("Unregistered user, terminating the program..")
    exit()

print("We have 3 texts to be analyzed.")
print(40 * "-")
text_choice = input("Enter a number btw. 1 and 3 to select: ")
print(40 * "-")
if text_choice.isdigit():
    text_choice = int(text_choice)
    if text_choice not in [1, 2, 3]:
        print("Wrong number, terminating the program.")
        exit()
else:
    print("Input must be number, terminating the program.")
    exit()

for text in TEXTS:
    TEXTS_copy = [text.replace("\n", " ").replace(".", "").replace(",", "").strip() for text in TEXTS]
    TEXTS_copy = [text.split(" ") for text in TEXTS_copy]

number_of_words = (len(TEXTS_copy[text_choice-1]))
print(f"There are {number_of_words} words in selected text.")

titlecase = sum(1 for i in TEXTS_copy[text_choice-1] if i[0].isupper())
print(f"There are {titlecase} titlecase words.")

uppercase = sum(1 for i in TEXTS_copy[text_choice-1] if i.isupper())
print(f"There are {uppercase} uppercase words.")

lowercase = sum(1 for i in TEXTS_copy[text_choice-1] if i.islower())
print(f"There are {lowercase} lowercase words.")

digit = sum(1 for i in TEXTS_copy[text_choice-1] if i.isdigit())
print(f"There are {digit} numeric strings.")

digit_sum = sum(int(i) for i in TEXTS_copy[text_choice-1] if i.isdigit())
print(f"The sum of all the numbers {digit_sum}.")

frequency = {}
for i in TEXTS_copy[text_choice-1]:
    if len(i) not in frequency:
        frequency[len(i)] = 1
    else:
        frequency[len(i)] += 1

print(40 * "-")
print(f"{'LEN':3}|{'   OCCURENCES':20}|{'NR.':3}")
print(40 * "-")
frequency_sorted = sorted(frequency.items())
for i, j in frequency_sorted:
    print(f"{i:3}|{'*'*j:20}|{j:3}")