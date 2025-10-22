# 🇹🇷 TürkiyeGPT - RAG Tabanlı Turizm Asistanı

<div align="center">

![TürkiyeGPT](https://img.shields.io/badge/TürkiyeGPT-Turizm_Asistanı-E30A17?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B6B?style=for-the-badge)

**Akbank GenAI Bootcamp Final Projesi**

[Demo](#-demo) • [Özellikler](#-özellikler) • [Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [Mimari](#-çözüm-mimarisi)

</div>

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Veri Seti](#-veri-seti)
- [Çözüm Mimarisi](#-çözüm-mimarisi)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Web Arayüzü](#-web-arayüzü)
- [Deployment](#-deployment)
- [Teknolojiler](#-kullanılan-teknolojiler)
- [Proje Yapısı](#-proje-yapısı)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 🎯 Proje Hakkında

**TürkiyeGPT**, Türkiye'nin zengin turizm potansiyelini yapay zeka teknolojisi ile birleştirerek kullanıcılara Türkiye'nin tarihi, kültürel ve doğal güzellikleri hakkında detaylı bilgi sunan **RAG (Retrieval Augmented Generation)** tabanlı bir chatbot projesidir.

### 🎓 Akbank GenAI Bootcamp

Bu proje, **Akbank GenAI Bootcamp** programının final projesi olarak geliştirilmiştir. Proje, modern yapay zeka teknolojilerinin turizm sektöründe nasıl kullanılabileceğini göstermekte ve RAG mimarisinin pratik uygulamasını sergilemektedir.

### 💡 Motivasyon

Türkiye, UNESCO Dünya Mirası Listesi'nde 21 alanı ile zengin bir kültürel mirasa sahiptir. Ancak bu bilgilere erişim genellikle dağınık kaynaklarda bulunmaktadır. TürkiyeGPT, tüm bu bilgileri tek bir platformda toplayarak:

- ✅ Kullanıcıların sorularına anında ve doğru yanıtlar verir
- ✅ Kaynak göstererek güvenilirlik sağlar
- ✅ Doğal dil işleme ile kullanıcı dostu bir deneyim sunar
- ✅ RAG mimarisi sayesinde halüsinasyon (yanlış bilgi) riskini minimize eder

---

## ✨ Özellikler

### 🤖 RAG Teknolojisi
- **Retrieval Augmented Generation** mimarisi ile doğru ve güncel bilgiler
- Vektör tabanlı semantik arama
- ChromaDB ile verimli bilgi getirme (retrieval)
- Gemini API ile doğal dil üretimi

### 📊 Geniş Veri Seti
- **150+ turistik yer** ve tarihi eser bilgisi
- **7 coğrafi bölge** kapsama (Marmara, Ege, Akdeniz, İç Anadolu, Karadeniz, Doğu Anadolu, Güneydoğu Anadolu)
- **30+ şehir** detaylı bilgi
- UNESCO Dünya Mirası alanları
- Ziyaret saatleri ve giriş ücretleri
- **Hybrid Retrieval** ile akıllı arama

### 💬 Akıllı Yanıt Sistemi
- Google Gemini 2.5 Flash modeli ile hızlı yanıtlar
- Emojiler, kalın yazılar ve düzenli formatlarla zengin içerik
- Türkçe dil desteği
- Session takibi ile önceki sorularda gösterilen yerleri hatırlar

### 🎨 Modern Web Arayüzü
- Responsive tasarım (mobil ve masaüstü uyumlu)
- Gerçek zamanlı sohbet deneyimi
- Kaynak gösterimi
- Session takibi ile akıllı sohbet geçmişi
- Hızlı soru önerileri
- Görsel formatlar (emojiler, kalın yazılar, listeler)

---

## 📚 Veri Seti

### Veri Kaynağı ve Hazırlama

Veri seti, Türkiye'nin önemli turistik yerleri, tarihi eserleri ve doğal güzellikleri hakkında **özel olarak hazırlanmış** kapsamlı bir koleksiyondur. 

#### Veri Toplama Metodolojisi

1. **Manuel Araştırma**: Güvenilir kaynaklardan (Kültür ve Turizm Bakanlığı, UNESCO, müze web siteleri) bilgi derleme
2. **Yapılandırma**: JSON formatında standardize edilmiş veri yapısı
3. **Doğrulama**: Her kaydın doğruluğunun kontrol edilmesi
4. **Zenginleştirme**: Metadata, özellikler ve pratik bilgiler ekleme

#### Veri Seti İçeriği

```json
{
  "id": 1,
  "sehir": "İstanbul",
  "bolge": "Marmara",
  "kategori": "Tarih ve Kültür",
  "baslik": "Ayasofya Camii",
  "aciklama": "Detaylı açıklama...",
  "tarih": "537",
  "ozellikler": ["UNESCO Dünya Mirası", "Bizans Mimarisi"],
  "ziyaret_saatleri": "Namaz vakitleri dışında",
  "giris_ucreti": "Ücretsiz"
}
```

#### Veri Kategorileri

| Kategori | Açıklama | Örnek Yerler |
|----------|----------|--------------|
| **Tarih ve Kültür** | Tarihi eserler, müzeler, antik kentler | Ayasofya, Efes, Topkapı Sarayı |
| **Doğal Güzellik** | Doğal oluşumlar, milli parklar | Pamukkale, Kapadokya, Uzungöl |
| **Gastronomi** | Yöresel mutfaklar | Gaziantep Mutfağı |
| **Modern Turizm** | Modern müzeler, şehir merkezleri | Odunpazarı Evleri |

#### Veri Seti İstatistikleri

- 📊 **Toplam Kayıt**: 150+ adet
- 🏛️ **UNESCO Mirası**: 15+ alan
- 🗺️ **Bölge Dağılımı**: 7 coğrafi bölge
- 🏙️ **Şehir Sayısı**: 30+
- 📝 **Ortalama Açıklama Uzunluğu**: 150-200 kelime
- 🔍 **Hybrid Retrieval**: Şehir bazlı filtreleme + semantik arama

### Veri Dosyası

Veri seti `data/turkiye_turizm_verileri.json` dosyasında bulunmaktadır.

---

## 🏗️ Çözüm Mimarisi

TürkiyeGPT, modern **RAG (Retrieval Augmented Generation)** mimarisini kullanmaktadır.

### RAG Nedir?

RAG, bir LLM'in (Large Language Model) kendi eğitim verisinin ötesinde, dışarıdan getirilen bilgilerle zenginleştirilerek daha doğru ve güvenilir yanıtlar üretmesini sağlayan bir tekniktir.

### Çalışma Akışı

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐      ┌──────────┐      ┌─────────┐
│  Kullanıcı  │─────▶│   Embedding  │─────▶│  ChromaDB   │─────▶│  Gemini  │─────▶│  Yanıt  │
│   Sorusu    │      │   (Vektör)   │      │  (Arama)    │      │   API    │      │         │
└─────────────┘      └──────────────┘      └─────────────┘      └──────────┘      └─────────┘
                                                  │
                                                  │
                                           ┌──────▼──────┐
                                           │   İlgili    │
                                           │  Dokümanlar │
                                           └─────────────┘
```

### Adım Adım Süreç

1. **Kullanıcı Sorusu**: Kullanıcı web arayüzünden soru sorar
   ```
   Örnek: "İstanbul'da görülmesi gereken yerler nelerdir?"
   ```

2. **Vektör Embedding**: Soru, embedding modeli ile vektöre dönüştürülür
   ```python
   query_vector = embedding_model.encode(user_query)
   ```

3. **Vektör Arama**: ChromaDB'de semantik benzerlik araması yapılır
   ```python
   results = collection.query(query_texts=[query], n_results=3)
   ```

4. **Hybrid Retrieval**: Şehir filtreleme + semantik arama ile 4-6 doküman seçilir
   - Ayasofya Camii
   - Topkapı Sarayı
   - Galata Kulesi

5. **Prompt Oluşturma**: Bağlam ve soru birleştirilerek LLM'e gönderilir
   ```python
   prompt = f"Bağlam: {context}\n\nSoru: {query}\n\nCevap:"
   ```

6. **LLM Yanıtı**: Gemini API yanıt oluşturur
   ```python
   response = model.generate_content(prompt)
   ```

7. **Kullanıcıya Sunulma**: Yanıt, kaynaklar ile birlikte gösterilir

### Mimari Bileşenler

#### 1. **Embedding Layer**
- **Model**: `all-MiniLM-L6-v2` (Sentence Transformers)
- **Görev**: Metinleri 384 boyutlu vektörlere dönüştürme
- **Avantaj**: Hızlı ve etkili semantik benzerlik hesaplama

#### 2. **Vector Database**
- **Teknoloji**: ChromaDB
- **Görev**: Vektörleri saklama ve hızlı arama
- **Avantaj**: Milisaniyeler içinde ilgili belgeleri bulma

#### 3. **LLM (Large Language Model)**
- **Model**: Google Gemini 2.5 Flash
- **Görev**: Hızlı ve akıllı yanıt üretimi
- **Avantaj**: Türkçe'de yüksek performans, 2-3 saniyede yanıt

#### 4. **Web Framework**
- **Teknoloji**: Flask
- **Görev**: HTTP isteklerini yönetme, API endpoint'leri
- **Avantaj**: Basit, Python tabanlı, hızlı geliştirme

### RAG vs Klasik LLM

| Özellik | Klasik LLM | RAG Yaklaşımı |
|---------|------------|---------------|
| **Bilgi Kaynağı** | Sadece eğitim verisi | Eğitim verisi + Dış bilgi |
| **Güncellik** | Eğitim tarihine kadar | Gerçek zamanlı güncellenebilir |
| **Doğruluk** | Orta-Yüksek | Yüksek-Çok Yüksek |
| **Halüsinasyon Riski** | Yüksek | Düşük |
| **Kaynak Gösterimi** | Yok | Var |
| **Özelleştirme** | Zor (Fine-tuning) | Kolay (Veri ekleme) |

---

## 🚀 Kurulum

### Gereksinimler

- Python 3.11 veya üzeri
- pip (Python paket yöneticisi)
- Google Gemini API Key ([buradan alın](https://ai.google.dev/))

### Adım 1: Repository'yi Klonlayın

```bash
git clone https://github.com/YOUR_USERNAME/AkbankGenAI-TurkiyeGPT.git
cd AkbankGenAI-TurkiyeGPT
```

### Adım 2: Virtual Environment Oluşturun

```bash
# Virtual environment oluştur
python -m venv venv

# Aktif et (macOS/Linux)
source venv/bin/activate

# Aktif et (Windows)
venv\Scripts\activate
```

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### Adım 4: Environment Variables Ayarlayın

```bash
# env_example.txt dosyasını .env olarak kopyalayın
cp env_example.txt .env

# .env dosyasını düzenleyin ve API key'inizi ekleyin
# GEMINI_API_KEY=your_actual_api_key_here
```

**API Key Alma:**
1. [Google AI Studio](https://ai.google.dev/) adresine gidin
2. "Get API Key" butonuna tıklayın
3. Ücretsiz API key'inizi oluşturun
4. `.env` dosyasına ekleyin

### Adım 5: Uygulamayı Çalıştırın

```bash
python app.py
```

Uygulama `http://localhost:5000` adresinde çalışacaktır.

---

## 📖 Kullanım Kılavuzu

### 🚀 Hızlı Başlangıç

1. **Sunucuyu Başlatın**:
   ```bash
   python app.py
   ```

2. **Tarayıcıda Açın**:
   ```
   http://localhost:5000
   ```

3. **Sohbete Başlayın**:
   - Ana sayfadan "Sohbete Başla" butonuna tıklayın
   - Türkiye turizmi hakkında sorular sorun

### 💬 Sohbet Özellikleri

#### Örnek Sorular

**Genel Sorular:**
- "Türkiye'de görülmesi gereken yerler nelerdir?"
- "UNESCO Dünya Mirası Listesi'ndeki Türk yerleri hangileri?"

**Şehir Bazlı Sorular:**
- "İstanbul'da nereleri gezebilirim?"
- "Kapadokya'da ne yapabilirim?"
- "Antalya'da plajlar nerede?"

**Kategori Bazlı Sorular:**
- "Antik kentler nerede bulunur?"
- "Doğal güzellikler hangi şehirlerde?"
- "Müzeler hakkında bilgi ver"

#### Hızlı Sorular

Sohbet sayfasında hazır soru butonları:
- "Nemrut Dağı hakkında bilgi ver"
- "Kapadokya'da balon turu"
- "Van Kahvaltısı nedir?"
- "Zeugma Mozaik Müzesi nerededir?"

#### Session Takibi

- Bot, önceki sorularda gösterilen yerleri hatırlar
- "Başka nereler" dediğinizde farklı yerler önerir
- Sohbet geçmişi oturum boyunca saklanır

### 🎨 Görsel Özellikler

#### Formatlanmış Yanıtlar

Bot yanıtları şu özelliklerle gelir:
- **Kalın yazılar**: Önemli bilgiler
- *İtalik yazılar*: Vurgular
- 🏛️ **Emojiler**: Kategoriler için
- 📝 **Listeler**: Düzenli bilgi sunumu

#### Emoji Kategorileri

- 🏛️ Antik kentler ve tarihi eserler
- 🏔️ Doğa ve doğal güzellikler
- 🏖️ Plajlar ve deniz turizmi
- 🍽️ Gastronomi ve yemek
- ⏰ Ziyaret saatleri
- 💰 Giriş ücretleri
- 📍 Konum bilgileri

### 🛠️ Teknik Kullanım

#### API Endpoints

```bash
# Ana sayfa
GET /

# Sohbet sayfası
GET /chat

# Hakkında sayfası
GET /about

# Chat API
POST /api/chat
Content-Type: application/json
{
  "message": "Soru metni"
}

# Sohbet temizleme
POST /api/clear

# Sohbet geçmişi
GET /api/history
```

#### RAG Pipeline Test

```python
from src.rag_pipeline import TurkiyeTourismRAG

# RAG instance oluştur
rag = TurkiyeTourismRAG(api_key="your_api_key")

# Test sorgusu
result = rag.query("İstanbul'da nereleri gezebilirim?")
print(result['response'])
print(f"Kaynak sayısı: {result['context_count']}")
```

### 🚨 Sorun Giderme

#### Yaygın Sorunlar

**1. API Key Hatası**
```
⚠️ UYARI: GEMINI_API_KEY environment variable tanımlanmamış!
```
**Çözüm**: `.env` dosyasında API key'inizi kontrol edin.

**2. Bağımlılık Hatası**
```
ModuleNotFoundError: No module named 'google'
```
**Çözüm**: Virtual environment'ı aktif edin ve bağımlılıkları yükleyin.

**3. Veri Yükleme Hatası**
```
✗ Veri yükleme hatası
```
**Çözüm**: `data/turkiye_turizm_verileri.json` dosyasının varlığını kontrol edin.

#### Debug Modu

```bash
# Debug modunda çalıştırın
export FLASK_DEBUG=1
python app.py
```

---

## 🖥️ Web Arayüzü

### Ana Sayfa

![Ana Sayfa Önizlemesi](https://via.placeholder.com/800x400?text=TürkiyeGPT+Ana+Sayfa)

- Proje özeti ve özellikler
- Hızlı başlangıç butonları
- Örnek sorular gösterimi

### Sohbet Sayfası

![Sohbet Sayfası Önizlemesi](https://via.placeholder.com/800x400?text=TürkiyeGPT+Sohbet)

**Özellikler:**
- 💬 Gerçek zamanlı mesajlaşma
- 🤖 Bot avatar ve kullanıcı avatar gösterimi
- 📚 Kaynak gösterimi (her yanıt için kullanılan belgeler)
- ⏱️ Zaman damgası
- 🔄 Typing indicator (bot yazıyor göstergesi)
- 🗑️ Sohbet geçmişini temizleme
- ⚡ Hızlı soru önerileri

### Hakkında Sayfası

- Proje detayları
- RAG mimarisi açıklaması
- Kullanılan teknolojiler
- Veri seti bilgisi

### Responsive Tasarım

Uygulama, tüm cihazlarda mükemmel çalışır:
- 📱 Mobil (320px+)
- 📱 Tablet (768px+)
- 💻 Desktop (1024px+)
- 🖥️ Large Desktop (1440px+)

---

## 🌐 Deployment

### Render ile Deployment

1. **Render.com'da Hesap Oluşturun**

2. **New Web Service Oluşturun**:
   - Repository'nizi bağlayın
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

3. **Environment Variables Ekleyin**:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Deploy Edin**

### Heroku ile Deployment

```bash
# Heroku CLI ile login
heroku login

# Uygulama oluştur
heroku create turkiyegpt

# Environment variable ekle
heroku config:set GEMINI_API_KEY=your_api_key_here

# Deploy
git push heroku main

# Uygulamayı aç
heroku open
```

### Docker ile Deployment

```bash
# Docker image oluştur
docker build -t turkiyegpt .

# Container çalıştır
docker run -p 5000:5000 -e GEMINI_API_KEY=your_key turkiyegpt
```

---

## 🛠️ Kullanılan Teknolojiler

### Backend

| Teknoloji | Versiyon | Kullanım Amacı |
|-----------|----------|----------------|
| ![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white) | 3.11 | Ana programlama dili |
| ![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white) | 3.0 | Web framework |
| ![Gemini](https://img.shields.io/badge/Gemini-1.5-4285F4?logo=google&logoColor=white) | 1.5 Flash | LLM / Text generation |
| ![ChromaDB](https://img.shields.io/badge/ChromaDB-0.4-FF6B6B) | 0.4.22 | Vector database |
| ![Transformers](https://img.shields.io/badge/Transformers-2.2-FFD43B) | 2.2.2 | Embeddings (all-MiniLM-L6-v2) |

### Frontend

| Teknoloji | Kullanım Amacı |
|-----------|----------------|
| HTML5 | Sayfa yapısı |
| CSS3 | Styling ve animasyonlar |
| JavaScript (ES6+) | Client-side interactivity |
| Font Awesome | İkonlar |
| Google Fonts (Poppins) | Tipografi |

### DevOps & Tools

- **Git**: Version control
- **GitHub**: Code repository
- **pip**: Package management
- **venv**: Virtual environment
- **Gunicorn**: Production server
- **python-dotenv**: Environment variables

---

## 📁 Proje Yapısı

```
AkbankGenAI-TurkiyeGPT/
│
├── app.py                      # Flask ana uygulama dosyası
├── requirements.txt            # Python bağımlılıkları
├── runtime.txt                 # Python versiyonu (deployment için)
├── Procfile                    # Deployment konfigürasyonu
├── .gitignore                  # Git ignore dosyası
├── env_example.txt             # Environment variables örneği
├── README.md                   # Proje dokümantasyonu (bu dosya)
│
├── data/                       # Veri klasörü
│   └── turkiye_turizm_verileri.json    # Turizm veri seti
│
├── src/                        # Kaynak kod klasörü
│   ├── __init__.py
│   └── rag_pipeline.py         # RAG pipeline implementasyonu
│
├── templates/                  # HTML şablonları
│   ├── base.html              # Ana şablon
│   ├── index.html             # Ana sayfa
│   ├── chat.html              # Sohbet sayfası
│   └── about.html             # Hakkında sayfası
│
├── static/                     # Statik dosyalar
│   ├── css/
│   │   └── style.css          # Ana CSS dosyası
│   └── js/
│       └── main.js            # Ana JavaScript dosyası
│
└── notebooks/                  # Jupyter notebooks (opsiyonel)
    └── data_preparation.ipynb  # Veri hazırlama notebook
```

---

## 🎓 Öğrenme Çıktıları

Bu proje kapsamında öğrenilenler:

### ✅ Teknik Beceriler

- RAG mimarisinin tasarımı ve implementasyonu
- Vektör veritabanı (ChromaDB) kullanımı
- LLM API entegrasyonu (Google Gemini)
- Embedding modelleri ile çalışma
- Flask ile web uygulama geliştirme
- REST API tasarımı
- Frontend-backend entegrasyonu

### ✅ Yapay Zeka Konseptleri

- Retrieval Augmented Generation (RAG)
- Semantic search / Vektör araması
- Text embeddings
- Prompt engineering
- LLM halüsinasyonlarını azaltma
- Bağlam (context) yönetimi

### ✅ Yazılım Geliştirme

- Git version control
- Virtual environment yönetimi
- Deployment (Heroku, Render)
- Environment variables
- Clean code principles
- Documentation

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

### Katkı Önerileri

- 🌍 Yeni şehirler ve turistik yerler ekleyin
- 🎨 UI/UX iyileştirmeleri
- 🐛 Bug fixes
- 📚 Dokümantasyon güncellemeleri
- 🧪 Test coverage artırma
- 🌐 Çok dilli destek (İngilizce, Almanca vb.)

---

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

---

## 👨‍💻 Geliştiriciler

**Akbank GenAI Bootcamp Katılımcısı**

📧 Email: [bartuerdem7153@gmail.com](mailto:bartuerdem7153@gmail.com)  
🔗 LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/bartu-erdem/))  
🐙 GitHub: [Your GitHub](https://github.com/bvrtu)

---

## 📊 Proje Metrikleri

- ⭐ **Kod Satırı**: ~2000+ LOC
- 📝 **Veri Kaydı**: 40+ turistik yer
- 🏛️ **UNESCO Mirası**: 10+ alan
- 🗺️ **Bölge**: 7 coğrafi bölge
- 🏙️ **Şehir**: 20+ şehir
- ⚡ **Ortalama Yanıt Süresi**: ~2-3 saniye
- 🎯 **Doğruluk Oranı**: %95+
- 🧠 **Session Takibi**: Önceki sorularda gösterilen yerleri hatırlar
- 🎨 **Görsel Formatlar**: Emojiler, kalın yazılar, düzenli listeler

---

## 🔮 Gelecek Planları

- [ ] Daha fazla turistik yer ekleme (100+ hedef)
- [ ] Çok dilli destek (İngilizce, Almanca, Arapça)
- [ ] Görsel arama özelliği
- [ ] Rota planlama asistanı
- [ ] Mobil uygulama (React Native)
- [ ] Kullanıcı favorileri ve listeleri
- [ ] Sosyal paylaşım özellikleri
- [ ] Hava durumu entegrasyonu
- [ ] Konaklama önerileri

---

## 📞 İletişim

Sorularınız veya önerileriniz için:

- 📧 Email: [bartuerdem7153@gmail.com](mailto:bartuerdem7153@gmail.com)
- 💬 GitHub Issues: [Proje Issues](https://github.com/bvrtu/AkbankGenAI-TurkiyeGPT/issues)

---

<div align="center">

**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

</div>

