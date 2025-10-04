"""
====================================
Docstring 作成完全ガイド
0から作る＆書き換える方法
ステップバイステップ
====================================
"""

# ====================================
# STEP 1: 関数を分析する（考えること）
# ====================================

"""
【分析すべき6つのポイント】

1. 目的: この関数は何をするか？
2. 入力: 何を受け取るか？（引数）
3. 出力: 何を返すか？（戻り値）
4. 例外: エラーは起きるか？
5. 副作用: 外部に影響するか？
6. 使い方: どう使うか？（例）
"""

# ----- 例題: この関数を分析しよう -----
def sell_daifuku(quantity, price, discount=0):
    # この関数を分析する
    if quantity <= 0:
        # 数量が0以下ならエラー
        raise ValueError("数量は1以上")
    
    # 小計を計算
    subtotal = quantity * price
    
    # 割引を適用
    total = subtotal * (1 - discount)
    
    # 結果を返す
    return int(total)


"""
【分析結果】

1. 目的: 大福の合計金額を計算する
2. 入力:
   - quantity (int): 個数
   - price (int): 単価
   - discount (float): 割引率（省略可）
3. 出力:
   - int: 割引後の合計金額
4. 例外:
   - ValueError: quantityが0以下の時
5. 副作用: なし
6. 使い方:
   - sell_daifuku(10, 150) → 1500
   - sell_daifuku(10, 150, 0.1) → 1350
"""


# ====================================
# STEP 2: 記法を選ぶ（確認観点）
# ====================================

"""
【記法選択のチェックリスト】

□ プロジェクトの種類は？
  - 個人 → PEP 257
  - チーム → Google
  - データ分析 → NumPy
  - OSS → reST

□ チームの経験は？
  - 初心者が多い → Google
  - 科学者が多い → NumPy
  - ベテラン → reST

□ ツールは何を使う？
  - Sphinx → reST
  - 特になし → Google

□ 既存コードは？
  - 既にスタイルがある → それに合わせる
  - 新規 → Google推奨

結論: 迷ったらGoogle!
"""


# ====================================
# STEP 3-1: PEP 257で書く
# ====================================

"""
【PEP 257 作成手順】

ステップ1: 目的を1文で書く
ステップ2: 動詞で始める
ステップ3: ピリオドで終わる

これで完成!
"""

def sell_daifuku_pep257(quantity, price, discount=0):
    """大福の合計金額を計算する。"""
    # ↑
    # 手順1: 「計算する」という動詞で始める
    # 手順2: 「何を？」→「大福の合計金額を」
    # 手順3: ピリオド . で終わる
    # 
    # これだけ! シンプル!
    
    if quantity <= 0:
        raise ValueError("数量は1以上")
    
    subtotal = quantity * price
    total = subtotal * (1 - discount)
    
    return int(total)


# ====================================
# STEP 3-2: Googleスタイルで書く
# ====================================

"""
【Google 作成手順】

ステップ1: 概要を書く（1行）
ステップ2: 空行を入れる
ステップ3: Args: を書く
  - 各引数を 引数名 (型): 説明 の形式で
  - デフォルト値がある場合は (型, optional)
ステップ4: Returns: を書く
  - 型: 説明 の形式で
ステップ5: Raises: を書く（例外がある場合）
  - 例外名: 発生条件
ステップ6: Examples: を書く（複雑な場合）
"""

def sell_daifuku_google(quantity, price, discount=0):
    """
    大福の合計金額を計算する。
    
    Args:
        quantity (int): 販売する個数
        price (int): 1個あたりの単価（円）
        discount (float, optional): 割引率（0.0〜1.0）。デフォルトは0
    
    Returns:
        int: 割引後の合計金額（円）
    
    Raises:
        ValueError: quantityが0以下の場合
    
    Examples:
        >>> sell_daifuku_google(10, 150)
        1500
        >>> sell_daifuku_google(10, 150, 0.1)
        1350
    """
    # ↑ 完成したdocstring
    # 
    # 手順1: 「大福の合計金額を計算する。」← 概要
    # 手順2: 空行
    # 手順3: Args: セクション
    #   - quantity (int): 説明
    #   - price (int): 説明
    #   - discount (float, optional): 説明 ← optionalを付ける
    # 手順4: Returns: セクション
    #   - int: 説明
    # 手順5: Raises: セクション
    #   - ValueError: 発生条件
    # 手順6: Examples: セクション
    #   - >>> 関数呼び出し
    #   - 期待される結果
    
    if quantity <= 0:
        raise ValueError("数量は1以上")
    
    subtotal = quantity * price
    total = subtotal * (1 - discount)
    
    return int(total)


