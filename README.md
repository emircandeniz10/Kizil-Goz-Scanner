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
