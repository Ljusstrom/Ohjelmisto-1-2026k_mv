# matkat = { "aikuinen": 330,
#            "lapsi":    170,
#            "ratikka":  100 }
#
# # Palauttaa true tai false, sen mukaan onko saldoa halvimman lipun hinta tai enemmän
# def saldoa_on(saldo_nyt):
#     return (saldo_nyt >= matkat["ratikka"]) # tarkistetaan halvimman matkan mukaan
#
# # Vähennetään yksi matka saldosta (hinta parametrina)
# def matkusta(saldo_nyt, hinta):
#     if saldo_nyt >= hinta:
#         saldo_nyt = saldo_nyt - hinta
#     return saldo_nyt
#
# def päättele_matkan_hinta(matkatyyppi):
#     if matkatyyppi.lower() in matkat:   # Testataan onko avain matkatyyppi matkat-sanakirjassa
#         return matkat[matkatyyppi.lower()]
#     else:
#         print("Matkatyyppi väärä ", matkatyyppi)
#         return 0
#
# saldo_euroissa = float(input("Lataa alkusaldo (euroissa): "))
# saldo = int(saldo_euroissa * 100) # muutetaan senteiksi ja kokonaisluvuksi
#
# while saldoa_on(saldo):
#     matkatyyppi = input("Minkä matkan haluat leimata? aikuinen, lapsi, ratikka: ")
#     matkan_hinta = päättele_matkan_hinta(matkatyyppi)
#     if matkan_hinta <= saldo:
#         saldo = matkusta(saldo, matkan_hinta)
#         print(f"Matkustit ja saldoa on jäljellä {(saldo/100):.2f} euroa.")
#     else:
#         print(f"Saldo ei riittänyt matkaan. Saldo {saldo/100:.2f}, matka: {matkan_hinta/100}")
#
# print(f"Saldosi loppui, et voi enää matkustaa.")

# lista = [1, 2, 'a', "makkara"] # lista
# lista[1] = 5
# for i in lista:
#     print(i)

# monikko = (3, 4, 'b', "nakki") # monikko
# #monikko[1] = 5 EI VOI MUOKATA MONIKKOA
# for i in monikko:
#     print(i)

# joukko = { 1, 2, 1, 3, 4, 5, 5 }
# joukko.remove(4)
# joukko.add("heippa")
# joukko.add(5)
# for i in joukko:
#     print(i)

# matkat = { "Aikuinen": 330,
#            "Lapsi": 170 }
#
# print(f"Aikuisten matkan hinta: {matkat["Aikuinen"]}")


# #Listaan viittaus
lista = [ 1, 2, 3, "Matti", (2,3), 'X']
# print("Listamme pituus", len(lista))
# # print(lista[0])  # lista ensimmäinen alkio
# # print(lista[-1]) # listan viimein alkio
# # print(lista[1:3]) # alkiot 1 ja 2
# # print(lista[1:]) # viisi viimeistä alkiota
# # print(lista[:3]) # kolme ensimmäistä alkiota
# # print(lista[::-1]) # lista väärinpäin.
# print(lista)
# for i in lista:
#     print(i)

for i in range(len(lista)-1, -1, -1): # lista väärinpäin tulostettuna, allekain
    print(lista[i])
