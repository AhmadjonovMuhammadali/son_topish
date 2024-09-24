# Son_topish_oyini

import Son_top as st
import Son_top_pc as stp

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = st.son_top(x)
        taxminlar_pc = stp.Son_top_pc(x)
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): "))
        