# ====================================
# STEP 3-3: NumPyスタイルで書く
# ====================================

"""
【NumPy 作成手順】

ステップ1: 概要を書く
ステップ2: 空行
ステップ3: Parameters を書く
  - Parameters の下に -------- (8個以上)
  - 引数名 : 型 の形式
  - 説明を次の行にインデント
ステップ4: Returns を書く
  - Returns の下に ------- (7個以上)
  - 型を書く
  - 説明を次の行にインデント
ステップ5: Raises を書く（例外がある場合）
  - Raises の下に ------ (6個以上)
  - 例外名だけ書く
  - 説明を次の行にインデント
"""

def sell_daifuku_numpy(quantity, price, discount=0):
    """
    大福の合計金額を計算する。
    
    Parameters
    ----------
    quantity : int
        販売する個数
    price : int
        1個あたりの単価（円）
    discount : float, optional
        割引率（0.0〜1.0）。デフォルトは0
    
    Returns
    -------
    int
        割引後の合計金額（円）
    
    Raises
    ------
    ValueError
        quantityが0以下の場合
    
    Examples
    --------
    >>> sell_daifuku_numpy(10, 150)
    1500
    >>> sell_daifuku_numpy(10, 150, 0.1)
    1350
    """
    # ↑ 完成したdocstring
    # 
    # 手順1: 概要
    # 手順2: 空行
    # 手順3: Parameters セクション
    #   - Parameters
    #   - ---------- ← ハイフン8個
    #   - quantity : int ← コロンで型
    #   -     説明 ← インデント4スペース
    # 手順4: Returns セクション
    #   - Returns
    #   - ------- ← ハイフン7個
    #   - int
    #   -     説明
    # 手順5: Raises セクション
    #   - Raises
    #   - ------ ← ハイフン6個
    #   - ValueError
    #   -     説明
    
    if quantity <= 0:
        raise ValueError("数量は1以上")
    
    subtotal = quantity * price
    total = subtotal * (1 - discount)
    
    return int(total)


# ====================================
# STEP 3-4: reSTスタイルで書く
# ====================================

"""
【reST 作成手順】

ステップ1: 概要を書く
ステップ2: 空行
ステップ3: 各引数を2行ずつ書く
  - :param 引数名: 説明
  - :type 引数名: 型
ステップ4: 戻り値を2行で書く
  - :return: 説明
  - :rtype: 型
ステップ5: 例外を1行で書く
  - :raises 例外名: 説明
"""

def sell_daifuku_rest(quantity, price, discount=0):
    """
    大福の合計金額を計算する。
    
    :param quantity: 販売する個数
    :type quantity: int
    :param price: 1個あたりの単価（円）
    :type price: int
    :param discount: 割引率（0.0〜1.0）。デフォルト: 0
    :type discount: float
    :return: 割引後の合計金額（円）
    :rtype: int
    :raises ValueError: quantityが0以下の場合
    """
    # ↑ 完成したdocstring
    # 
    # 手順1: 概要
    # 手順2: 空行
    # 手順3: 各引数を2行ずつ
    #   - :param quantity: 説明
    #   - :type quantity: int
    #   ↑ paramとtypeはセット
    # 手順4: 戻り値を2行で
    #   - :return: 説明
    #   - :rtype: int
    # 手順5: 例外を1行で
    #   - :raises ValueError: 説明
    
    if quantity <= 0:
        raise ValueError("数量は1以上")
    
    subtotal = quantity * price
    total = subtotal * (1 - discount)
    
    return int(total)


# ====================================
# STEP 4: 書き換え実践
# ====================================

"""
【書き換えの流れ】

1. 既存のdocstringを読む
2. 情報を抽出する
   - 概要
   - 引数
   - 戻り値
   - 例外
3. 新しい記法で書き直す
4. 確認する
"""

# ----- 元のdocstring（Google） -----
def calc_original(x, y, z=10):
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
    """
    if y == 0:
        raise ValueError("yは0以外")
    return x / y + z


# ----- ステップ1: 情報を抽出 -----
"""
【抽出した情報】

概要: (x / y) + z を計算する
引数:
  - x (float): 割られる数
  - y (float): 割る数
  - z (float, optional): 加算する数。デフォルト10
戻り値:
  - float: 計算結果
例外:
  - ValueError: yが0の場合
