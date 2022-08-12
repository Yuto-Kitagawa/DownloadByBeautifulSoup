import cloudscraper
from bs4 import BeautifulSoup
import requests
import os

#cloudflareにブロックされたときの回避
#requestは使いません
scraper = cloudscraper.create_scraper()

# アクセスするURL
url = "https://www.pexels.com/ja-jp/"
response = scraper.get(url=url)
soup = BeautifulSoup(response.text, "lxml")

#最初に実行
if __name__ == '__main__':

    #ディレクトリがない場合、作成
    basename = "./img/"
    os.makedirs(basename,exist_ok=True)

    # インデックスを写真の名前に付与
    counter = 1
    
    #写真の数だけ繰り返し
    for download_url_element in soup.select("a.ButtonGroup_buttonOverrides__NuhSe"):
        # 写真のダウンロードURLを取得
        download_url = download_url_element.get('href')
        
        # URLに写真と動画があるので、写真の時だけ処理
        if("https://images.pexels.com/photos" in download_url):
            
            # 写真のURLにリクエスト
            r = requests.get(download_url).content

            with open(basename+'image' + str(counter) + '.jpg', 'wb') as handler:
                handler.write(r)
                counter += 1


