class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'INI ADALAH LUAS OBJECT SEGITIGA DENGAN ALAS = {self.alas} DAN TINGGI = {self.tinggi}'

    def luas(self):
        return self.alas * self.tinggi / 2