"""


# ----- ステップ2: NumPyに書き換え -----
def calc_to_numpy(x, y, z=10):
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
    """
    # 書き換え手順:
    # 1. 概要はそのまま
    # 2. Args → Parameters + --------
    # 3. x (float) → x : float
    # 4. 説明を次の行に
    # 5. Returns → Returns + -------
    # 6. Raises → Raises + ------
    
    if y == 0:
        raise ValueError("yは0以外")
    return x / y + z


# ----- ステップ3: reSTに書き換え -----
def calc_to_rest(x, y, z=10):
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
    """
    # 書き換え手順:
    # 1. 概要はそのまま
    # 2. Args を削除
    # 3. 各引数を2行ずつ
    #    x (float): 説明
    #    ↓
    #    :param x: 説明
    #    :type x: float
    # 4. Returns を2行に
    #    Returns: float: 説明
    #    ↓
    #    :return: 説明
    #    :rtype: float
    
    if y == 0:
        raise ValueError("yは0以外")
    return x / y + z


# ====================================
# STEP 5: 確認観点チェックリスト
# ====================================

"""
【確認すべき10項目】

□ 1. 三重引用符で囲んだ
  - \"\"\" または ''' を使用
  - 関数定義の直後に配置

□ 2. 概要が明確
  - 1行で何をするか分かる
  - 動詞で始まる
  - ピリオドで終わる

□ 3. 全引数を説明した
  - 引数の数と説明の数が一致
  - デフォルト値を明記

□ 4. 型情報が正確
  - int, float, str, list など
  - 複雑な型も説明（list of int など）

□ 5. 戻り値を説明した
  - 何を返すか明記
  - Noneの場合も書く

□ 6. 例外を記載した
  - 発生する例外を全て
  - 発生条件も明記

□ 7. 使用例がある（複雑な関数の場合）
  - >>> で呼び出し例
  - 期待される結果

□ 8. スペルミスがない
  - 英語のスペルチェック
  - 日本語の誤字チェック

□ 9. 文法が正しい
  - 記法のルールに従っている
  - ハイフンの数が正しい（NumPy）
  - コロンの位置が正しい（reST）

□ 10. help()で確認した
  - help(関数名)で表示
  - 読みやすいか確認
"""


# ====================================
# 確認例: help()で表示してみる
# ====================================

def check_example_google(x, y):
    """
    2つの数を足し算する。
    
    Args:
        x (int): 1つ目の数
        y (int): 2つ目の数
    
    Returns:
        int: x + y の結果
    """
    return x + y

# help(check_example_google) を実行すると...
# 
# Help on function check_example_google:
# 
# check_example_google(x, y)
#     2つの数を足し算する。
#     
#     Args:
#         x (int): 1つ目の数
#         y (int): 2つ目の数
#     
#     Returns:
#         int: x + y の結果
# 
# このように表示される!


# ====================================
# よくある間違いと修正例
# ====================================

"""
【間違い1】引用符の数が違う
"""
def wrong_1():
    "これは1個" # NG: 1個だとただのコメント
    pass

def correct_1():
    """これは3個""" # OK: 3個でdocstring
    pass


"""
【間違い2】位置が違う
"""
"""これは間違い""" # NG: 関数の外
def wrong_2():
    pass

def correct_2():
    """これは正しい""" # OK: 関数の直後
    pass


"""
【間違い3】型の書き方が間違い
"""
def wrong_3(x):
    """
    Args:
        x int: 説明 # NG: カッコがない（Google）
    """
    pass

def correct_3(x):
    """
    Args:
        x (int): 説明 # OK: (型)
    """
    pass


"""
【間違い4】ハイフンの数が違う
"""
def wrong_4(x):
    """
    Parameters
    --- # NG: 少なすぎる
    x : int
    """
    pass

def correct_4(x):
    """
    Parameters
    ---------- # OK: 8個以上
    x : int
        説明
    """
    pass


# ====================================
# まとめ: 作成フローチャート
# ====================================

print("="*60)
print("Docstring作成フローチャート")
print("="*60)
print("""
START
  ↓
1. 関数を分析
  - 何をする？
  - 何を受け取る？
  - 何を返す？
  - エラーは？
  ↓
2. 記法を選ぶ
  - 個人 → PEP 257
  - チーム → Google
  - データ → NumPy
  - Doc → reST
  ↓
3. docstringを書く
  - 概要
  - 引数
  - 戻り値
  - 例外
  ↓
4. 確認する
  - チェックリスト
  - help()で表示
  - 誤字確認
  ↓
5. 完成！
  ↓
END

【所要時間】
- PEP 257: 1分
- Google: 3分
- NumPy: 5分
- reST: 5分
""")