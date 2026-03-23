import socket
import concurrent.futures
import datetime
import argparse
import sqlite3
import requests

# --- 🛰️ İSTİHBARAT MERKEZİ (TELEGRAM) ---
def istihbarat_gonder(mesaj):
    # Senin mühürlü şifrelerin
    TOKEN = "8718893664:AAHwp6-GakMEOkC1RfGJpPJMbYhQbPec8rI"
    CHAT_ID = "1814688893"
    
    try:
        send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID, 
            "text": f"🚨 *[KIZIL GÖZ - CANLI RAPOR]*\n\n{mesaj}",
            "parse_mode": "Markdown"
        }
        requests.post(send_url, data=payload)
    except Exception as e:
        print(f"[!] İstihbarat hatası: {e}")

# --- 🎨 GÖRSEL ARAYÜZ ---
def logo_yazdir():
    print(r"""
    ██╗  ██╗██╗███████╗██╗██╗      ██████╗  ██████╗ ███████╗
    ██║ ██╔╝██║╚══███╔╝██║██║     ██╔════╝ ██╔═══██╗╚══███╔╝
    █████╔╝ ██║  ███╔╝ ██║██║     ██║  ███╗██║   ██║  ███╔╝ 
    ██╔═██╗ ██║ ███╔╝  ██║██║     ██║   ██║██║   ██║ ███╔╝  
    ██║  ██╗██║███████╗██║███████╗╚██████╔╝╚██████╔╝███████╗
    ╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝
    >> KIZIL GÖZ CYBER SCANNER V7.1 | Developed by Emir <<
    """)

# Ajanların bulduklarını atacağı geçici sepet
acik_portlar_listesi = []

# --- 🕵️‍♂️ PORT TARAMA AJANI ---
def port_tara(hedef_ip, port):
    ajan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ajan.settimeout(1.5)
    sonuc = ajan.connect_ex((hedef_ip, port))
    
    if sonuc == 0:
        try:
            ajan.send(b"Merhaba\r\n") 
            banner = ajan.recv(1024).decode('utf-8', errors='ignore').strip()
            kimlik = banner if banner else "Gizli"
        except:
            kimlik = "Güvenlik Duvarı Engeli"
        
        print(f"[+] Port {port} AÇIK | Kimlik: {kimlik}")
        
        # CANLI BİLDİRİM
        istihbarat_gonder(f"Hedef: {hedef_ip}\nPort {port} AÇIK bulundu!\nServis: {kimlik}")
        
        # Sepete ekle
        acik_portlar_listesi.append((hedef_ip, port, kimlik))
            
    ajan.close()

# --- 🚀 ANA OPERASYON ---
def main():
    logo_yazdir()

    komut_yakalayici = argparse.ArgumentParser()
    komut_yakalayici.add_argument("hedef")
    komut_yakalayici.add_argument("-p", "--port", type=int, default=1000)
    ayarlar = komut_yakalayici.parse_args()

    hedef_site = ayarlar.hedef
    kac_port_taranacak = ayarlar.port

    print("*" * 65)
    print("🔴 SİBER AJAN V7.1 - KIZIL GÖZ (Kusursuz Veritabanı) 🔴")
    print("*" * 65)

    try:
        # Bak, bu satır 'try'dan tam 4 boşluk (1 Tab) içeride olmalı!
        istihbarat_gonder("Sinyal kontrolü: Kızıl Göz siber uzaya çıkıyor... 🛰️")
        
        hedef_ip = socket.gethostbyname(hedef_site)
        print(f"\n🎯 HEDEF KİLİTLENDİ: {hedef_ip}")
        print(f"100 Ajan sahada, {kac_port_taranacak} kapı taranıyor...\n")

        # Tarama başlama sinyali (Zaten yukarıda gönderdik, istersen burayı silebilirsin)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as ajan_ordusu:
            for port_numarasi in range(1, kac_port_taranacak + 1):
                ajan_ordusu.submit(port_tara, hedef_ip, port_numarasi)
        # Veritabanı Kayıt
        if len(acik_portlar_listesi) > 0:
            print("\n🗄️ Bulgular veritabanına işleniyor...")
            baglanti = sqlite3.connect("siber_istihbarat.db")
            islem = baglanti.cursor()
            islem.execute("""
            CREATE TABLE IF NOT EXISTS acik_portlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hedef_ip TEXT, port_no INTEGER, kimlik_banner TEXT, tarama_tarihi TEXT
            )
            """)
            zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for kayit in acik_portlar_listesi:
                islem.execute("INSERT INTO acik_portlar (hedef_ip, port_no, kimlik_banner, tarama_tarihi) VALUES (?, ?, ?, ?)", 
                             (kayit[0], kayit[1], kayit[2], zaman))
            baglanti.commit()
            baglanti.close()
            print("✅ TARAMA BİTTİ! Veriler mühürlendi.")
        else:
            print("\n✅ Tarama bitti, açık kapı bulunamadı.")

    except socket.gaierror:
        print("\n❌ HATA: Hedef bulunamadı!")
    except KeyboardInterrupt:
        print("\n⚠️ Tarama iptal edildi.")

if __name__ == "__main__":
    main()
    import rapor_olusturucu
rapor_olusturucu.rapor_olustur()
import webbrowser
import os

# Rapor oluştuktan hemen sonra bu satırı ekle:
webbrowser.open('file://' + os.path.realpath("siber_rapor.html"))
import os
os.system("python rapor_olusturucu.py")