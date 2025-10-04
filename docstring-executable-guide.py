"""
====================================
🐰 ふわふわ大福店で学ぶ
Docstring完全実践ガイド

実際に動くコード
====================================

このファイルを実行すると:
✓ 3大スタイルの違いが分かる
✓ help()で結果が確認できる
✓ 書き換え方法が理解できる
✓ 実践的な使い方が身につく
"""

print("="*70)
print("🐰 Docstring実践ガイドを開始します")
print("="*70)

# ====================================
# 第1部: Googleスタイル
# ====================================

print("\n" + "="*70)
print("【第1部】Googleスタイル - 初心者に最適")
print("="*70)

# --------------------------------------------------
# パターン1: 基本形
# --------------------------------------------------
def sell_daifuku(quantity, price):
    """
    大福を販売して合計金額を計算する。
    
    Args:
        quantity (int): 販売する大福の個数
        price (int): 1個あたりの価格（円）
    
    Returns:
        int: 合計金額（円）
    
    Examples:
        >>> sell_daifuku(10, 150)
        1500
    """
    # Args: 引数の説明
    # 形式: 引数名 (型): 説明
    
    # Returns: 戻り値の説明
    # 形式: 型: 説明
    
    # Examples: 使用例（省略可）
    # 形式: >>> 関数呼び出し
    #       期待される結果
    
    return quantity * price


# --------------------------------------------------
# パターン2: 例外を含む
# --------------------------------------------------
def add_stock(current, amount):
    """
    在庫を追加する。
    
    Args:
        current (int): 現在の在庫数
        amount (int): 追加する在庫数
    
    Returns:
        int: 更新後の在庫数
    
    Raises:
        ValueError: amountが負の値の場合
    
    Examples:
        >>> add_stock(100, 50)
        150
    """
    # Raises: 発生する例外
    # 形式: 例外名: 発生条件
    
    # バリデーション（検証処理）
    if amount < 0:
        # 負の値はエラー
        raise ValueError("追加量は0以上を指定してください")
    
    # 在庫を加算
    return current + amount


# --------------------------------------------------
# パターン3: デフォルト引数
# --------------------------------------------------
def calculate_total(price, quantity, tax_rate=0.1):
    """
    税込み合計金額を計算する。
    
    Args:
        price (int): 単価（円）
        quantity (int): 数量
        tax_rate (float, optional): 消費税率。デフォルトは0.1（10%）
    
    Returns:
        int: 税込み合計金額（円）
    
    Note:
        計算結果は整数に丸められます。
    """
    # optional: デフォルト値がある引数
    # 形式: 引数名 (型, optional): 説明。デフォルトは値
    
    # Note: 重要な注意事項
    
    # 小計を計算
    subtotal = price * quantity
    
    # 税込み金額を計算
    total = subtotal * (1 + tax_rate)
    
    # 整数に変換して返す
    return int(total)


# --------------------------------------------------
# パターン4: クラスのdocstring
# --------------------------------------------------
class DaifukuShop:
    """
    大福店クラス。
    
    在庫管理と販売機能を提供する。
    
    Attributes:
        owner_name (str): 店長の名前
        stock (int): 現在の在庫数
        sold (int): 累計販売数
    
    Examples:
        >>> shop = DaifukuShop("うさうさ", 100)
        >>> shop.sell(10)
        True
        >>> shop.stock
        90
    """
    # クラスのdocstring:
    # 1. クラスの簡単な説明
    # 2. Attributes: インスタンス変数の説明
    # 3. Examples: 使用例
    
    def __init__(self, owner_name, stock):
        """
        大福店を初期化する。
        
        Args:
            owner_name (str): 店長の名前
            stock (int): 初期在庫数
        """
        # __init__のdocstring:
        # コンストラクタの引数を説明
        # Returnsは書かない（__init__は何も返さない）
        
        self.owner_name = owner_name  # 店長名を保存
        self.stock = stock            # 在庫数を保存
        self.sold = 0                 # 販売数は0から開始
    
    def sell(self, quantity):
        """
        大福を販売する。
        
        Args:
            quantity (int): 販売する個数
        
        Returns:
            bool: 販売成功ならTrue、在庫不足ならFalse
        """
        # 在庫チェック
        if quantity > self.stock:
            # 在庫不足
            return False
        
        # 在庫を減らす
        self.stock -= quantity
        
        # 販売数を増やす
        self.sold += quantity
        
        # 成功
        return True
    
    def show_info(self):
        """店舗情報を表示する。"""
        # シンプルな関数なら1行でOK
        
        print(f"店長: {self.owner_name}")
        print(f"在庫: {self.stock}個")
        print(f"販売: {self.sold}個")


