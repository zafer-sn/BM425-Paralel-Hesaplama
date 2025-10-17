try:
    sayi1 = int(input("Lütfen bir sayi değeri giriniz..:"))
    sayi2 = int(input("Lütfen bir sayi değeri giriniz..:"))
except ValueError as ve:
    print(ve)
except NameError as ne:
    print(ne)
except:
    print("Hata!")