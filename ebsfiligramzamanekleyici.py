import os
import time
from PIL import Image, ImageDraw, ImageFont

# ---------- AYARLAR ----------
MUSTERI_KLASORU = r"C:\Users\siyahmuhafiz\Desktop\denemeebsresi"  # Müşteri klasörlerinin olduğu ana dizin
AYIRT_EDICI_EK = "_tarihli"  # İşlem gören resimlerin sonuna eklenecek takı
FONT_BOYUTU = 24  # Yazı boyutu (Özel font yüklenirse aktif olur)
METIN_RENGI = (255, 255, 255, 220)  # Beyaz renk ve hafif şeffaflık (RGBA)
ARKA_PLAN_RENGI = (0, 0, 0, 100)  # Metnin arkasına hafif siyah şeffaf şerit (Okunabilirlik için)
# ----------------------------

def dosya_tarihi_al(dosya_yolu):
    """Dosyanın en eski zaman damgasını (oluşturulma/değiştirme) alır ve formatlar."""
    try:
        stat = os.stat(dosya_yolu)
        # Windows'ta st_ctime oluşturulmadır ancak garanti olması için en eskisini alıyoruz
        en_eski_zaman = min(stat.st_ctime, stat.st_mtime)
        return time.strftime("%d.%m.%Y %H:%M", time.localtime(en_eski_zaman))
    except Exception:
        return time.strftime("%d.%m.%Y %H:%M")  # Hata durumunda güncel zamanı dön

def tarih_damgasi_ekle():
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
                    # Resmi RGBA modunda açıyoruz (Şeffaf katman desteği için)
                    ana_resim = Image.open(tam_resim_yolu).convert("RGBA")
                    
                    # 1. Yazılacak Tarih Verisini Al
                    tarih_metni = dosya_tarihi_al(tam_resim_yolu)
                    
                    # 2. Font Ayarla
                    try:
                        # Sisteminizde arial varsa onu kullanır, yoksa varsayılana düşer
                        font = ImageFont.truetype("arial.ttf", FONT_BOYUTU)
                    except IOError:
                        font = ImageFont.load_default()
                    
                    # Çizim objesi oluşturma
                    duzenleyici = ImageDraw.Draw(ana_resim)
                    
                    # Metnin boyutlarını hesapla (Sağ alta tam hizalamak için)
                    metin_kutusu = duzenleyici.textbbox((0, 0), tarih_metni, font=font)
                    metin_genisligi = metin_kutusu[2] - metin_kutusu[0]
                    metin_yuksekligi = metin_kutusu[3] - metin_kutusu[1]
                    
                    # Sağ alttan bırakılacak boşluk (Margin)
                    ofset_x = 20
                    ofset_y = 20
                    
                    # Koordinatları hesapla
                    x = ana_resim.size[0] - metin_genisligi - ofset_x
                    y = ana_resim.size[1] - metin_yuksekligi - ofset_y
                    
                    if x < 0 or y < 0:
                        continue

                    # 3. Okunabilirliği Artırmak İçin Metnin Arkasına Hafif Arka Plan Çiz (İsteğe Bağlı)
                    # Arka plan kutusu koordinatları
                    bg_pad = 6  # Metin etrafındaki dolgu
                    duzenleyici.rectangle(
                        [x - bg_pad, y - bg_pad, x + metin_genisligi + bg_pad, y + metin_yuksekligi + bg_pad],
                        fill=ARKA_PLAN_RENGI
                    )
                    
                    # 4. Metni Yazdır
                    duzenleyici.text((x, y), tarih_metni, font=font, fill=METIN_RENGI)
                    
                    # JPG/JPEG ise tekrar RGB'ye dönüştürerek kaydet
                    if dosya_uzantisi.lower() in ('.jpg', '.jpeg'):
                        ana_resim = ana_resim.convert("RGB")
                    
                    ana_resim.save(yeni_resim_yolu)
                    ana_resim.close()
                    
                    # Orijinal resmi sil
                    os.remove(tam_resim_yolu)
                    
                except Exception as e:
                    # Geliştirme aşamasında hataları görmek isterseniz alt satırı aktifleştirebilirsiniz
                    # print(f"Hata oluştu ({dosya}): {e}")
                    pass

if __name__ == "__main__":
    tarih_damgasi_ekle()