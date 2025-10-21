#!/bin/bash

# TürkiyeGPT - Kurulum Script'i
# Bu script projeyi yerel ortamda çalıştırmak için gerekli adımları otomatik yapar

echo "🇹🇷 TürkiyeGPT Kurulum Script'i"
echo "================================"
echo ""

# Renk kodları
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Python versiyonu kontrolü
echo "📌 Python versiyonu kontrol ediliyor..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.11"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then 
    echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION bulundu"
else
    echo -e "${RED}✗${NC} Python 3.11+ gerekli. Mevcut versiyon: $PYTHON_VERSION"
    exit 1
fi

# Virtual environment kontrolü
echo ""
echo "📌 Virtual environment oluşturuluyor..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} Virtual environment oluşturuldu"
else
    echo -e "${YELLOW}⚠${NC} Virtual environment zaten mevcut"
fi

# Virtual environment aktifleştirme
echo ""
echo "📌 Virtual environment aktifleştiriliyor..."
source venv/bin/activate
echo -e "${GREEN}✓${NC} Virtual environment aktif"

# Bağımlılıkları yükleme
echo ""
echo "📌 Bağımlılıklar yükleniyor..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Tüm bağımlılıklar yüklendi"
else
    echo -e "${RED}✗${NC} Bağımlılık yükleme hatası"
    exit 1
fi

# .env dosyası kontrolü
echo ""
echo "📌 Environment variables kontrol ediliyor..."
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠${NC} .env dosyası bulunamadı"
    echo "📝 env_example.txt dosyasından .env oluşturuluyor..."
    cp env_example.txt .env
    echo -e "${YELLOW}⚠${NC} Lütfen .env dosyasını düzenleyip GEMINI_API_KEY değerini ekleyin!"
    echo ""
    echo "API Key almak için: https://ai.google.dev/"
    exit 1
else
    # API key kontrolü
    if grep -q "your_gemini_api_key_here" .env; then
        echo -e "${YELLOW}⚠${NC} .env dosyasında geçerli bir API key yok!"
        echo "Lütfen .env dosyasını düzenleyip GEMINI_API_KEY değerini ekleyin"
        exit 1
    else
        echo -e "${GREEN}✓${NC} .env dosyası hazır"
    fi
fi

# Veri seti kontrolü
echo ""
echo "📌 Veri seti kontrol ediliyor..."
if [ -f "data/turkiye_turizm_verileri.json" ]; then
    RECORD_COUNT=$(python3 -c "import json; print(len(json.load(open('data/turkiye_turizm_verileri.json'))))")
    echo -e "${GREEN}✓${NC} Veri seti hazır ($RECORD_COUNT kayıt)"
else
    echo -e "${RED}✗${NC} Veri seti bulunamadı!"
    exit 1
fi

# Başarı mesajı
echo ""
echo "================================"
echo -e "${GREEN}✅ Kurulum başarıyla tamamlandı!${NC}"
echo ""
echo "🚀 Uygulamayı başlatmak için:"
echo "   source venv/bin/activate"
echo "   python app.py"
echo ""
echo "📍 Uygulama şu adreste çalışacak: http://localhost:5000"
echo ""

