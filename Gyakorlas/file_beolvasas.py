
# 'r' read (olvasas)
# 'w' write (iras)
# 'a' append (hozzzasfuzes, mellekel)


#f = open('mondasok.txt', 'r', encoding='utf-8')

#sor = f.readline()
#print(sor.strip())     # a .strip() a plusz sor hozzáadását törli

#sor = f.readline()
#print(sor.strip())

#sor = f.readline()
#print(sor.strip())

#sor = f.readline()
#print(sor.strip())

# De ha nem akarom ilyen sokszor leirni akkor igy egyszerűbb

#for sor in f:
#   print(sor.strip())

# De lehet while ciklussal is kiiratni

#sor = f.readline()   # De egy sor már előre be kell olvasnunk a file-bol
#while sor:
#    print(sor.strip())
#    sor = f.readline()


#f.close()


# van az a módszer amikor nem akarom, vagy nem kell lezárni a beolvasást akkor
# az alábbi módszer alkalmas rá


with open('mondasok.txt', 'r', encoding='utf-8') as f:
    for sor in f:
        print(sor.strip())

with open('mondasok.txt', 'r', encoding='utf-8') as f:
    sor = f.readline()      # AEgy sor beolvasása egyesével

    while sor:              # Addig amig van sor
        print(sor.strip())  # Printeljew kis a sorokat
        sor = f.readline()
