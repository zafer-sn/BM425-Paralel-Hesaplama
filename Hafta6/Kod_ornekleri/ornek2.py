import json
import string
import time
import urllib.request
def count_letter(l_dict, url):
    response = urllib.request.urlopen(url)
    r_txt = str(response.read().decode("utf-8"))
    # r_txt.replace(" ", "")
    # print(r_txt)
    for l in r_txt:
        letter = l.lower()
        if letter in l_dict:
            l_dict[letter] += 1

le_dict = {}
ing_harfler = string.ascii_lowercase

for i in ing_harfler:
    le_dict[i] = 0

baslangic_zamani = time.time()
for i in range(1000, 1051):
    count_letter(le_dict, f"https://www.rfc-editor.org/rfc/rfc{i}.txt")
bitis_zamani = time.time()
print(json.dumps(le_dict, indent=4))
print(f"Geçen süre: {bitis_zamani-baslangic_zamani}")
