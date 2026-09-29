#Tuliskan kode untuk tugas-tugas berikut! Kemudian, tunjukkan hasilnya kepada pengajar atau asisten untuk mendapatkan penilaian!
#Saat Anda menunjukkan kode tersebut, pengajar atau asisten akan mengajukan beberapa pertanyaan untuk mengetahui sejauh mana pemahaman Anda terhadap materi yang telah dipelajari.

#1. Buatlah sebuah fungsi yang mengonversi suhu dari Celsius ke Fahrenheit dan sebaliknya. Fungsi ini menerima dua parameter, yaitu nilai suhu dan satuan suhu ('C' untuk Celsius, 'F' untuk Fahrenheit).
#f = (Celsius . 9/5)+ 32
#Celsius = (*F - 32) 5/9

#2. Gunakan fungsi lambda untuk membuat fungsi yang menghitung luas lingkaran! Input yang digunakan adalah jarak dari pusat lingkaran ke tepinya (jari-jari lingkaran).

import math
#1.
def konversi_suhu(value, unit):
    if unit == "C":
        return (value * 9/5) + 32
    elif unit == "F":
        return (value - 32) * 5/9
    else:
        return "nilai tidak ditemukan. Gunakan c dan f"

#2.
sum = lambda p,r: math.pi*(r*r)
print ("value of cycle area : ", sum (math,r=12))
