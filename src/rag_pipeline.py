"""
RAG Pipeline for Türkiye Tourism Chatbot
Bu modül, Retrieval Augmented Generation (RAG) mimarisini kullanarak
Türkiye turizm bilgileri üzerinde soru-cevap işlemi yapar.

Kullanılan Teknolojiler:
- Gemini API: Text generation için
- ChromaDB: Vektör veritabanı olarak
- Google Generative AI Embeddings: Metin embedding için
"""

import os
import json
import google.generativeai as genai
from chromadb import Client, Settings
from chromadb.utils import embedding_functions
from typing import List, Dict, Any


class TurkiyeTourismRAG:
    """
    Türkiye Turizm RAG Pipeline Sınıfı
    
    Bu sınıf, turizm verilerini vektör veritabanına yükler,
    kullanıcı sorularına göre ilgili bilgileri getirir ve
    Gemini API ile doğal dil yanıtları üretir.
    """
    
    def __init__(self, api_key: str, data_path: str = "data/turkiye_turizm_verileri.json"):
        """
        RAG pipeline'ı başlatır
        
        Args:
            api_key: Google Gemini API anahtarı
            data_path: Turizm verilerinin bulunduğu JSON dosya yolu
        """
        self.api_key = api_key
        self.data_path = data_path
        
        # Gemini API'yi yapılandır
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # ChromaDB client'ı başlat
        self.chroma_client = Client(Settings(
            anonymized_telemetry=False,
            allow_reset=True
        ))
        
        # Google'ın embedding fonksiyonunu kullan
        # Not: Gemini embeddings için alternatif olarak sentence-transformers kullanabiliriz
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Collection oluştur veya al
        self.collection = None
        self.initialize_database()
    
    def initialize_database(self):
        """
        ChromaDB veritabanını başlatır ve verileri yükler
        """
        try:
            # Eğer collection varsa sil ve yeniden oluştur
            try:
                self.chroma_client.delete_collection("turkiye_turizm")
            except:
                pass
            
            # Yeni collection oluştur
            self.collection = self.chroma_client.create_collection(
                name="turkiye_turizm",
                embedding_function=self.embedding_function,
                metadata={"description": "Türkiye turizm bilgileri vektör veritabanı"}
            )
            
            # Verileri yükle
            self.load_data()
            print(f"✓ Veritabanı başarıyla oluşturuldu. Toplam {self.collection.count()} kayıt yüklendi.")
            
        except Exception as e:
            print(f"✗ Veritabanı başlatma hatası: {str(e)}")
            raise
    
    def load_data(self):
        """
        JSON dosyasından verileri okur ve ChromaDB'ye yükler
        """
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            documents = []
            metadatas = []
            ids = []
            
            for item in data:
                # Her veri kaydını birleştirilmiş metin olarak hazırla
                doc_text = f"""
                Şehir: {item['sehir']}
                Bölge: {item['bolge']}
                Kategori: {item['kategori']}
                Başlık: {item['baslik']}
                Açıklama: {item['aciklama']}
                Tarih: {item.get('tarih', 'Bilinmiyor')}
                Özellikler: {', '.join(item.get('ozellikler', []))}
                Ziyaret Saatleri: {item.get('ziyaret_saatleri', 'Bilgi yok')}
                Giriş Ücreti: {item.get('giris_ucreti', 'Bilgi yok')}
                """
                
                documents.append(doc_text)
                metadatas.append({
                    "sehir": item['sehir'],
                    "bolge": item['bolge'],
                    "kategori": item['kategori'],
                    "baslik": item['baslik']
                })
                ids.append(str(item['id']))
            
            # ChromaDB'ye toplu yükleme
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            
        except FileNotFoundError:
            print(f"✗ Veri dosyası bulunamadı: {self.data_path}")
            raise
        except json.JSONDecodeError:
            print(f"✗ JSON dosyası okunamadı: {self.data_path}")
            raise
        except Exception as e:
            print(f"✗ Veri yükleme hatası: {str(e)}")
            raise
    
    def retrieve_context(self, query: str, n_results: int = 8, exclude_titles: List[str] = None) -> List[Dict[str, Any]]:
        """
        Kullanıcı sorusu için ilgili bağlamı getirir (Hybrid Retrieval)
        
        Args:
            query: Kullanıcının sorusu
            n_results: Getirilecek sonuç sayısı
            exclude_titles: Önceki sorularda gösterilen başlıklar (tekrar gösterilmemesi için)
            
        Returns:
            İlgili dokümanların listesi
        """
        try:
            if exclude_titles is None:
                exclude_titles = []
            # Şehir ve bölge haritası
            city_keywords = {
                'istanbul': 'İstanbul',
                'ankara': 'Ankara',
                'izmir': 'İzmir',
                'antalya': 'Antalya',
                'kapadokya': 'Nevşehir',
                'kappadokya': 'Nevşehir',
                'göreme': 'Nevşehir',
                'nevşehir': 'Nevşehir',
                'efes': 'İzmir',
                'bergama': 'İzmir',
                'pamukkale': 'Denizli',
                'nemrut': 'Adıyaman',
                'trabzon': 'Trabzon',
                'van': 'Van',
                'konya': 'Konya',
                'gaziantep': 'Gaziantep',
                'urfa': 'Şanlıurfa',
                'şanlıurfa': 'Şanlıurfa',
                'mardin': 'Mardin',
                'bodrum': 'Muğla',
                'marmaris': 'Muğla',
                'fethiye': 'Muğla',
                'ölüdeniz': 'Muğla',
                'çanakkale': 'Çanakkale',
                'truva': 'Çanakkale',
                'troya': 'Çanakkale',
                'bursa': 'Bursa',
                'edirne': 'Edirne',
                'kars': 'Kars',
                'erzurum': 'Erzurum',
                'sivas': 'Sivas',
                'amasya': 'Amasya',
                'safranbolu': 'Karabük',
                'karabük': 'Karabük'
            }
            
            # Query'den şehir bilgisini çıkar
            query_lower = query.lower()
            detected_city = None
            for keyword, city in city_keywords.items():
                if keyword in query_lower:
                    detected_city = city
                    break
            
            context_docs = []
            
            # Eğer şehir tespit edildiyse, önce o şehirden kayıtları getir
            if detected_city:
                # Şehre özel filtreleme (hız için optimize)
                city_results = self.collection.query(
                    query_texts=[query],
                    n_results=min(n_results + 2, 8),  # Hız için daha az
                    where={"sehir": detected_city}
                )
                
                if city_results['documents'] and len(city_results['documents']) > 0:
                    for i, doc in enumerate(city_results['documents'][0]):
                        metadata = city_results['metadatas'][0][i] if city_results['metadatas'] else {}
                        baslik = metadata.get('baslik', '')
                        
                        # Exclude listesinde yoksa ekle
                        if baslik not in exclude_titles:
                            context_docs.append({
                                'document': doc,
                                'metadata': metadata,
                                'distance': city_results['distances'][0][i] if city_results.get('distances') else None,
                                'priority': 'high'  # Şehir eşleşmesi yüksek öncelik
                            })
            
            # Genel semantic search yap (hız için optimize)
            general_results = self.collection.query(
                query_texts=[query],
                n_results=n_results + 2  # Hız için daha az
            )
            
            if general_results['documents'] and len(general_results['documents']) > 0:
                for i, doc in enumerate(general_results['documents'][0]):
                    metadata = general_results['metadatas'][0][i] if general_results['metadatas'] else {}
                    baslik = metadata.get('baslik', '')
                    
                    # Tekrar eklememek için ve exclude listesinde olmadığını kontrol et
                    already_added = any(d['metadata'].get('baslik') == baslik for d in context_docs)
                    in_exclude_list = baslik in exclude_titles
                    
                    if not already_added and not in_exclude_list:
                        context_docs.append({
                            'document': doc,
                            'metadata': metadata,
                            'distance': general_results['distances'][0][i] if general_results.get('distances') else None,
                            'priority': 'normal'
                        })
            
            # Önceliğe göre sırala (high priority önce)
            context_docs.sort(key=lambda x: (0 if x.get('priority') == 'high' else 1, x.get('distance', 999)))
            
            # Maksimum n_results kadar döndür
            return context_docs[:n_results]
            
        except Exception as e:
            print(f"✗ Bağlam getirme hatası: {str(e)}")
            return []
    
    def generate_response(self, query: str, context_docs: List[Dict[str, Any]]) -> str:
        """
        Gemini API kullanarak bağlam ve soruya dayalı yanıt üretir
        
        Args:
            query: Kullanıcının sorusu
            context_docs: İlgili bağlam dokümanları
            
        Returns:
            Üretilen yanıt metni
        """
        try:
            if not context_docs:
                return "Üzgünüm, bu konu hakkında şu an bilgim yok. Başka bir konu hakkında soru sorabilir misiniz?"
            
            # Bağlamı birleştir
            context_text = "\n\n---\n\n".join([doc['document'] for doc in context_docs])
            
            # Kaynak listesi oluştur
            sources_list = [f"- {doc['metadata'].get('baslik', 'Bilinmeyen')} ({doc['metadata'].get('sehir', 'Bilinmeyen')})" 
                           for doc in context_docs]
            sources_text = "\n".join(sources_list[:5])  # İlk 5 kaynağı göster
            
            # Kaç kaynak olduğunu belirt
            kaynak_sayisi = len(context_docs)
            
            # Prompt oluştur (hız + görsel optimizasyon)
            prompt = f"""
Sen Türkiye turizm konusunda uzman, yardımsever ve bilgili bir asistansın. 

Aşağıdaki veritabanından alınan bilgileri kullanarak kullanıcının sorusuna DETAYLI, BİLGİLENDİRİCİ ve DOSTANE bir şekilde cevap ver.

VERİTABANINDAN ALINAN BİLGİLER ({kaynak_sayisi} KAYNAK):
{context_text}

KULLANICI SORUSU: {query}

ÖNEMLİ KURALLAR:
1. SADECE yukarıdaki veritabanı bilgilerini kullan
2. Veritabanında {kaynak_sayisi} kaynak var - HEPSİNİ KULLAN ve bahset
3. "İzmirdeki antik kentler" gibi sorularda, veritabanındaki TÜM antik kentleri say
4. Bir şehirle ilgili sorularda, o şehirle ilgili BÜTÜN yerleri listele
5. Her yerin adını, özelliklerini, tarihi önemini ve pratik bilgilerini (ziyaret saatleri, ücret) detaylı belirt
6. Eğer veritabanında bilgi yoksa, "Bu konu hakkında şu anda bilgim yok" de
7. HTML formatı kullan: <strong>kalın</strong>, <em>italik</em>, <br> satır sonu
8. Emojiler kullan: 🏛️ antik kentler, 🏔️ doğa, 🏖️ plaj, 🍽️ yemek, ⏰ saat, 💰 ücret, 📍 konum
9. Numaralı liste veya madde işaretleri kullanarak düzenli yaz
10. Hiçbir kaynağı atlama, hepsinden bahset!

CEVAP:
"""
            
            # Gemini'den yanıt al
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            print(f"✗ Yanıt üretme hatası: {str(e)}")
            return "Üzgünüm, yanıt oluştururken bir hata oluştu. Lütfen tekrar deneyin."
    
    def query(self, user_query: str, n_results: int = 8, exclude_titles: List[str] = None) -> Dict[str, Any]:
        """
        Kullanıcı sorgusunu işler ve yanıt döndürür
        
        Args:
            user_query: Kullanıcının sorusu
            n_results: Getirilecek bağlam sayısı
            exclude_titles: Daha önce gösterilen başlıklar
            
        Returns:
            Yanıt ve metadata içeren dictionary
        """
        # İlgili bağlamı getir
        if exclude_titles is None:
            exclude_titles = []
        context_docs = self.retrieve_context(user_query, n_results, exclude_titles)
        
        # Yanıt üret
        response = self.generate_response(user_query, context_docs)
        
        # Kullanılan kaynaklardan metadata çıkar
        sources = [
            {
                'baslik': doc['metadata'].get('baslik', 'Bilinmiyor'),
                'sehir': doc['metadata'].get('sehir', 'Bilinmiyor'),
                'kategori': doc['metadata'].get('kategori', 'Bilinmiyor')
            }
            for doc in context_docs
        ]
        
        return {
            'query': user_query,
            'response': response,
            'sources': sources,
            'context_count': len(context_docs)
        }


def test_rag_pipeline():
    """
    RAG pipeline'ı test eder (geliştirme amaçlı)
    """
    # API key'i environment variable'dan al
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("✗ GEMINI_API_KEY environment variable tanımlanmamış!")
        return
    
    # RAG pipeline'ı başlat
    rag = TurkiyeTourismRAG(api_key=api_key)
    
    # Test sorguları
    test_queries = [
        "İstanbul'da görülmesi gereken yerler nelerdir?",
        "Kapadokya'da ne yapabilirim?",
        "Pamukkale hakkında bilgi verir misin?",
        "Ege bölgesindeki antik kentler hangileri?"
    ]
    
    print("\n" + "="*80)
    print("RAG PIPELINE TEST")
    print("="*80 + "\n")
    
    for query in test_queries:
        print(f"\n📌 SORU: {query}")
        print("-" * 80)
        result = rag.query(query)
        print(f"💬 CEVAP:\n{result['response']}")
        print(f"\n📚 KAYNAKLAR:")
        for source in result['sources']:
            print(f"  • {source['baslik']} ({source['sehir']})")
        print("\n" + "="*80)


if __name__ == "__main__":
    test_rag_pipeline()

