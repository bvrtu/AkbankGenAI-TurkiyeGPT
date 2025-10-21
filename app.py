"""
Türkiye Tourism Chatbot - Flask Web Application
RAG tabanlı Türkiye turizm chatbot'u için web arayüzü

Author: Akbank GenAI Bootcamp Project
"""

from flask import Flask, render_template, request, jsonify, session
from src.rag_pipeline import TurkiyeTourismRAG
import os
from datetime import datetime
import secrets
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Flask uygulamasını oluştur
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Global RAG instance
rag_instance = None


def initialize_rag():
    """RAG pipeline'ı başlatır"""
    global rag_instance
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("⚠️  UYARI: GEMINI_API_KEY environment variable tanımlanmamış!")
        print("   Lütfen .env dosyasını kontrol edin veya API key'i tanımlayın.")
        return False
    
    try:
        rag_instance = TurkiyeTourismRAG(api_key=api_key)
        print("✓ RAG Pipeline başarıyla başlatıldı!")
        return True
    except Exception as e:
        print(f"✗ RAG Pipeline başlatma hatası: {str(e)}")
        return False


@app.route('/')
def index():
    """Ana sayfa"""
    # Session'da chat history yoksa oluştur
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    return render_template('index.html')


@app.route('/chat')
def chat():
    """Chat sayfası"""
    # Session'da chat history yoksa oluştur
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    return render_template('chat.html')


@app.route('/api/chat', methods=['POST'])
def api_chat():
    """Chat API endpoint"""
    global rag_instance
    
    # RAG instance kontrolü
    if rag_instance is None:
        return jsonify({
            'success': False,
            'error': 'RAG sistemi başlatılamadı. Lütfen GEMINI_API_KEY kontrol edin.'
        }), 500
    
    try:
        # Kullanıcı mesajını al
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Lütfen bir mesaj girin.'
            }), 400
        
        # Chat history'yi al
        if 'chat_history' not in session:
            session['chat_history'] = []
        
        # Önceki kaynaklardan başlıkları çıkar (tekrar göstermemek için)
        previous_titles = set()
        for msg in session['chat_history']:
            if 'sources' in msg:
                for source in msg['sources']:
                    previous_titles.add(source.get('baslik', ''))
        
        # RAG pipeline ile yanıt üret (10 sonuç getir şehir sorularında)
        n_results = 12 if any(word in user_message.lower() for word in ['gezebilirim', 'nereleri', 'başka', 'daha', 'diğer', 'antik kentler', 'gezilecek']) else 8
        result = rag_instance.query(user_message, n_results=n_results, exclude_titles=list(previous_titles))
        
        # Chat history'ye ekle
        session['chat_history'].append({
            'user': user_message,
            'bot': result['response'],
            'sources': result['sources'],
            'timestamp': datetime.now().strftime('%H:%M')
        })
        
        # Session'ı güncelle
        session.modified = True
        
        return jsonify({
            'success': True,
            'response': result['response'],
            'sources': result['sources'],
            'timestamp': datetime.now().strftime('%H:%M')
        })
        
    except Exception as e:
        print(f"✗ Chat hatası: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Bir hata oluştu: {str(e)}'
        }), 500


@app.route('/api/clear', methods=['POST'])
def api_clear():
    """Chat geçmişini temizle"""
    session['chat_history'] = []
    session.modified = True
    return jsonify({
        'success': True,
        'message': 'Sohbet geçmişi temizlendi.'
    })


@app.route('/api/history', methods=['GET'])
def api_history():
    """Chat geçmişini getir"""
    history = session.get('chat_history', [])
    return jsonify({
        'success': True,
        'history': history
    })


@app.route('/about')
def about():
    """Hakkında sayfası"""
    return render_template('about.html')


@app.errorhandler(404)
def not_found(e):
    """404 hatası"""
    return """
    <!DOCTYPE html>
    <html><head><title>404 - Sayfa Bulunamadı</title>
    <style>body{font-family:Arial;text-align:center;padding:50px;}h1{color:#E30A17;}</style>
    </head><body><h1>404</h1><p>Aradığınız sayfa bulunamadı.</p>
    <a href="/">Ana Sayfaya Dön</a></body></html>
    """, 404


@app.errorhandler(500)
def server_error(e):
    """500 hatası"""
    return """
    <!DOCTYPE html>
    <html><head><title>500 - Sunucu Hatası</title>
    <style>body{font-family:Arial;text-align:center;padding:50px;}h1{color:#E30A17;}</style>
    </head><body><h1>500</h1><p>Bir hata oluştu.</p>
    <a href="/">Ana Sayfaya Dön</a></body></html>
    """, 500


if __name__ == '__main__':
    print("\n" + "="*80)
    print("TÜRKİYE TOURISM CHATBOT - RAG Tabanlı Turizm Asistanı")
    print("="*80 + "\n")
    
    # RAG pipeline'ı başlat
    if initialize_rag():
        print("\n🚀 Uygulama başlatılıyor...")
        print("📍 URL: http://localhost:5000")
        print("💡 Çıkmak için Ctrl+C\n")
        
        # Flask uygulamasını başlat
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True
        )
    else:
        print("\n✗ Uygulama başlatılamadı!")
        print("  Lütfen GEMINI_API_KEY environment variable'ını tanımlayın.")
        print("\n  Örnek:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        print("  python app.py\n")

