# Esimerkki 1
# kerrat = int(input("Montako kertaa tervehditään: "))
# tehdyt = 0
# while tehdyt < kerrat: # tehdyt: 0, 1, 2
#     print("Hyvää huomenta")
#     tehdyt = tehdyt + 1
# print("Ohjelma loppui.")

# Esimerkki 2:
# komento = input ("Anna komento: ")
# while komento != "lopeta" and komento != "Lopeta": # ehto: "Laske" != "lopeta" and "Laske" != "Lopeta"
#     print ("Suoritan toiminnon: " + komento)
#     komento = input("Anna komento: ")
# print ("Toiminnot lopetettu.")

# Esimerkki 3:
# import random
#
# noppa1 = noppa2 = heitot = 0 # nollataan kaikki 3 muuttujaa
# while (noppa1 != 6 or noppa2 != 6):
#     noppa1 = random.randint(1, 6)
#     noppa2 = random.randint(1, 6)
#     heitot += 1
#     print(f"Heitit nopat {noppa1}, {noppa2}")
# print(f"Tarvittiin {heitot} heittoa.")

# Esimerkki 4:
# eka = 1
# while eka <= 3:
#     toka = 1
#     while toka <= 3:
#         print(f"{eka} kertaa {toka} on {eka*toka:d}")
#         toka = toka + 1
#     eka = eka + 1

# Esimerkki 5:
# import random
#
# toistot = 0
# heitot_yhteensä = 0
# while toistot < 100_000:
#
#     # Heitetään niin kauan kunnes saadaan kaksi kuutosta
#     noppa1 = noppa2 = heitot = 0
#     while (noppa1!=6 or noppa2!=6):
#         noppa1 = random.randint(1,6)
#         noppa2 = random.randint(1,6)
#         heitot = heitot + 1
#
#     # Kasvatetaan kierroslaskuria ja lasketaan heittojen kokonaismäärä
#     toistot = toistot + 1
#     heitot_yhteensä = heitot_yhteensä + heitot
#
# # keskiarvon laskenta ja tulostus
# heitot_keskimäärin = heitot_yhteensä/toistot
# print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")

# Esimerkki 6 (break):
# komento = input ("Anna komento: ")
# while komento != "lopeta" and \
#       komento != "Lopeta" and \
#       komento != "MAYDAY":
#     print ("Suoritan toiminnon: " + komento)
#     komento = input("Anna komento: ")
# print ("Toiminnot lopetettu.")
# komento = input ("Anna komento: ")
# while komento!="lopeta":
#     if komento=="MAYDAY":
#         break
#     print ("Suoritan toiminnon: " + komento)
#     komento = input("Anna komento: ")
# else:
#     print ("Näkemiin.")
# print ("Toiminnot lopetettu.")

# Esimerkki 7 (ikiluuppi):
# Virheellinen ohjelma, ikuinen silmukka -> Tehkää moduuli 4:n lopussa olevien ohjeiden
# mukaisesti terminaaliemulaatio, jotta voitte keskeyttää ohjelman.
luku = 1
while luku<5:
    print (luku)

# Tänne ei koskaan päästä:
print("Valmista tuli.")