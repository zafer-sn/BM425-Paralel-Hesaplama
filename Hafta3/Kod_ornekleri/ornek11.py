def dis_fonksiyon():
    print("Dış fonksiyon çalıştı")
    def ic_fonksiyon():
        print("İç fonksiyon çalıştı")
    ic_fonksiyon()

dis_fonksiyon()