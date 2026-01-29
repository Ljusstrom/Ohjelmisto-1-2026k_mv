# def tervehdi(kerta):
#     for i in range(kerta):
#         print(f"Heippa! {i+1}. kerta")
#     print("Olen funktion lopussa.")
#     return
#
# # tästä alkaa ohjelma pääosuus (main):
# tervehdi(5)
# tervehdi(1)
#
# print("Ohjelma loppuu.")

# Moduuli 4:stä esimerkki
# def ohje():
#     print("Komennot:")
#     print("1) Laske - Suorita laskenta")
#     print("2) Tulos - Tulosta laskennan tulos")
#     print("3) lopeta - Lopettaa ohjelman")
#
# komento = input ('Anna komento ("ohje" antaa ohjeen): ')
# while komento != "lopeta" and komento != "Lopeta": # ehto: "Laske" != "lopeta" and "Laske" != "Lopeta"
#     if komento == "ohje":
#         ohje()
#     else:
#         print ("Suoritan toiminnon: " + komento)
#     komento = input("Anna komento: ")
# print ("Toiminnot lopetettu.")

# Muuttujien näkyvyys:
# def vaihda(city):
#     city = "Vantaa"
#     return
#
# kaupunki = "Helsinki"
# print(kaupunki)
# vaihda(kaupunki) # kaupunki parametrina funktiolle
# print(kaupunki) # ? -> Helsinki, koska city="Vantaa" on lokaali muutos

# def vaihda(city):
#     city[0] = "Vantaa"
#     return
#
# kaupunki = ["Helsinki"]
# print(kaupunki)
# vaihda(kaupunki) # kaupunki parametrina funktiolle
# print(kaupunki) # ? -> Helsinki, koska city="Vantaa" on lokaali muutos

# Esimerkki - lista parametrina
# def inventaario(tavarat):
#     print("Sinulla on seuraavat tavarat:")
#     for t in tavarat:
#         print ("- " + t)
#     # Tavarat katoavat inventaariossa!
#     tavarat.clear()
#     return
#
# reppu = ["Vesipullo", "Kartta", "Kompassi"]
# inventaario(reppu)
# reppu.append("Linkkuveitsi")
# inventaario(reppu)

# Useampi parametri
# def tervehdi(tervehdys, kerta):
#     for i in range(kerta):
#         print(f"{tervehdys}! {i+1}. kerta")
#     return
#
# # tästä alkaa ohjelma pääosuus (main):
# tervehdi("Moikka", 4)
# tervehdi("Hyvää päivää", 2)
#
# print("Ohjelma loppuu.")

# funktion paluuarvo
# def neliosumma(eka, toka):
#     ns = eka**2 + toka**2
#     return ns
#
# luku1 = float(input("Anna ensimmäinen luku: "))
# luku2 = float(input("Anna toinen luku: "))
# tulos = neliosumma(luku1, luku2)
# print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}.")

# Muuttujien näkyvyys muokattuna paluuarvolla:
# def vaihda():
#     return "Vantaa"
#
# kaupunki = "Helsinki"
# print(kaupunki)
# kaupunki = vaihda() # kaupunki parametrina funktiolle, paluuarvo kaupunki-muuttujaan
# print(kaupunki)     # ? -> Vantaa

# vaihtuvan mittaiset argumentit
# def summa(*luvut):
#     s = 0
#     for l in luvut:
#         s += l
#     return s
#
# tulos = summa(1, 2, 3, 4)
# print(f"Summa on {tulos}")

# Parametrien välittäminen avainsanojen avulla:
# def tervehdi(tervehdys="Hei", kerrat=1):
#     for i in range(kerrat):
#         print(tervehdys + " " + str(i + 1) + ". kerran")
#     return
#
# # tervehdi()
# # tervehdi("Terve", 3)
# # tervehdi(kerrat=2, tervehdys="Moro")
# tervehdi(kerrat=6) # -> Hei kuusi kertaa

import random

def arvo_luku():
    return random.randint(1, 13)

def tervehdi(tervehdys):
    kerrat = arvo_luku()
    for i in range(kerrat):
        print(tervehdys + " " + str(i + 1) + ". kerran")
    return

tervehdi("Moikka")