#!/bin/bash

echo "🚀 TürkiyeGPT Codespaces Setup"
echo "================================"

# Python bağımlılıklarını yükle
echo "📦 Bağımlılıklar yükleniyor..."
pip install -r requirements.txt

# Environment variable kontrolü
if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  UYARI: GEMINI_API_KEY environment variable tanımlanmamış!"
    echo "Lütfen Codespaces'te environment variable'ı ayarlayın:"
    echo "1. Codespaces'te Settings → Secrets and variables → Codespaces"
    echo "2. New repository variable ekleyin:"
    echo "   Name: GEMINI_API_KEY"
    echo "   Value: your_api_key_here"
    echo ""
    echo "Veya terminal'de:"
    echo "export GEMINI_API_KEY='your_api_key_here'"
    echo ""
fi

# RAG pipeline'ı test et
echo "🧪 RAG Pipeline test ediliyor..."
python -c "
try:
    from src.rag_pipeline import TurkiyeTourismRAG
    print('✅ RAG Pipeline import başarılı')
except Exception as e:
    print(f'❌ RAG Pipeline import hatası: {e}')
"

echo ""
echo "🎉 Setup tamamlandı!"
echo "🚀 Uygulamayı başlatmak için:"
echo "   python app.py"
echo ""
echo "🌐 Public URL için port 5000'i forward edin"
echo "   Codespaces'te Ports sekmesinde 'Public' yapın"
