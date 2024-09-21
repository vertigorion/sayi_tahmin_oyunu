import random

def sayi_tahmin_oyunu():
    print("1 ile 100 arasında bir sayı tuttum. Kaç tahminde bulabileceksin?")
    rastgele_sayi = random.randint(1,100)
    tahmin_sayisi = 0

    while True:
        tahmin = int(input("Tahmininiz: "))
        tahmin_sayisi += 1

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayıyla tekrar dene.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayıyla tekrar dene.")
        else:
            print("Tebrikler! " + str(tahmin_sayisi) + " tahminde doğru sayıyı buldun!")
            break            

sayi_tahmin_oyunu()