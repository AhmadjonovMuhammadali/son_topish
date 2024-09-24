# Son topish o'yini | Son_top

import random

def son_top(x=10):
    tanlash = random.randint(1,x)
    print(f"1dan {x}gacha son o'ylandim. Uni topa olasizmi? ")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tanlash:
            print("Xato! Men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
        elif taxmin > tanlash:
            print("Xato! Men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
        else:
            break
    print(f"Topdingiz! Men {tanlash} sonini o'ylagan edim. Siz {taxminlar} taxmin bilan topdingiz Tabriklayman!")
    return taxminlar






































