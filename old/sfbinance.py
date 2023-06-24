from os import listdir
import requests
from pprint import pprint

# market tickers url list
BINANCE_URL = 'https://sandwichfinance.blob.core.windows.net/files/binance_all_markets.txt'

# get ticker data from sandwich.finance
req = requests.get(BINANCE_URL).text


def clear_hashtags(tickers):
    
    # her bir ticker in satirlarina ayir ve tickers_list listesine ata 
    tickers_list = tickers.splitlines()

    # her bir ticker elemaninin icinde '###' olup olmadigini incele
    # eger '###' bulunursa tickers_list listesinden cikar
    for ticker in tickers_list:
        if '###' in ticker:
            tickers_list.remove(ticker)
    
    return tickers_list

def store_tickers(tickers_list):

    # tickers_list listesindeki her bir elemani '\n' ile birlestir
    # old_ticker.txt dosyasina yaz
    with open('old/old_ticker.txt', 'w') as ticker_file:
        ticker_file.write('\n'.join(tickers_list))

# yeni veriler ile eski verileri kiyasla
def compare(ticker_list):
    
    # old dosyasinin icine old_ticker.txt olup olmadigini kontrol et
    if 'old_ticker.txt' in listdir('old'):
        
        # eski veriyi oku
        with open('old/old_ticker.txt', 'r') as ticker_file:

            # old_ticker.txt dosyasini oku ve listeye cevir
            old_tickers = ticker_file.read().splitlines()

        # yeni cektigimiz veriyi '###' temizle ve listeye cevir
        new_ticker_list = clear_hashtags(req)
        # new_ticker_list.append('BINANCE:RSLBTC')
        # new_ticker_list.append('BINANCE:RSLUSDT')
        # new_ticker_list.append('BINANCE:RSLTRY')
        # new_ticker_list.remove('BINANCE:ALGOBTC')

        new_listings = list() # new_listings = []

        # yeni listede olupta eski listede olmayanlari bul ve listele
        # yeni eklenen ticker lari bul 
        for new_ticker in new_ticker_list:
            if new_ticker not in old_tickers:
                new_listings.append(new_ticker)

        # cikarilan ticker lari bul
        delist = list(set(old_tickers) - set(new_ticker_list))

        print(f'new listings: {new_listings}')
        print(f'delist      : {delist}')

        store_tickers(new_ticker_list)


    else:
        store_tickers(ticker_list)
        print('Karsilastirilacak dosyalar bulunamadi. Dosya kaydedildi. Bir sonraki karsilastirma icin program hazir..')


compare(req)