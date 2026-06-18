# Toplu Resim Filigranlama Aracı

Python ile geliştirilmiş bu araç, belirlenen ana klasör içindeki tüm müşteri klasörlerini tarar ve desteklenen görsel dosyalarına otomatik olarak PNG filigran ekler. Filigranlanan görseller yeni adla kaydedilir ve orijinal dosya silinir.

## Özellikler

- Ana klasör altındaki tüm alt klasörleri otomatik tarar.
- `.jpg`, `.jpeg`, `.png`, `.bmp`, `.webp` formatlarını destekler.
- PNG filigran dosyasını şeffaflık oranıyla uygular.
- Filigranı görselin sağ alt köşesine yerleştirir.
- Daha önce filigran eklenmiş dosyaları tekrar işlemez.
- İşlenen dosyaları `_filigranli` ekiyle yeniden adlandırır.
- Orijinal dosyayı işlemden sonra otomatik siler.

## Gereksinimler

Bu projeyi çalıştırmak için Python 3 ve Pillow kütüphanesi gereklidir.

```bash
pip install pillow
```

## Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/ebubekirbastama/ebs-auto-watermark-processor/proje-adi.git
cd proje-adi
```

Gerekli paketi yükleyin:

```bash
pip install pillow
```

## Kullanım

Kod içerisindeki ayarları kendi sisteminize göre düzenleyin:

```python
MUSTERI_KLASORU = r"C:\ebs_deneme_resimler"
FILIGRAN_RESMI_YOLU = r"C:\logo.png"
AYIRT_EDICI_EK = "_filigranli"
```

Ardından scripti çalıştırın:

```bash
python filigran_ekle.py
```

## Çalışma Mantığı

Program önce filigran dosyasının mevcut olup olmadığını kontrol eder. Filigran dosyası bulunursa RGBA formatında açılır ve belirlenen şeffaflık oranı uygulanır.

Daha sonra ana klasör ve tüm alt klasörler taranır. Desteklenen görsel dosyaları tespit edilir. Eğer dosya adı daha önce belirlenen ayırt edici eki içeriyorsa, dosya tekrar işleme alınmaz.

Filigran, görselin sağ alt köşesine 20 piksel boşluk bırakılarak yerleştirilir. İşlem tamamlandıktan sonra yeni filigranlı dosya kaydedilir ve orijinal dosya silinir.

## Varsayılan Ayarlar

| Ayar | Açıklama |
|---|---|
| `MUSTERI_KLASORU` | Müşteri klasörlerinin bulunduğu ana dizin |
| `FILIGRAN_RESMI_YOLU` | Kullanılacak PNG filigran dosyasının yolu |
| `AYIRT_EDICI_EK` | Filigranlanan dosya adının sonuna eklenecek ifade |
| `seffaflik_orani` | Filigranın opaklık seviyesi |

## Dikkat Edilmesi Gerekenler

Bu script işlemden sonra orijinal görsel dosyasını siler. Bu nedenle kullanmadan önce mutlaka yedek almanız önerilir.

Aşağıdaki satır orijinal dosyanın silinmesini sağlar:

```python
os.remove(tam_resim_yolu)
```

Orijinal dosyaların korunmasını istiyorsanız bu satırı kaldırabilir veya yorum satırı yapabilirsiniz:

```python
# os.remove(tam_resim_yolu)
```

## Örnek Klasör Yapısı

```text
C:\ebs_deneme_resimler
├── Musteri-1
│   ├── resim1.jpg
│   └── resim2.png
├── Musteri-2
│   ├── foto1.webp
│   └── foto2.jpeg
```

İşlem sonrası örnek çıktı:

```text
C:\ebs_deneme_resimler
├── Musteri-1
│   ├── resim1_filigranli.jpg
│   └── resim2_filigranli.png
├── Musteri-2
│   ├── foto1_filigranli.webp
│   └── foto2_filigranli.jpeg
```

## Desteklenen Dosya Formatları

- JPG
- JPEG
- PNG
- BMP
- WEBP

## Önerilen Geliştirmeler

- Grafik arayüz eklenebilir.
- İşlem log kaydı tutulabilir.
- Orijinal dosyayı silme seçeneği ayara bağlanabilir.
- Filigran konumu seçilebilir hale getirilebilir.
- Toplu işlem sonunda rapor üretilebilir.

## Lisans

Bu proje Apache License 2.0 lisansı ile lisanslanmıştır.

Detaylı bilgi için `LICENSE` dosyasını inceleyebilirsiniz.

## Sorumluluk Reddi

Bu yazılım görseller üzerinde kalıcı işlem yapabilir ve mevcut yapılandırmada orijinal dosyaları silebilir. Kullanımdan önce dosyalarınızın yedeğini almanız önerilir. Yazılımın kullanımından doğabilecek veri kaybı veya benzeri durumlardan kullanıcı sorumludur.
