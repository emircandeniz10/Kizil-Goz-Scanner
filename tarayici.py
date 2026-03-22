import socket
import concurrent.futures
import datetime
import argparse
import sqlite3
def logo_yazdir():
    # Tırnak işaretinden önceki 'r' harfine dikkat! Bu, şeklin bozulmasını engeller.
    print(r"""
    ██╗  ██╗██╗███████╗██╗██╗      ██████╗  ██████╗ ███████╗
    ██║ ██╔╝██║╚══███╔╝██║██║     ██╔════╝ ██╔═══██╗╚══███╔╝
    █████╔╝ ██║  ███╔╝ ██║██║     ██║  ███╗██║   ██║  ███╔╝ 
    ██╔═██╗ ██║ ███╔╝  ██║██║     ██║   ██║██║   ██║ ███╔╝  
    ██║  ██╗██║███████╗██║███████╗╚██████╔╝╚██████╔╝███████╗
    ╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝
    >> KIZIL GÖZ CYBER SCANNER V7.1 | Developed by Emir <<
    """)

# Program başlar başlamaz logoyu göster
logo_yazdir()
# Terminal Komutlarını Al
komut_yakalayici = argparse.ArgumentParser()
komut_yakalayici.add_argument("hedef")
komut_yakalayici.add_argument("-p", "--port", type=int, default=1000)
ayarlar = komut_yakalayici.parse_args()

hedef_site = ayarlar.hedef
kac_port_taranacak = ayarlar.port

print("*" * 65)
print("🔴 SİBER AJAN V7.1 - KIZIL GÖZ (Kusursuz Veritabanı) 🔴")
print("*" * 65)

# Ajanların bulduklarını atacağı geçici sepet
acik_portlar_listesi = []

try:
    hedef_ip = socket.gethostbyname(hedef_site)
    print(f"\n🎯 HEDEF KİLİTLENDİ: {hedef_ip}")
    print(f"100 Ajan sahada, {kac_port_taranacak} kapı taranıyor...\n")

    def port_tara(port):
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
            # Veritabanına saldırmak yerine sadece sepete atıyoruz
            acik_portlar_listesi.append((hedef_ip, port, kimlik))
                
        ajan.close()

    # Ajanları sahaya sür
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as ajan_ordusu:
        for port_numarasi in range(1, kac_port_taranacak + 1):
            ajan_ordusu.submit(port_tara, port_numarasi)

    # -----------------------------------------
    # MERKEZİ KAYIT SİSTEMİ (Çakışmayı Önler)
    # -----------------------------------------
    if len(acik_portlar_listesi) > 0:
        print("\n🗄️ Ajanlar döndü. Bulgular sırayla veritabanına işleniyor...")
        baglanti = sqlite3.connect("siber_istihbarat.db")
        islem = baglanti.cursor()
        
        islem.execute("""
        CREATE TABLE IF NOT EXISTS acik_portlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hedef_ip TEXT,
            port_no INTEGER,
            kimlik_banner TEXT,
            tarama_tarihi TEXT
        )
        """)
        
        zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Sepetteki tüm kayıtları tek bir işçi sırayla veritabanına yazar
        for kayit in acik_portlar_listesi:
            islem.execute("INSERT INTO acik_portlar (hedef_ip, port_no, kimlik_banner, tarama_tarihi) VALUES (?, ?, ?, ?)", 
                          (kayit[0], kayit[1], kayit[2], zaman))
        
        baglanti.commit()
        baglanti.close()
        print("✅ TARAMA BİTTİ! Tüm veriler 'siber_istihbarat.db' dosyasına mühürlendi.")
    else:
        print("\n✅ Tarama bitti, açık kapı bulunamadı. Veritabanına kayıt yapılmadı.")

except socket.gaierror:
    print("\n❌ HATA: Hedef bulunamadı!")
except KeyboardInterrupt:
    print("\n⚠️ Tarama iptal edildi.")