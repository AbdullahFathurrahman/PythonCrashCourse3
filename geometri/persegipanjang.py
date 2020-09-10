class PersegiPanjang():

    def __init__(self, panjang, lebar):
        # fungsi yg dipanggil pertama kali
        self.panjang = panjang
        self.lebar = lebar

    def info(self):
        return f'INI ADALAH LUAS OBJECT PERSEGIPANJANG DENGAN PANJANG = {self.panjang} DAN LEBAR = {self.lebar}'

    def luas(self):
        return self.panjang * self.lebar