with open("Hafta3/test.txt", mode="r") as dosya:
    f = dosya.read()
print(f)

with open("Hafta3/test.txt", mode="a") as dosya:
    dosya.write("test4")

with open("Hafta3/test.txt", mode="r") as dosya:
    f = dosya.read()
print(f)