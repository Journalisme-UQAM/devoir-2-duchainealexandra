#coding utf-8

import csv 

fichier = "concordia1.csv"

f1 = open(fichier)

lignes = csv.reader(f1)

for ligne in lignes:
    if "M." in ligne[6]:
        type="maitrise"
        # print(ligne[6])
    else:
        type="doctorat"
        # print(ligne[6])
    
    # print(ligne[2])
    longTitre=len(ligne[2])
    # print(longTitre)
    
    # print(ligne[5])
    if "leaves" in ligne[5]:
        fin=ligne[5].find("leaves")
        chiffre=ligne[5][fin-4:fin].strip()
        if chiffre == "":
            chiffre=ligne[5][fin-3:fin].strip()
            # print(ligne[5])
        elif chiffre == "l00":
            chiffre=100
        elif chiffre=="ii,":
            # prend le pas
            break
            # print(ligne[5])
       
        chiffre=int(chiffre)
        # print(chiffre)
    
    if ligne[5][0]== "x":
        # print(ligne[5])
        fin=ligne[5].find(",")
        romain=ligne[5][0:6].strip()
        if ligne[5][3] == ",":
            romain=ligne[5][0:3]
        elif ligne[5][4] == ",":
            romain=ligne[5][0:4]
        elif ligne[5][5] == ",":
            romain=ligne[5][0:5]
        elif ligne[5][2] == ",":
            romain=ligne[5][0:2]
        elif ligne[5][1] == ",":
            romain=ligne[5][0:1]
        elif ligne[5][6] == ",":
            romain=ligne[5][0:6]
        # print(romain)
        
d = {
    "i" : 1,
    "ii" : 2,
    "iii" : 3,
    "iv": 4,
    "v": 5,
    "vi": 6,
    "vii": 7,
    "viii": 8,
    "ix": 9,
    "x": 10,
    "xi": 11,
    "xii": 12,
    "xiii": 13,
    "xiv": 14,
    "xv": 15,
    "xvi": 16,
    "xvii": 17,
    "xviii": 18,
    "xix": 19,
    "xx": 20,
    "xxi": 21,
    "xxii": 22,
    "xxiii": 23,
    "xxiv": 24,
    "xxv": 25,
    "xxvi": 26,
    "xxvii": 27,
    "xxviii": 28,
    "xxix": 29,
    "xxx": 30,
    "xxxi": 31,
    "xxxii": 32,
    "xxxiii": 33,
    "xxxiv": 34,
    "xxxv": 35,
    "xxxvi": 36,
    "xxxvii": 37,
    "xxxxviii": 38,
    "xxxxix": 39,
    "xl" : 40,
    "xli" : 41,
    "xlii" : 42,
    "xliii": 43,
    "xliv": 44,
    "xlv": 45,
    "xlvi": 46,
    "xlvii": 47,
    "xliii": 48,
    "xliv": 49,
    "l" : 50,
    "li" : 51,
    "lii" : 52,
    "liii" : 53,
    "liv": 54
    }

# print(d.values())


    #je ne comprends plus comment faire. Voici mes pistes de réflexion : 
    
    #if romain == d.keys():
        #print(d.values())
        
# nbPages = x + chiffre

# print("La {} de {} compte {nbPages}. Son titre est {} {longTitre}"")
