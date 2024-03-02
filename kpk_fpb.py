#!/usr/bin/env python
# coding: utf-8

# In[7]:


def hitung_fpb_kpk():
    print("Pilihan:")
    print("1. FPB")
    print("2. KPK")

    pilihan = int(input("Masukan pilihan (1/2): "))

    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input("Masukan angka kedua: "))

    def fpb(a, b):
        # Hitung FPB
        while b:
            a, b = b, a % b
        return a

    def kpk(a, b):
        #Hitung KPK
        return abs(a*b) // gcd(a, b)

    if pilihan == 1:
        # FPB
        hasil = fpb(angka1, angka2)
        print(f"FPB dari {angka1} dan {angka2} adalah: {hasil}")
    elif choice == 2:
        # KPK
        hasil = kpk(angka1, angka2)
        print(f"KPK dari {angka1} dan {angka2} adalah: {hasil}")
    else:
        print("Pilihan Salah")

hitung_fpb_kpk()


# In[ ]:




