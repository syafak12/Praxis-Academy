from random import randint


# Buat list option untuk permainan
Glist = ["Gunting", "Batu", "Kertas"]

# buat pilihan secara random dengan func randint
syafak = Glist[randint(0,2)]

# Set pemain ke False
doni = False

while doni == False:
    #Set pemain ke True
    doni = input("Gunting, Batu, Kertas ? : ")
    if doni == syafak:
        print("Seri!")
    elif doni == "Batu":
        if syafak == "Kertas":
            print("Kamu Kalah!", syafak, "membungkus", doni)
        else:
            print("Kamu Menang!", doni, "menghancurkan", syafak)
    elif doni == "Kertas":
        if syafak == "Gunting":
            print("Kamu Kalah!", syafak, "memotong", doni)
        else:
            print("Kamu Menang!", doni, "membungkus", syafak)
    elif doni == "Gunting":
        if syafak == "Batu":
            print("Kamu Kalah!", syafak, "menghancurkan", doni)
        else:
            print("Kamu Menang!", doni, "momotong", syafak)
    else:
        print("Pilihan yang kamu masukan salah...")

    # Set pemain ke False lagi supaya terjadinya looping yang berulang

    doni = False1
syafak = Glist[randint(0,2)]