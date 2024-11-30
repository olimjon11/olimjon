#1

sonlar = [1, 2, 3, 4, 5]
yangi_royxat = [son * 2 for son in sonlar]
print("Yangi ro'yxat:", yangi_royxat)

#2

sonlar = [7, 2, 9, 4, 3, 5]
eng_kichik = min(sonlar)
print("Eng kichik son:", eng_kichik)

#3

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
faqat_toqlar = [son for son in sonlar if son % 2 != 0]
print("Faqat toq sonlar:", faqat_toqlar)

#4

sozlar = ["salom", "dunyo", "python", "dasturlash"]
bosh_harflar = [soz.capitalize() for soz in sozlar]
print("Bosh harflar bilan ro'yxat:", bosh_harflar)

#5

royxat = [1, 2, 3, 4, 5, 6, 7, 8]
uzunlik = len(royxat)
orta = uzunlik // 2
birinchi_qism = royxat[:orta]
ikkinchi_qism = royxat[orta:]
print("Birinchi qism:", birinchi_qism)
print("Ikkinchi qism:", ikkinchi_qism)

#6

royxat = [1, 2, 3, 4, 5]
aylantirilgan_royxat = [royxat[-1]] + royxat[:-1]
print("Aylantirilgan ro'yxat:", aylantirilgan_royxat)

#7
royxat = [1, "salom", 3.14, "dunyo", True, "python", 42]
faqat_stringlar = [elem for elem in royxat if isinstance(elem, str)]
print("Faqat string elementlar:", faqat_stringlar)

#8

royxat = [[1, 2, 3], [4, 5], [6, 7, 8], 9, 10]
birinchi_elementlar = []
for element in royxat:
    if isinstance(element, list):  
        birinchi_elementlar.append(element[0])
print("Birinchi elementlar:", birinchi_elementlar)

#9

sozlar = ["olma", "anjir", "gilos", "nok", "shaftoli", "banan"]
tartiblangan = sorted(sozlar, key=len)
print("Uzunligiga qarab togirlangan ro'yxat:", togirlangan)