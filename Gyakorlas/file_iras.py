
# 'r' read (olvasas)
# 'w' write (iras)
# 'a' append (hozzzasfuzes, mellekel)


#with open('mondasok.txt', 'r', encoding='utf-8') as infile:
#    with open('out.txt', 'w', encoding='utf-8') as outfile:
#        sor = infile.readline()
#        while sor:
#            outfile.write(sor)
#            sor = infile.readline()

with open('out.txt', 'a', encoding='utf-8') as file:   # itt az a beillesztést jelöli
    ujsor = '\nNem akarásnak nyögés a vége.'           # \n ezzel töröm a sort a beolvasásánál

    file.write(ujsor)