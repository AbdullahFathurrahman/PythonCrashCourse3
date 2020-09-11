from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('MENGGUNAKAN OBJECT ORIENTED PROGRAMMING')

print('\nPERSEGI PANJANG')
p1 = PersegiPanjang(40, 20)
print(p1.info())
print(p1.luas())

print('\nSEGITIGA')
s1 = Segitiga(20, 10)
print(s1.info())
print(s1.luas())

print('\nMENCOBA MEMBUAT OBJECT DARI KELAS BANGUN RUANG')

b1 = BangunRuang()
print(b1.luas())
print(b1.info())

# POLIMORPHISME KEMAMPUAN OBJECT UNTUK MERESPON BERBEDA PEMANGGILAN METHOD YANG SAMA
daftar_bangun_ruang = [p1, s1]

for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
