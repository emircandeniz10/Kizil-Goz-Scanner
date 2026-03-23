# 👁️ KIZIL GÖZ (Red Eye) - Cyber Intelligence Tool

Kızıl Göz, Python ile geliştirilmiş, çok iş parçacıklı (multithreaded) bir ağ tarama ve istihbarat toplama aracıdır.

## 🚀 Özellikler
* **Işık Hızında Tarama:** `concurrent.futures` kullanarak 100 farklı ajanla aynı anda tarama yapar.
* **İstihbarat Toplama (Banner Grabbing):** Açık portlardaki servislerin sürüm bilgilerini (SSH, HTTP vb.) otomatik olarak yakalar.
* **SQL Veritabanı Entegrasyonu:** Tüm bulguları `siber_istihbarat.db` içine yapılandırılmış şekilde kaydeder.
* **Karanlık Web Paneli:** SQL verilerini kullanarak Matrix temalı HTML raporları üretir.
* **CLI Desteği:** Tamamen terminal üzerinden parametrelerle yönetilebilir.
* **📲 Telegram Bot Entegrasyonu:** Açık port tespit edildiğinde anlık bildirim gönderir ve operasyon sonunda detaylı raporu dosya olarak cebinize fırlatır.

## 🛠️ Kurulum ve Kullanım
1. Projeyi klonlayın.
2. Terminalden taramayı başlatın:
   ```bash
   python network_analyzer.py scanme.nmap.org -p 1000
## 📸 Ekran Görüntüleri

### 🖥️ Profesyonel HTML Raporu
[  <img width="1909" height="969" alt="HTML RAPORU" src="https://github.com/user-attachments/assets/2eb0edf2-fc63-49ee-8202-fb881240b5ed" />
    ]

### 📲 Telegram Bildirim Sistemi
[ ![kızılgöz screenshot telegram](https://github.com/user-attachments/assets/6e3777c5-ebd1-4b2a-858d-53948a981aec)
     ]

### ⚙️ Otonom Terminal Akışı
[    <img width="1917" height="1006" alt="Otonom terminal akışı" src="https://github.com/user-attachments/assets/f2e06066-ef30-414b-834b-a57e46028f63" />
  ]
