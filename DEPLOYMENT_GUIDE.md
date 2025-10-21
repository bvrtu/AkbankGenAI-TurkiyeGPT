# 🚀 TürkiyeGPT - Deployment Rehberi

Bu rehber, TürkiyeGPT projesini çeşitli platformlara deploy etmek için adım adım talimatlar içerir.

---

## 📋 Deployment Öncesi Kontrol Listesi

- [x] `requirements.txt` güncel
- [x] `.env` dosyası gitignore'da
- [x] `Procfile` hazır (Heroku için)
- [x] `runtime.txt` hazır (Python versiyonu)
- [x] GEMINI_API_KEY environment variable tanımlanmış

---

## 🌐 Render.com ile Deployment

### Adım 1: Render Hesabı Oluşturma

1. [Render.com](https://render.com) adresine gidin
2. GitHub hesabınızla giriş yapın
3. "New Web Service" butonuna tıklayın

### Adım 2: Repository Bağlama

1. GitHub repository'nizi seçin
2. Şu ayarları yapın:
   - **Name**: `turkiyegpt` (veya dilediğiniz isim)
   - **Region**: Europe (Frankfurt) - En yakın region
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### Adım 3: Environment Variables

Environment Variables bölümüne şu değeri ekleyin:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### Adım 4: Deploy

1. "Create Web Service" butonuna tıklayın
2. Deploy işlemi başlayacak (5-10 dakika sürebilir)
3. Deploy tamamlandığında URL'niz hazır olacak: `https://turkiyegpt.onrender.com`

### Render Özellikleri

✅ Ücretsiz tier ile 750 saat/ay
✅ Otomatik SSL sertifikası
✅ Git push ile otomatik deploy
⚠️ Free tier'da 15 dakika inaktiviteden sonra uyku moduna geçer

---

## 🔥 Heroku ile Deployment

### Adım 1: Heroku CLI Kurulumu

```bash
# macOS
brew tap heroku/brew && brew install heroku

# Ubuntu
curl https://cli-assets.heroku.com/install.sh | sh

# Windows
# https://devcenter.heroku.com/articles/heroku-cli adresinden indirin
```

### Adım 2: Heroku'ya Login

```bash
heroku login
```

### Adım 3: Heroku App Oluşturma

```bash
# Heroku app oluştur
heroku create turkiyegpt

# veya özel isimle
heroku create my-turkiye-tourism-bot
```

### Adım 4: Environment Variables Ayarlama

```bash
heroku config:set GEMINI_API_KEY=your_api_key_here
```

### Adım 5: Deploy

```bash
# Git repository'sine ekle
git add .
git commit -m "Initial deployment"

# Heroku'ya push et
git push heroku main
```

### Adım 6: App'i Aç

```bash
heroku open
```

### Heroku Komutları

```bash
# Logları görüntüle
heroku logs --tail

# Dyno'ları kontrol et
heroku ps

# Environment variables'ı görüntüle
heroku config

# Shell aç
heroku run bash
```

---

## 🐳 Docker ile Deployment

### Dockerfile Oluşturma

```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıkları
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Port
EXPOSE 5000

# Gunicorn ile çalıştır
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "app:app"]
```

### Docker Komutları

```bash
# Image oluştur
docker build -t turkiyegpt .

# Container çalıştır
docker run -d -p 5000:5000 \
  -e GEMINI_API_KEY=your_api_key_here \
  --name turkiyegpt-app \
  turkiyegpt

# Logları görüntüle
docker logs -f turkiyegpt-app

# Container'ı durdur
docker stop turkiyegpt-app

# Container'ı sil
docker rm turkiyegpt-app
```

### Docker Compose (docker-compose.yml)

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    restart: unless-stopped
```

Kullanım:
```bash
docker-compose up -d
docker-compose logs -f
docker-compose down
```

---

## ☁️ AWS (Amazon Web Services) Deployment

### EC2 ile Deployment

1. **EC2 Instance Oluşturma**:
   - Ubuntu Server 22.04 LTS
   - t2.micro (Free tier)
   - Security Group: Port 80, 443, 22 açık

2. **Instance'a Bağlanma**:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Gerekli Paketleri Kurma**:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx -y
   ```

4. **Projeyi Klonlama**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AkbankGenAI-TurkiyeGPT.git
   cd AkbankGenAI-TurkiyeGPT
   ```

5. **Virtual Environment Kurulumu**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Environment Variables**:
   ```bash
   nano .env
   # GEMINI_API_KEY=your_key_here ekleyin
   ```

7. **Gunicorn ile Çalıştırma**:
   ```bash
   gunicorn --bind 0.0.0.0:5000 app:app
   ```

8. **Nginx Reverse Proxy** (Opsiyonel):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

---

## 🔧 Production Best Practices

### 1. Gunicorn Konfigürasyonu

```bash
gunicorn --bind 0.0.0.0:5000 \
  --workers 4 \
  --threads 2 \
  --timeout 120 \
  --access-logfile logs/access.log \
  --error-logfile logs/error.log \
  app:app
```

### 2. Environment Variables

Asla API key'leri kodda saklamayın:

```python
# ❌ Yanlış
GEMINI_API_KEY = "AIzaSy..."

# ✅ Doğru
import os
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
```

### 3. HTTPS Kullanımı

Production'da mutlaka HTTPS kullanın:
- Let's Encrypt ile ücretsiz SSL sertifikası
- Cloudflare kullanarak ücretsiz SSL

### 4. Rate Limiting

API abuse'i önlemek için rate limiting ekleyin:

```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/chat', methods=['POST'])
@limiter.limit("20 per minute")
def api_chat():
    # ...
```

### 5. Logging

Production'da düzgün logging yapın:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### 6. Monitoring

- **Uptime Monitoring**: UptimeRobot, Pingdom
- **Error Tracking**: Sentry
- **Performance**: New Relic, Datadog

---

## 🐛 Troubleshooting

### Sorun: Port zaten kullanımda

```bash
# Port kullanan process'i bul
lsof -i :5000

# Process'i sonlandır
kill -9 <PID>
```

### Sorun: ModuleNotFoundError

```bash
# Virtual environment'ı aktifleştirin
source venv/bin/activate

# Bağımlılıkları yeniden yükleyin
pip install -r requirements.txt
```

### Sorun: GEMINI_API_KEY tanımlı değil

```bash
# Environment variable'ı kontrol edin
echo $GEMINI_API_KEY

# Tanımlayın
export GEMINI_API_KEY='your_key_here'
```

### Sorun: ChromaDB hatası

```bash
# ChromaDB veritabanını sıfırlayın
rm -rf data/chroma_db/

# Uygulamayı yeniden başlatın
python app.py
```

---

## 📞 Destek

Deployment sırasında sorun yaşarsanız:

1. GitHub Issues açın
2. Logları paylaşın
3. Hata mesajını tam olarak belirtin

---

**Made with ❤️ for Akbank GenAI Bootcamp**

