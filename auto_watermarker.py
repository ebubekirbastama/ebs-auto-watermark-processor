import os
from PIL import Image, ImageEnhance

# ---------- AYARLAR ----------
MUSTERI_KLASORU = r"C:\ebs_deneme_resimler"  # Müşteri klasörlerinin olduğu ana dizin
FILIGRAN_RESMI_YOLU = r"C:\logo.png"  # Buraya PNG logonun yolunu yazabilirsin
AYIRT_EDICI_EK = "_filigranli"  # Filigranlanan resimlerin sonuna eklenecek takı
# ----------------------------

def filigran_ekle():
    if not os.path.exists(FILIGRAN_RESMI_YOLU):
        return
    
    try:
        filigran = Image.open(FILIGRAN_RESMI_YOLU).convert("RGBA")
    except Exception:
        return

    # --- ŞEFFAFLIK (OPAKLIK) AYARI ---
    seffaflik_orani = 0.5 
    alpha = filigran.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(seffaflik_orani)
    filigran.putalpha(alpha)
    # ---------------------------------

    uzantilar = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

    for kok_dizin, alt_klasorler, dosyalar in os.walk(MUSTERI_KLASORU):
        for dosya in dosyalar:
            if dosya.lower().endswith(uzantilar):
                
                dosya_adi, dosya_uzantisi = os.path.splitext(dosya)
                if dosya_adi.endswith(AYIRT_EDICI_EK):
                    continue
                
                tam_resim_yolu = os.path.join(kok_dizin, dosya)
                yeni_resim_yolu = os.path.join(kok_dizin, f"{dosya_adi}{AYIRT_EDICI_EK}{dosya_uzantisi}")
                
                try:
                    ana_resim = Image.open(tam_resim_yolu).convert("RGBA")
                    
                    x = ana_resim.size[0] - filigran.size[0] - 20
                    y = ana_resim.size[1] - filigran.size[1] - 20
                    
                    if x < 0 or y < 0:
                        continue

                    ana_resim.paste(filigran, (x, y), mask=filigran)
                    
                    if dosya_uzantisi.lower() in ('.jpg', '.jpeg'):
                        ana_resim = ana_resim.convert("RGB")
                    
                    ana_resim.save(yeni_resim_yolu)
                    ana_resim.close()
                    os.remove(tam_resim_yolu)
                    
                except Exception:
                    pass

if __name__ == "__main__":
    filigran_ekle()
