import sqlite3
import datetime

print("*" * 65)
print("🕸️ SİBER İSTİHBARAT AĞI - KARANLIK WEB PANELİ OLUŞTURUCU 🕸️")
print("*" * 65)

try:
    # 1. Veritabanına Bağlan ve Verileri Çek
    print("🗄️ Veritabanına (siber_istihbarat.db) sızılıyor...")
    baglanti = sqlite3.connect("siber_istihbarat.db")
    islem = baglanti.cursor()
    
    islem.execute("SELECT hedef_ip, port_no, kimlik_banner, tarama_tarihi FROM acik_portlar")
    veriler = islem.fetchall()
    
    if len(veriler) == 0:
        print("⚠️ Veritabanında hiç açık port kaydı yok. Önce tarayıcıyı çalıştırın!")
    else:
        print(f"📊 Toplam {len(veriler)} adet açık kapı kaydı bulundu. Rapor işleniyor...")
        
        # 2. Matrix Temalı HTML Tasarımı (Karanlık Tema ve Yeşil Yazılar)
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
            
            # Eğer kimlik "Gizli" değilse, yazıyı kırmızı yapıp tehlikeyi vurgulayalım
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
        
        # 4. Her Şeyi Birleştir ve .html Dosyası Olarak Kaydet
        tam_html = html_baslangic + html_orta + html_bitis
        
        with open("siber_rapor.html", "w", encoding="utf-8") as dosya:
            dosya.write(tam_html)
            
        print("✅ GÖREV TAMAM! 'siber_rapor.html' dosyası yaratıldı.")
        
except sqlite3.Error as hata:
    print(f"❌ Veritabanı Hatası: {hata}")
finally:
    if 'baglanti' in locals():
        baglanti.close()