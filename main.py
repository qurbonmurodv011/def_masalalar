# def yigindi(son1, son2):
#     natija = son1 + son2
#     return natija  

# x = int(input("1-sonni kiritng: "))
# y = int(input("2-sonni kirintg: "))

# print(f"Yig'indisi: {yigindi(x, y)}")

# def summa(a, b):
#     print(f"{a} + {b} = {a + b}")

# summa(3, 5) # Natija: 3 + 5 =8
# summa(10, 20) # Natija: 10 + 20 = 30
    

# def salom_ayt(ism ="do'stim"):
#     print(f"Salom, {ism}!")

#     salom_ayt()        # Natija: Salom, do'stim!
#     salom_ayt("Ali")    # Natija: Salom, Ali !7

# def bolani_malumotlari(ism,yosh):
#     print(f"{ism} {yosh} yoshda.")
#
#
# bolani_malumotlari(ism="Ali", yosh=11)  # Natija: Ali 11 yoshda.
# bolani_malumotlari(yosh=12, ism="Vali")  # Natija: Vali 12 yoshda.


# def min_max(sonlar):
#     return min(sonlar), max(sonlar)
#
# kichik, katta = min_max([1, 2, 3, 4, 5,])
# print(f"Eng kichik: {kichik}, Eng katta: {katta}")  # Natija: Eng kichik: 1, Eng katta: 5


class Transport:
    def __init__(self, model: str, yil: int) -> None:
        self.model = model
        self.yil = yil

    def malumot(self) -> str:
        return f"Model: {self.model}, Yil: {self.yil}"

class Avtomobil(Transport):
    def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
        # Ota klassning __init__ metodini chaqirish
        super().__init__(model, yil)
        self.yonilgi_turi = yonilgi_turi

    def malumot(self) -> str:
        # Ota klassdagi metod natijasiga qo'shimcha qo'shish
        return super().malumot() + f", Yonilg'i: {self.yonilgi_turi}"

class Avtobus(Transport):
    def __init__(self, model: str, yil: int, o_rinlar_soni: int) -> None:
        # Ota klassning __init__ metodini chaqirish
        super().__init__(model, yil)
        self.o_rinlar_soni = o_rinlar_soni

    def malumot(self) -> str:
        # Ota klassdagi metod natijasiga qo'shimcha qo'shish
        return super().malumot() + f", O'rinlar: {self.o_rinlar_soni}"

# Tekshirish uchun namunalar:
avto = Avtomobil("Tesla Model S", 2023, "Elektr")
avtobus = Avtobus("Isuzu", 2021, 35)

print(avto.malumot())
print(avtobus.malumot())

