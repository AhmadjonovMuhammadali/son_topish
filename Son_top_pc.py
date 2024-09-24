# Son topish o'yini | Son_top_pc

import random

def Son_top_pc(x=10):
    input(f"1dan {x}gacha son o'ylang va istalgan tugmani bosing. Men uni topaman?")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t),"
                      f"men o'ylagan son bundan kattaroq(+), yoki kichikroq(-).".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar}ta taxmin bilan topdim.")
    return taxminlar

        
    
    



































