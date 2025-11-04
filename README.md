# 📧 Otomatik Mail Gönderme Uygulaması

Modern ve kullanıcı dostu bir web arayüzü ile toplu mail gönderme uygulaması. Staj başvuruları ve iş başvuruları için idealdir.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Özellikler

- 🎨 **Modern Web Arayüzü**: Kullanıcı dostu, responsive tasarım
- 📝 **Canlı Mail Editörü**: Gerçek zamanlı önizleme ile mail içeriğini düzenleyin
- 🏢 **Dinamik Şirket Adı**: Mail içeriğinde `[ŞİRKET ADI]` otomatik değişir
- 📎 **CV Ekleme**: PDF formatında CV yükleme desteği
- 📊 **İstatistik Takibi**: Gönderilen mail sayısını otomatik kaydetme
- 🔐 **Güvenli Giriş**: Gmail uygulama şifresi ile güvenli bağlantı
- 💾 **Kalıcı Veriler**: Mail sayacı ve taslak kalıcı olarak saklanır

## 🚀 Kurulum

### Gereksinimler

- Python 3.x
- Gmail hesabı
- Gmail uygulama şifresi

### Adımlar

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/KULLANICI_ADINIZ/staj-basvuru.git
cd staj-basvuru
```

2. **Gerekli paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

3. **Uygulamayı çalıştırın:**
```bash
python app.py
```

4. **Tarayıcınızda açın:**
```
http://127.0.0.1:5000
```

## 🔑 Gmail Uygulama Şifresi Nasıl Alınır?

1. **Google Hesap Güvenliği** sayfasına gidin
   - https://myaccount.google.com/security

2. **2 Adımlı Doğrulama'yı** etkinleştirin

3. **Uygulama şifreleri** oluşturun
   - https://myaccount.google.com/apppasswords
   - "Mail" seçin
   - "Windows Bilgisayar" seçin
   - Oluşturulan 16 haneli şifreyi kopyalayın

4. **Web arayüzünde kullanın**
   - Gmail adresinizi girin
   - 16 haneli şifreyi yapıştırın

## 📖 Kullanım

### 1. Giriş Yapın
- Gmail adresinizi girin
- Uygulama şifrenizi girin
- "Devam Et" butonuna tıklayın

### 2. Mail Taslağını Hazırlayın
- Sol panelden mail içeriğini düzenleyin
- `[ŞİRKET ADI]` ifadesini kullanın (otomatik değişecek)
- Sağ panelde önizlemeyi görün

### 3. CV Yükleyin
- "CV Yükle (PDF)" butonuna tıklayın
- PDF dosyanızı seçin

### 4. Mail Gönderin
- Şirket adını yazın
- Alıcı mail adresini girin
- "Mail Gönder" butonuna tıklayın

### 5. İstatistikleri Takip Edin
- Gönderilen mail sayısı otomatik güncellenir
- Her açılışta önceki sayı korunur

## 📁 Proje Yapısı

```
staj-basvuru/
├── app.py                 # Ana uygulama
├── templates/
│   └── index.html        # Web arayüzü
├── mail-taslağı.md       # Mail taslağı
├── stats.json            # İstatistikler
├── uploaded_cv.pdf       # Yüklenen CV (otomatik)
├── requirements.txt      # Python bağımlılıkları
├── README.md            # Bu dosya
└── .gitignore           # Git ignore ayarları
```

## ⚙️ Teknik Detaylar

### Backend
- **Framework**: Flask 2.3.0
- **Mail**: Python smtplib (Gmail SMTP)
- **Dosya İşleme**: base64, json

### Frontend
- **HTML5 + CSS3**
- **Tailwind CSS** (CDN)
- **Vanilla JavaScript**
- **Fetch API**

## 🛡️ Güvenlik

- Gmail uygulama şifresi kullanılır (normal şifre değil)
- Şifreler session'da saklanır
- CV dosyaları local'de tutulur
- Rate limiting yok (dikkatli kullanın)

## ⚠️ Önemli Notlar

1. **Gmail Limitleri**
   - Gmail günlük ~500 mail limiti vardır
   - Çok hızlı göndermekten kaçının

2. **Spam Koruması**
   - İlk maillerde spam klasörüne düşebilir
   - Test maillerini kendinize gönderin

3. **CV Dosyası**
   - Sadece PDF formatı desteklenir
   - Her yüklemede üzerine yazılır

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👤 Yazar

**Ahmet Koç**

- 🌐 Website: [kocengineer.com](https://kocengineer.com)
- 💼 LinkedIn: [Ahmet Koç](https://www.linkedin.com/in/ahmet-ko%C3%A7-9a089a25a/)
- 🐙 GitHub: [@ahmetkc58](https://github.com/ahmetkc58)
- 📧 Email: ahmet58koc3o@gmail.com

## 🙏 Teşekkürler

Bu proje staj başvuru sürecini kolaylaştırmak için geliştirilmiştir. 

---

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!

## 📞 Destek

Sorun yaşarsanız veya öneriniz varsa:
- Issue açın
- Pull Request gönderin
- Email atın: ahmet58koc3o@gmail.com

---

**Not**: Bu uygulama eğitim amaçlıdır. Spam göndermek için kullanmayın!