# --------------------------------------------------
# Googleスタイルの動作確認
# --------------------------------------------------
print("\n【Googleスタイルの例】")
print("-"*70)

# 基本形
result = sell_daifuku(10, 150)
print(f"売上: {result}円")

# 例外を含む
stock = add_stock(100, 50)
print(f"在庫: {stock}個")

# デフォルト引数
total = calculate_total(150, 10)
print(f"税込み: {total}円")

# クラス
shop = DaifukuShop("うさうさ", 100)
shop.sell(10)
shop.show_info()

# help()で確認（コメントアウトを外すと実行）
# print("\n【help()の結果】")
# help(sell_daifuku)


# ====================================
# 第2部: NumPyスタイル
# ====================================

print("\n" + "="*70)
print("【第2部】NumPyスタイル - 科学技術系向け")
print("="*70)

# --------------------------------------------------
# パターン1: 基本形
# --------------------------------------------------
def sell_daifuku_numpy(quantity, price):
    """
    大福を販売して合計金額を計算する。
    
    Parameters
    ----------
    quantity : int
        販売する大福の個数
    price : int
        1個あたりの価格（円）
    
    Returns
    -------
    int
        合計金額（円）
    
    Examples
    --------
    >>> sell_daifuku_numpy(10, 150)
    1500
    """
    # Parameters: 引数の説明
    # Parameters の下に -------- (8個以上のハイフン)
    # 形式: 引数名 : 型
    #         説明（次の行にインデント）
    
    # Returns: 戻り値の説明
    # Returns の下に ------- (7個以上のハイフン)
    # 形式: 型
    #         説明（次の行にインデント）
    
    return quantity * price


# --------------------------------------------------
# パターン2: 複数の戻り値
# --------------------------------------------------
def calculate_stats(sales_list):
    """
    販売統計を計算する。
    
    Parameters
    ----------
    sales_list : list of int
        各日の販売数のリスト
    
    Returns
    -------
    total : int
        合計販売数
    average : float
        平均販売数
    max_sales : int
        最大販売数
    
    Examples
    --------
    >>> calculate_stats([10, 20, 15])
    (45, 15.0, 20)
    """
    # 複数の戻り値:
    # 各戻り値を個別に説明
    # 形式: 戻り値名 : 型
    #         説明
    
    # 合計を計算
    total = sum(sales_list)
    
    # 平均を計算
    average = total / len(sales_list)
    
    # 最大値を取得
    max_sales = max(sales_list)
    
    # タプルで返す
    return total, average, max_sales


# --------------------------------------------------
# パターン3: 例外と注意事項
# --------------------------------------------------
def divide_daifuku(total, people):
    """
    大福を人数で割る。
    
    Parameters
    ----------
    total : int
        大福の総数
    people : int
        分ける人数
    
    Returns
    -------
    float
        1人あたりの個数
    
    Raises
    ------
    ValueError
        peopleが0以下の場合
    
    Notes
    -----
    この関数は小数点以下も返します。
    整数が必要な場合は int() で変換してください。
    
    See Also
    --------
    sell_daifuku_numpy : 大福の販売計算
    """
    # Raises: 例外の説明
    # Raises の下に ------ (6個以上のハイフン)
    # 形式: 例外名
    #         説明
    
    # Notes: 注意事項
    # Notes の下に ----- (5個以上のハイフン)
    # 詳しい説明を書ける
    
    # See Also: 関連関数
    # See Also の下に -------- (8個以上のハイフン)
    # 形式: 関数名 : 簡単な説明
    
    # バリデーション
    if people <= 0:
        raise ValueError("人数は1以上を指定してください")
    
    # 割り算
    return total / people


