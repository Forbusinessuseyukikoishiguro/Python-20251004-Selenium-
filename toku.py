# === 必要なライブラリを全てインポート ===
# Seleniumの基本機能
from selenium import webdriver
# Chromeのオプション設定用
from selenium.webdriver.chrome.options import Options
# Chromeのサービス設定用
from selenium.webdriver.chrome.service import Service
# ChromeDriverを自動ダウンロードするツール
from webdriver_manager.chrome import ChromeDriverManager
# HTML要素を探すための方法を指定
from selenium.webdriver.common.by import By
# BeautifulSoupでHTML解析
from bs4 import BeautifulSoup
# 待機処理用
import time
# ログ出力用
import logging

# ログの設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def find_specific_elements(url):
    """
    特定のパターンの要素を探索する
    """
    # Chromeのオプションを作成
    chrome_options = Options()
    
    # ヘッドレスモードをオフ(画面を表示)
    # chrome_options.add_argument('--headless')  # コメントアウト=画面表示
    
    # その他の基本設定
    chrome_options.add_argument('--disable-gpu')  # GPU無効化
    chrome_options.add_argument('--no-sandbox')  # サンドボックス無効化
    chrome_options.add_argument('--window-size=1920,1080')  # ウィンドウサイズ
    
    # User-Agentを設定(ボット判定回避)
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
    
    # ChromeDriverを自動インストール
    service = Service(ChromeDriverManager().install())
    
    # Chromeドライバーを起動
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # 対象URLにアクセス
        logger.info(f"アクセス中: {url}")
        driver.get(url)
        
        # ページが完全に読み込まれるまで3秒待機
        time.sleep(3)
        
        # ページのHTMLソースを取得
        page_source = driver.page_source
        
        # BeautifulSoupで解析(HTMLを扱いやすくする)
        soup = BeautifulSoup(page_source, 'html.parser')
        
        print("\n" + "="*80)
        print("【coorikuya.com 詳細な要素検索】")
        print("="*80)
        
        # === パターン1: 記事一覧を探す ===
        print("\n1. 記事一覧候補:")
        # よくある記事一覧のパターン(CSSセレクター)
        patterns = [
            ('article'),  # articleタグ
            ('.post'),  # postクラス
            ('.entry'),  # entryクラス
            ('.blog-post'),  # blog-postクラス
            ('.article-item'),  # article-itemクラス
            ('[class*="post"]'),  # postを含むクラス
            ('.card'),  # cardクラス
            ('.item'),  # itemクラス
        ]
        
        # 各パターンで要素を検索
        for pattern in patterns:
            # CSSセレクターで要素を検索
            elements = soup.select(pattern)
            # 要素が見つかった場合
            if elements:
                print(f"  ✓ セレクター '{pattern}': {len(elements)}個見つかりました")
                # 最初の要素の構造を表示
                if elements:
                    first = elements[0]
                    # タグ名とクラス名を取得
                    class_list = first.get('class', [])
                    print(f"    構造例: <{first.name} class='{' '.join(class_list)}'>")
                    # 直接の子要素を確認
                    children = first.find_all(recursive=False)
                    print(f"    直接の子要素: {len(children)}個")
        
        # === パターン2: タイトルを探す ===
        print("\n2. タイトル候補:")
        title_patterns = [
            ('h1'),  # h1タグ
            ('h2'),  # h2タグ
            ('h2.entry-title'),  # entry-titleクラスを持つh2
            ('h2.post-title'),  # post-titleクラスを持つh2
            ('.title'),  # titleクラス
            ('article h2'),  # article内のh2
            ('h2 a'),  # リンクを含むh2
            ('.entry-title'),  # entry-titleクラス
        ]
        
        # 各パターンで検索
        for pattern in title_patterns:
            elements = soup.select(pattern)
            if elements:
                print(f"  ✓ '{pattern}': {len(elements)}個")
                # 最初のテキストを表示(50文字まで)
                if elements:
                    text = elements[0].get_text(strip=True)
                    print(f"    例: {text[:50]}")
        
        # === パターン3: 日付を探す ===
        print("\n3. 日付候補:")
        date_patterns = [
            ('time'),  # timeタグ
            ('.date'),  # dateクラス
            ('.published'),  # publishedクラス
            ('.entry-date'),  # entry-dateクラス
            ('[datetime]'),  # datetime属性を持つ要素
            ('.post-date'),  # post-dateクラス
        ]
        
        # 各パターンで検索
        for pattern in date_patterns:
            elements = soup.select(pattern)
            if elements:
                print(f"  ✓ '{pattern}': {len(elements)}個")
                if elements:
                    # テキストまたはdatetime属性を表示
                    text = elements[0].get_text(strip=True)
                    datetime_attr = elements[0].get('datetime', '')
                    print(f"    例: {text}")
                    if datetime_attr:
                        print(f"    datetime属性: {datetime_attr}")
        
        # === パターン4: 本文・抜粋を探す ===
        print("\n4. 本文・抜粋候補:")
        content_patterns = [
            ('.entry-content'),  # entry-contentクラス
            ('.post-content'),  # post-contentクラス
            ('.excerpt'),  # excerptクラス
            ('.summary'),  # summaryクラス
            ('article p'),  # article内のp(段落)
            ('.description'),  # descriptionクラス
        ]
        
        # 各パターンで検索
        for pattern in content_patterns:
            elements = soup.select(pattern)
            if elements:
                print(f"  ✓ '{pattern}': {len(elements)}個")
                if elements:
                    # テキストを取得(最初の80文字)
                    text = elements[0].get_text(strip=True)
                    print(f"    例: {text[:80]}...")
        
        # === パターン5: カテゴリー・タグを探す ===
        print("\n5. カテゴリー・タグ候補:")
        category_patterns = [
            ('.category'),  # categoryクラス
            ('.tag'),  # tagクラス
            ('.categories'),  # categoriesクラス
            ('.tags'),  # tagsクラス
            ('a[rel="category"]'),  # rel属性がcategoryのリンク
            ('a[rel="tag"]'),  # rel属性がtagのリンク
            ('.cat-links'),  # cat-linksクラス
        ]
        
        # 各パターンで検索
        for pattern in category_patterns:
            elements = soup.select(pattern)
            if elements:
                print(f"  ✓ '{pattern}': {len(elements)}個")
                if elements:
                    # テキストを表示
                    print(f"    例: {elements[0].get_text(strip=True)}")
        
        # === パターン6: 画像を探す ===
        print("\n6. 画像候補:")
        images = soup.find_all('img')
        print(f"  総画像数: {len(images)}個")
        
        # 最初の3つの画像を表示
        for i, img in enumerate(images[:3], 1):
            src = img.get('src', '')
            alt = img.get('alt', '')
            print(f"  {i}. alt='{alt[:30]}' src='{src[:60]}'")
        
        # === パターン7: リンクを探す ===
        print("\n7. リンク候補:")
        links = soup.find_all('a', href=True)
        print(f"  総リンク数: {len(links)}個")
        
        # 最初の5つのリンクを表示
        for i, link in enumerate(links[:5], 1):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            print(f"  {i}. {text[:30]} -> {href[:50]}")
        
        # === 全体のHTML構造ツリーを表示 ===
        print("\n8. HTML構造ツリー(body直下の要素):")
        body = soup.find('body')
        if body:
            # bodyの直接の子要素を列挙
            for i, child in enumerate(body.find_all(recursive=False), 1):
                # クラス名を取得
                class_str = ' '.join(child.get('class', []))
                # ID属性を取得
                id_str = child.get('id', '')
                
                # 出力
                print(f"  {i}. <{child.name}> ", end='')
                if id_str:
                    print(f"id='{id_str}' ", end='')
                if class_str:
                    print(f"class='{class_str}'", end='')
                print()
        
        # === よく使われているクラス名のランキング ===
        print("\n9. 頻出クラス名トップ10:")
        class_counter = {}
        # 全てのタグからクラス名を収集
        for tag in soup.find_all(class_=True):
            classes = tag.get('class', [])
            for cls in classes:
                # カウント
                class_counter[cls] = class_counter.get(cls, 0) + 1
        
        # 出現回数でソート
        sorted_classes = sorted(
            class_counter.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # トップ10を表示
        for i, (cls, count) in enumerate(sorted_classes[:10], 1):
            print(f"  {i:2d}. '{cls}' - {count}回")
        
        # === HTMLソースを保存 ===
        print("\n10. HTMLソース保存:")
        with open('coorikuya_source.html', 'w', encoding='utf-8') as f:
            # きれいに整形して保存
            f.write(soup.prettify())
        print("  ✓ 'coorikuya_source.html' に保存しました")
        
        # === スクリーンショット保存 ===
        driver.save_screenshot('coorikuya_screenshot.png')
        print("  ✓ 'coorikuya_screenshot.png' に保存しました")
        
        print("\n" + "="*80)
        print("【分析完了！】")
        print("="*80)
        
    except Exception as e:
        # エラーが発生した場合
        logger.error(f"エラーが発生しました: {e}")
        # 詳細なエラー情報を表示
        import traceback
        traceback.print_exc()
        
    finally:
        # 必ずブラウザを閉じる
        print("\n5秒後にブラウザを閉じます...")
        time.sleep(5)
        driver.quit()
        logger.info("ブラウザを閉じました")


# このファイルが直接実行された場合のみ実行
if __name__ == "__main__":
    # coorikuya.comを分析
    find_specific_elements("https://www.coorikuya.com/")