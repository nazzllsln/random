import random

#random() 0 ile 1  arasında rastgele,uniform() bizim belirlediğimiz kayan virgüllü şekilde sayı randint() ise tam sayıları alır.
#choice() ise diziden rastgele eleman seçer.
#shuffle() ile dizideki elemanları rastgele sıralayabiliriz.
#randrange() tek parametre belirtebiliriz randint ile aynı görevde

#print(random.randint(5,100))
#liste = range(100)
#print(random.sample(liste, 5))


puan = 100
sayi = random.randint(1,100)
hak = int(input("Kaç hak istiyorsunuz? "))
for i in range(hak+1) :
    sayiniz = int(input("1 ile 100 arasında sayı giriniz: "))
    puan = puan-(puan/hak)
    hak = hak - 1
    if (sayiniz!=sayi):
        if (sayiniz<sayi):
            print("sayiniz küçüktür.") 
        elif (sayiniz>sayi):
            print("sayiniz büyüktür. ")
    else:
        print(f"tebrikler bildiniz sayi:{sayi} puanınız:{puan} kalan hak:{hak}")
        break
    if (hak==0):
        print("tahmin hakkiniz kalmamiştir.")
        break