# --------------------------------------------------
# パターン4: クラスのdocstring
# --------------------------------------------------
class PremiumDaifukuShop:
    """
    プレミアム大福店クラス。
    
    基本的な販売機能に加えて、VIP会員管理機能を提供する。
    
    Attributes
    ----------
    owner_name : str
        店長の名前
    stock : int
        現在の在庫数
    vip_count : int
        VIP会員数
    
    Methods
    -------
    sell(quantity)
        大福を販売する
    add_vip(count)
        VIP会員を追加する
    
    Examples
    --------
    >>> shop = PremiumDaifukuShop("もちもち", 100, 5)
    >>> shop.sell(10)
    True
    """
    # クラスのdocstring（NumPy版）:
    # 1. クラスの説明
    # 2. Attributes: 属性の説明
    # 3. Methods: メソッドの一覧
    # 4. Examples: 使用例
    
    def __init__(self, owner_name, stock, vip_count):
        """
        プレミアム大福店を初期化する。
        
        Parameters
        ----------
        owner_name : str
            店長の名前
        stock : int
            初期在庫数
        vip_count : int
            初期VIP会員数
        """
        self.owner_name = owner_name
        self.stock = stock
        self.vip_count = vip_count
    
    def sell(self, quantity):
        """
        大福を販売する。
        
        Parameters
        ----------
        quantity : int
            販売する個数
        
        Returns
        -------
        bool
            販売成功ならTrue、在庫不足ならFalse
        """
        if quantity > self.stock:
            return False
        self.stock -= quantity
        return True
    
    def add_vip(self, count=1):
        """
        VIP会員を追加する。
        
        Parameters
        ----------
        count : int, optional
            追加する会員数。デフォルトは1
        """
        # optional: デフォルト値がある引数
        self.vip_count += count


# --------------------------------------------------
# NumPyスタイルの動作確認
# --------------------------------------------------
print("\n【NumPyスタイルの例】")
print("-"*70)

# 基本形
result = sell_daifuku_numpy(10, 150)
print(f"売上: {result}円")

# 複数の戻り値
total, avg, max_val = calculate_stats([10, 20, 15])
print(f"合計: {total}, 平均: {avg}, 最大: {max_val}")

# 例外と注意事項
per_person = divide_daifuku(100, 3)
print(f"1人あたり: {per_person:.2f}個")

# クラス
premium_shop = PremiumDaifukuShop("もちもち", 100, 5)
premium_shop.sell(10)
premium_shop.add_vip(2)
print(f"VIP会員: {premium_shop.vip_count}名")


# ====================================
# 第3部: reSTスタイル
# ====================================

print("\n" + "="*70)
print("【第3部】reSTスタイル - Sphinx用")
print("="*70)

# --------------------------------------------------
# パターン1: 基本形
# --------------------------------------------------
def sell_daifuku_rest(quantity, price):
    """
    大福を販売して合計金額を計算する。
    
    :param quantity: 販売する大福の個数
    :type quantity: int
    :param price: 1個あたりの価格（円）
    :type price: int
    :return: 合計金額（円）
    :rtype: int
    
    .. code-block:: python
    
       >>> sell_daifuku_rest(10, 150)
       1500
    """
    # :param 引数名: 引数の説明
    # :type 引数名: 引数の型
    # param と type はセットで書く
    
    # :return: 戻り値の説明
    # :rtype: 戻り値の型
    # return と rtype もセット
    
    # .. code-block:: python
    #    使用例のコードブロック
    
    return quantity * price


