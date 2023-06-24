# Sandwich-Finance

Bu Python programı, Sandwich Finance üzerinden alınan ticker verilerini kullanarak eski ve yeni verileri karşılaştırır. Program, yeni eklenen ve silinen tickerları bulur ve bunları ekrana yazdırır. Ayrıca, eski veriye dayanarak yeni verileri kaydeder.

## Kullanılan Kütüphaneler

- `os`: Dosya ve dizin işlemleri için kullanılır.
- `requests`: HTTP istekleri göndermek ve veri almak için kullanılır.
- `pprint`: Veri yapılarını düzenli bir şekilde ekrana yazdırmak için kullanılır.

## Özellikler

- Sandwich Finance üzerinden ticker verilerini alır.
- Ticker verilerinde bulunan '# ##' sembollerini temizler.
- Eski ve yeni verileri karşılaştırır.
- Yeni eklenen ve silinen tickerları ekrana yazdırır.
- Yeni verileri kaydeder.

## Kullanım

1. `compare_tickers.py` dosyasını çalıştırın.
2. Program, Sandwich Finance'den ticker verilerini alacak ve eski ve yeni verileri karşılaştıracaktır.
3. Yeni eklenen ve silinen tickerlar ekrana yazdırılacak ve `old/old_ticker.txt` dosyasına kaydedilecektir.
4. Eğer `old` dizininde `old_ticker.txt` dosyası bulunmuyorsa, program eski verileri kaydedecek ve bir sonraki karşılaştırma için hazır olacak.
   
