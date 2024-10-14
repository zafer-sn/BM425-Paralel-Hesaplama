def bilgi_goster(**kwargs):
    for i in kwargs.keys():
        print(type(i))

#sozluk = {"isim":"Zafer", "yas":28}
bilgi_goster(isim="Zafer", yas = 28)