# --------------------------------------------------
# パターン2: 例外を含む
# --------------------------------------------------
def add_stock_rest(current, amount):
    """
    在庫を追加する。
    
    :param current: 現在の在庫数
    :type current: int
    :param amount: 追加する在庫数
    :type amount: int
    :return: 更新後の在庫数
    :rtype: int
    :raises ValueError: amountが負の値の場合
    """
    # :raises 例外名: 発生条件
    # 1行で書く
    
    if amount < 0:
        raise ValueError("追加量は0以上を指定してください")
    
    return current + amount


# --------------------------------------------------
# パターン3: デフォルト引数と警告
# --------------------------------------------------
def calculate_discount(price, rate=0.1):
    """
    割引後の価格を計算する。
    
    :param price: 元の価格（円）
    :type price: int
    :param rate: 割引率（デフォルト: 0.1）
    :type rate: float
    :return: 割引後の価格（円）
    :rtype: int
    
    .. note::
       rateは0.0〜1.0の範囲で指定してください。
    
    .. warning::
       rateが範囲外の場合、予期しない結果になります。
    """
    # デフォルト引数:
    # 説明に「デフォルト: 値」を書く
    
    # .. note:: 注意事項
    # .. warning:: 警告
    # これらはSphinxで特別な表示になる
    
    return int(price * (1 - rate))


# --------------------------------------------------
# パターン4: クラスのdocstring
# --------------------------------------------------
class VIPDaifukuShop:
    """
    VIP専門大福店クラス。
    
    プレミアム機能に加えて、コンシェルジュサービスを提供する。
    
    :ivar owner_name: 店長の名前
    :vartype owner_name: str
    :ivar stock: 現在の在庫数
    :vartype stock: int
    :ivar concierge_count: コンシェルジュの人数
    :vartype concierge_count: int
    """
    # クラスのdocstring（reST版）:
    # :ivar 変数名: インスタンス変数の説明
    # :vartype 変数名: インスタンス変数の型
    
    def __init__(self, owner_name, stock, concierge_count):
        """
        VIP専門大福店を初期化する。
        
        :param owner_name: 店長の名前
        :type owner_name: str
        :param stock: 初期在庫数
        :type stock: int
        :param concierge_count: コンシェルジュの人数
        :type concierge_count: int
        """
        self.owner_name = owner_name
        self.stock = stock
        self.concierge_count = concierge_count
    
    def sell_vip(self, quantity):
        """
        VIP限定販売を行う。
        
        :param quantity: 販売する個数
        :type quantity: int
        :return: 販売成功ならTrue
        :rtype: bool
        """
        if quantity > self.stock:
            return False
        self.stock -= quantity
        return True


# --------------------------------------------------
# reSTスタイルの動作確認
# --------------------------------------------------
print("\n【reSTスタイルの例】")
print("-"*70)

# 基本形
result = sell_daifuku_rest(10, 150)
print(f"売上: {result}円")

# 例外を含む
stock = add_stock_rest(100, 50)
print(f"在庫: {stock}個")

# デフォルト引数
discounted = calculate_discount(1000, 0.2)
print(f"割引後: {discounted}円")

# クラス
vip_shop = VIPDaifukuShop("ぴょんぴょん", 100, 3)
vip_shop.sell_vip(10)
print(f"VIP店在庫: {vip_shop.stock}個")


# ====================================
# 第4部: 書き換え実践
# ====================================

print("\n" + "="*70)
print("【第4部】書き換え実践 - 同じ関数を3スタイルで")
print("="*70)

# --------------------------------------------------
# ビフォー: docstringなし
# --------------------------------------------------
def calc_before(x, y, z=10):
    # 何をする関数？
    if y == 0:
        raise ValueError("y cannot be zero")
    return x / y + z


# --------------------------------------------------
# アフター1: Google版
# --------------------------------------------------
def calc_google(x, y, z=10):
    """
    (x / y) + z を計算する。
    
    Args:
        x (float): 割られる数
        y (float): 割る数
        z (float, optional): 加算する数。デフォルトは10
    
    Returns:
        float: 計算結果
    
    Raises:
        ValueError: yが0の場合
    
    Examples:
        >>> calc_google(20, 2, 5)
        15.0
    """
    if y == 0:
        raise ValueError("y cannot be zero")
    return x / y + z


