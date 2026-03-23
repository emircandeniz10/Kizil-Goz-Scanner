import sqlite3
import datetime

def rapor_olustur():
    print("*" * 65)
    print("🕸️ SİBER İSTİHBARAT AĞI - KARANLIK WEB PANELİ OLUŞTURUCU 🕸️")
    print("*" * 65)

    try:
        # 1. Veritabanına Bağlan ve Verileri Çek
        print("🗄️ Veritabanına (siber_istihbarat.db) sızılıyor...")
        baglanti = sqlite3.connect("siber_istihbarat.db")
        islem = baglanti.cursor()
        
        islem.execute("SELECT hedef_ip, port_no, kimlik_banner, tarama_tarihi FROM acik_portlar ORDER BY id DESC")
        veriler = islem.fetchall()
        
        if len(veriler) == 0:
            print("⚠️ Veritabanında hiç açık port kaydı yok. Önce tarayıcıyı çalıştırın!")
        else:
            print(f"📊 Toplam {len(veriler)} adet açık kapı kaydı bulundu. Rapor işleniyor...")
            
            # 2. Matrix Temalı HTML Tasarımı
            html_baslangic = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Siber İstihbarat Raporu</title>
                <meta charset="utf-8">
                <style>
                    body {{ background-color: #0d1117; color: #00ff00; font-family: 'Courier New', Courier, monospace; padding: 20px; }}
                    h1 {{ color: #00ff00; text-align: center; border-bottom: 1px solid #00ff00; padding-bottom: 10px; }}
                    table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background-color: #161b22; }}
                    th, td {{ border: 1px solid #30363d; padding: 12px; text-align: left; }}
                    th {{ background-color: #21262d; color: #58a6ff; font-weight: bold; font-size: 1.1em; }}
                    tr:hover {{ background-color: #1f2428; }}
                    .zaman {{ text-align: right; font-size: 0.9em; color: #8b949e; }}
                    .tehlike {{ color: #ff7b72; font-weight: bold; }}
                </style>
            </head>
            <body>
                <h1>🛡️ KIZIL GÖZ SİBER İSTİHBARAT RAPORU 🛡️</h1>
                <div class="zaman">Rapor Üretim Tarihi: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
                <table>
                    <tr>
                        <th>Hedef IP</th>
                        <th>Açık Port</th>
                        <th>Sistem Kimliği (Banner)</th>
                        <th>Tespit Tarihi</th>
                    </tr>
            """
            
            # 3. Verileri HTML Tablosunun İçine Yerleştir
            html_orta = ""
            for kayit in veriler:
                ip, port, kimlik, tarih = kayit
                kimlik_stili = f"<span class='tehlike'>{kimlik}</span>" if kimlik != "Gizli" else kimlik
                
                html_orta += f"""
                    <tr>
                        <td>{ip}</td>
                        <td><strong>{port}</strong></td>
                        <td>{kimlik_stili}</td>
                        <td>{tarih}</td>
                    </tr>
                """
                
            html_bitis = """
                </table>
            </body>
            </html>
            """
            
            # 4. Her Şeyi Birleştir ve Kaydet
            tam_html = html_baslangic + html_orta + html_bitis
            
            with open("siber_rapor.html", "w", encoding="utf-8") as dosya:
                dosya.write(tam_html)
                
            print("✅ GÖREV TAMAM! 'siber_rapor.html' dosyası yaratıldı.")
            
    except sqlite3.Error as hata:
        print(f"❌ Veritabanı Hatası: {hata}")
    finally:
        if 'baglanti' in locals():
            baglanti.close()

# Eğer dosya direkt çalıştırılırsa raporu oluştur:
if __name__ == "__main__":
    rapor_olustur()
    import requests

# ... Mevcut rapor oluşturma kodlarının bittiği yer ...

def raporu_telegrama_firlat():
    print("\n⏳ Matrix Raporu Telegram'a yükleniyor...")
    
    # Senin özel token ve chat ID bilgilerini ekledim:
    TOKEN = "8718893664:AAHwp6-GakMEOkC1RfGJpPJMbYhQbPec8rI"
    CHAT_ID = "1814688893"
    DOSYA_YOLU = "siber_rapor.html"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    
    try:
        # Dosyayı "rb" (read binary) modunda açıyoruz
        with open(DOSYA_YOLU, "rb") as dosya:
            payload = {"chat_id": CHAT_ID}
            files = {"document": dosya}
            
            # Post isteği ile dosyayı fırlatıyoruz
            response = requests.post(url, data=payload, files=files)
            
        if response.status_code == 200:
            print("[+] GÖREV TAMAM! Rapor başarıyla cebine fırlatıldı. 🚀📱")
        else:
            print(f"[-] Hata oluştu: {response.text}")
            
    except Exception as e:
        print(f"[-] Dosya okunurken bir sorun çıktı: {e}")

# Fonksiyonu ateşle!
raporu_telegrama_firlat()
