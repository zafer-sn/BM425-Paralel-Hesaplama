meyveler = ["elma", "armut", "portakal", "nar"]
sebzeler = ["domates", "salatalık", "maydonoz", "biber"]
meyveler = sebzeler.copy()
meyveler[0] = "mandalin"
sebzeler[1] = "patlıcan"
meyveler[2] = "şeftali"
sebzeler[3] = "marul"
print(*meyveler)
print(*sebzeler)