# --------------------------------------------------
# アフター2: NumPy版
# --------------------------------------------------
def calc_numpy(x, y, z=10):
    """
    (x / y) + z を計算する。
    
    Parameters
    ----------
    x : float
        割られる数
    y : float
        割る数
    z : float, optional
        加算する数。デフォルトは10
    
    Returns
    -------
    float
        計算結果
    
    Raises
    ------
    ValueError
        yが0の場合
    
    Examples
    --------
    >>> calc_numpy(20, 2, 5)
    15.0
    """
    if y == 0:
        raise ValueError("y cannot be zero")
    return x / y + z


# --------------------------------------------------
# アフター3: reST版
# --------------------------------------------------
def calc_rest(x, y, z=10):
    """
    (x / y) + z を計算する。
    
    :param x: 割られる数
    :type x: float
    :param y: 割る数
    :type y: float
    :param z: 加算する数（デフォルト: 10）
    :type z: float
    :return: 計算結果
    :rtype: float
    :raises ValueError: yが0の場合
    
    .. code-block:: python
    
       >>> calc_rest(20, 2, 5)
       15.0
    """
    if y == 0:
        raise ValueError("y cannot be zero")
    return x / y + z


# --------------------------------------------------
# 書き換え結果の確認
# --------------------------------------------------
print("\n【書き換え結果の比較】")
print("-"*70)

# ビフォー
result_before = calc_before(20, 2, 5)
print(f"ビフォー: {result_before}")

# Google版
result_google = calc_google(20, 2, 5)
print(f"Google版: {result_google}")

# NumPy版
result_numpy = calc_numpy(20, 2, 5)
print(f"NumPy版: {result_numpy}")

# reST版
result_rest = calc_rest(20, 2, 5)
print(f"reST版: {result_rest}")


# ====================================
# 第5部: チートシート
# ====================================

print("\n" + "="*70)
print("【第5部】チートシート - 書き方まとめ")
print("="*70)

print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Googleスタイル テンプレート          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def 関数名(引数1, 引数2=デフォルト値):
    \"\"\"
    関数の簡潔な説明（1行）
    
    Args:
        引数1 (型): 説明
        引数2 (型, optional): 説明。デフォルトは値
    
    Returns:
        型: 説明
    
    Raises:
        例外名: 説明
    
    Examples:
        >>> 関数名(値1, 値2)
        結果
    \"\"\"


┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  NumPyスタイル テンプレート            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def 関数名(引数1, 引数2=デフォルト値):
    \"\"\"
    関数の簡潔な説明
    
    Parameters
    ----------
    引数1 : 型
        説明
    引数2 : 型, optional
        説明。デフォルトは値
    
    Returns
    -------
    型
        説明
    
    Raises
    ------
    例外名
        説明
    
    Examples
    --------
    >>> 関数名(値1, 値2)
    結果
    \"\"\"


┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  reSTスタイル テンプレート             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def 関数名(引数1, 引数2=デフォルト値):
    \"\"\"
    関数の簡潔な説明
    
    :param 引数1: 説明
    :type 引数1: 型
    :param 引数2: 説明（デフォルト: 値）
    :type 引数2: 型
    :return: 説明
    :rtype: 型
    :raises 例外名: 説明
    \"\"\"
""")

print("\n" + "="*70)
print("【使い分けガイド】")
print("="*70)
print("""
Googleスタイル → 初心者・チーム開発・Web開発
NumPyスタイル  → データ分析・科学計算・研究
reSTスタイル   → 公式ドキュメント・大規模OSS

迷ったら → Googleスタイル！
""")

print("\n" + "="*70)
print("実行完了！help()で各関数を確認してみましょう")
print("例: help(sell_daifuku)")
print("="*70)