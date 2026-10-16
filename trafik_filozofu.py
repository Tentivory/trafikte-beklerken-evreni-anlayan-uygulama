#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trafikte Beklerken Evreni Anlayan Uygulama
Bu kod, trafikte beklerken zamanın akışını ve varoluşun derin anlamını keşfetmenizi sağlar.
Gerçekten çalışır. Deneyin.
"""

import time
import random

def bekle_ve_felsefe_yap(dakika=1):
    print("\ud83d\ude97 Trafiğe girdiniz. Motor çalışıyor... (asıl çalışan felsefe motoru)")
    print("Lütfen kornaya basmayın, bu evrenin ritmini bozar.\n")
    
    felsefeler = [
        "Bu kırmızı ışık aslında kırmızı değil, sadece senin gözün yanılıyor. Veya ışık yanılıyor.",
        "Önündeki araba aslında senin gelecekteki sen. O yüzden ona küfretme.",
        "Zaman durduğu anda anladım ki, aslında hiçbir zaman akmıyormuş. Sadece biz bekliyormuşuz.",
        "Bu sıkışıklık, evrenin sana 'biraz yavaş ol' deme şekli. Dinle onu.",
        "Eğer bu trafik sonsuza kadar sürse, acaba kahve soğur mu yoksa ısınır mı? Bilim adamları hala araştırıyor."
    ]
    
    baslangic = time.time()
    while time.time() - baslangic < dakika * 60:
        print(f"[{int(time.time() - baslangic)}s] {random.choice(felsefeler)}")
        time.sleep(random.uniform(2, 5))
    
    print("\n\ud83c\udf89 Trafik bitti! Evreni anladın. Tebrikler, artık daha bilgesin.")
    print("Ama hala geç kaldın. Bu da bir öğreti.")

if __name__ == "__main__":
    try:
        sure = int(input("Kaç dakika bekleyeceksin? (varsayılan 1): ") or 1)
        bekle_ve_felsefe_yap(sure)
    except KeyboardInterrupt:
        print("\n\u26a1 Aniden yeşil yandı! Felsefe yarıda kaldı. Evren seni affetmeyecek.")
    except ValueError:
        print("Sayı gir be abi, trafik zaten yeterince kafa karışık.")
