import time
from flask import Flask, jsonify


app = Flask(__name__)

toplam_ziyaretci_sayisi = 0
@app.route("/")
def anasayfa():
    global toplam_ziyaretci_sayisi
    mevcut_ziyaretci_sayisi = toplam_ziyaretci_sayisi
    time.sleep(0.1)
    yeni_ziyaretci_sayisi = mevcut_ziyaretci_sayisi + 1
    toplam_ziyaretci_sayisi = yeni_ziyaretci_sayisi
    return jsonify({"ziyaretci_sayisi": toplam_ziyaretci_sayisi})

if __name__ == "__main__":
    app.run(debug=True, threaded=True, use_reloader = False)
