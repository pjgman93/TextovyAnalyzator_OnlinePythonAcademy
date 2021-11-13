'''
author = Petr JANÍK
'''
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

ODDELOVAC = 40 * "-"

databaze_uzivatelu = dict()
# databaze_uzivatelu = {"bob": "123"}
databaze_uzivatelu["bob"] = "123"
databaze_uzivatelu["ann"] = "pass123"
databaze_uzivatelu["mike"] = "password123"
databaze_uzivatelu["liz"] = "pass123"

# ziskani vstupu od uzivatele a overeni totoznosti

user = input("username: ")
password = input("password: ")

print(ODDELOVAC)

if user not in databaze_uzivatelu.keys():
    print(f"User '{user}' is not registered. Terminating...")
    quit()
else:
    if password != databaze_uzivatelu.get(user):
        print("Wrong password. Terminating...")
        quit()

print(f"Welcome to our app, {user}!")
print("We have 3 texts to be analyzed.")

print(ODDELOVAC)

choice = input("Enter the number of the text to be analyzed (1 - 3): ")
choices = ["1", "2", "3"]           # nejak jsem tu nevedel, jak to udelat jinak, rafinovaneji?

if not choice.isdigit():            # kdybych mel promenou choice jako int(input), nemohl bych tu pouzit metodu stringu
  print("This is not a number. Terminating...")
  quit()
elif choice not in choices:          # s promenou choice typu int bych tu pak mohl vyuzi obecnejsi zapis jako: ... not in range(len(TEXTS) + 1)
  print("You have to enter a number from 1 to 3. Terminating...")
  quit()

print(ODDELOVAC)

# vlastni skript
# rozsekani na slova a ocesteni

text = TEXTS[(int(choice)) - 1]

text = text.replace("-", " ")       # toto nahrazeni jsem provedl, abych rozdelil slozena slova jako "buff-to-white", ale uplne jsem si nebyl jist, zda to nebrat jako jedno slovo..

words = [word.strip(",.@{}&~ˇ^˘+''°˛`„-–´˝÷<>*()#đ“") for word in text.split()]

alpha_words = []                    # pro analyzu uppercase a lowercase (30N vyhodnoceno jako uppercase, 30n jako lowercase, ale vzhledem k cislicim ve slove bych to tak uplne nevidel
for word in words:
    if word.isalpha():
        alpha_words.append(word)

# pocet slov

sum_words = len(words)              # nebyl jsem si jist, zda mam mezi slova pocitat i cisla, nebo napr. "30N", rozhodl jsem se pocitat

# počet slov začínajících velkým písmenem

titlecase_words = 0

for word in words:
    if word.istitle():
        titlecase_words += 1

# počet slov psaných velkými písmeny
uppercase_words = 0

for word in alpha_words:
    if word.isupper():
        uppercase_words += 1

# počet slov psaných malými písmeny
lowercase_words = 0

for word in alpha_words:
    if word.islower():
        lowercase_words += 1

# počet čísel (ne cifer)
notalpha_words = set(words) - set(alpha_words)          # toto uz je priprava na dalsi krok, tedy soucet cisel (budu je potrebovat jako type int)
                                                        # takto to delam s ohledem na cisla, ktera nejsou ve slove osamocena, tj. napr. to "30N", tzn. nemohu pouzit metodu ".isdigit"
# for word in words:
#     if word.isalnum() and not word.isalpha():         # takto pres listy mi to prislo kostrbate
#         notalpha_words.append(word)

numbers = len(notalpha_words)

# sumu všech čísel (ne cifer) v textu.
digit_words = []

for word in notalpha_words:
  for case in word:                         # tady odmazavam pismena ze stringu, kde jsou kombinovana cisla s pismeny, opet napr. 30N
    if not case.isdigit():
      word = word.replace(case, " ")
  digit_words.append(word)

sum_numbers = 0

for i in range(len(digit_words)):
    sum_numbers = sum_numbers + int(digit_words[i])

# proc mi to PROSIM nefunguje takto??? nekde jsme to takto urcite pouzivali, jde mi o to definovani promene s podminkou resp. for cyklem
# sum_numbers = sum_numbers + int(digit_list[i]) for i in range(len(digit_list))

print(f"There are {sum_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numbers} numeric strings.")
print(f"The sum of all the numbers is {sum_numbers}.")

print(ODDELOVAC)

# delka slov

delky_slov = []

for word in words:
    delka = len(word)
    delky_slov.append(delka)

delky_slov.sort()

vyskyt_slov_danych_delek = {}
for delka in delky_slov:
    if not delka in vyskyt_slov_danych_delek.keys():
        vyskyt_slov_danych_delek[delka] = 1
    else:
        vyskyt_slov_danych_delek[delka] += 1

# graficke znazorneni statistiky delky slov

max_pocet = max(pocet for pocet in vyskyt_slov_danych_delek.values())

sirka_sloupce_occ = int()
if max_pocet % 2 == 1:
    sirka_sloupce_occ = max_pocet + 3
else:
    sirka_sloupce_occ = max_pocet + 2

odsazeni = int((sirka_sloupce_occ - len("occurences"))/2)

print(ODDELOVAC)
print("LEN"+"|"+ " "*odsazeni + "OCCURANCES" + " "*odsazeni + "|NR.")
print(ODDELOVAC)

for delka, pocet in vyskyt_slov_danych_delek.items():
    print(" "*(3-len(str(delka))) + str(delka) + "|" + "*"*pocet + " "*(sirka_sloupce_occ - pocet) + "|" + str(pocet))