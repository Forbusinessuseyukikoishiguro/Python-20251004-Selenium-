# """
# ====================================
# 5大記法 書き換え実践
# デバッグプリント完全版
# 何をしているか完全に見える
# ====================================
# """

# ====================================
# パターン1: PEP 257 から書き換えhelp( calc_original_pep)
# ====================================

print("=" * 70)
print("【パターン1】PEP 257 → 他の4記法へ書き換え")
print("=" * 70)


# ----- 元: PEP 257 -----
def calc_original_pep(x, y):
    """2つの数を足し算する。"""
    # 【この関数の目的】
    # - 2つの整数を受け取る
    # - 足し算する
    # - 結果を返す

    print(f"  [PEP257元] 実行: {x} + {y}")  # デバッグ
    result = x + y  # 計算
    print(f"  [PEP257元] 結果: {result}")  # デバッグ
    return result


print("\n--- PEP 257 → Google への書き換え ---")


def calc_pep_to_google(x, y):
    """
    2つの数を足し算する。

    Args:
        x (int): 1つ目の数
        y (int): 2つ目の数

    Returns:
        int: x + y の結果
    """
    # 【書き換え内容】
    # PEP 257: """2つの数を足し算する。"""
    #    ↓
    # Google: 概要 + Args + Returns

    print(f"  [Google版] 実行: {x} + {y}")
    print(f"  [Google版] 引数x={x}, y={y} を足し算")
    result = x + y
    print(f"  [Google版] 結果: {result}")
    print(f"  [書き換え成功] PEP 257 → Google")
    return result


print("\n--- PEP 257 → NumPy への書き換え ---")


def calc_pep_to_numpy(x, y):
    """
    2つの数を足し算する。

    Parameters
    ----------
    x : int
        1つ目の数
    y : int
        2つ目の数

    Returns
    -------
    int
        x + y の結果
    """
    # 【書き換え内容】
    # PEP 257: """2つの数を足し算する。"""
    #    ↓
    # NumPy: 概要 + Parameters + ハイフン + Returns

    print(f"  [NumPy版] 実行: {x} + {y}")
    print(f"  [NumPy版] Parameters形式で引数を記述")
    result = x + y
    print(f"  [NumPy版] 結果: {result}")
    print(f"  [書き換え成功] PEP 257 → NumPy")
    return result


print("\n--- PEP 257 → reST への書き換え ---")


def calc_pep_to_rest(x, y):
    """
    2つの数を足し算する。

    :param x: 1つ目の数
    :type x: int
    :param y: 2つ目の数
    :type y: int
    :return: x + y の結果
    :rtype: int
    """
    # 【書き換え内容】
    # PEP 257: """2つの数を足し算する。"""
    #    ↓
    # reST: 概要 + :param/:type + :return/:rtype

    print(f"  [reST版] 実行: {x} + {y}")
    print(f"  [reST版] :param と :type で引数を2行ずつ記述")
    result = x + y
    print(f"  [reST版] 結果: {result}")
    print(f"  [書き換え成功] PEP 257 → reST")
    return result


print("\n--- PEP 257 → Epytext への書き換え ---")


def calc_pep_to_epytext(x, y):
    """
    2つの数を足し算する。

    @param x: 1つ目の数
    @type x: int
    @param y: 2つ目の数
    @type y: int
    @return: x + y の結果
    @rtype: int
    """
    # 【書き換え内容】
    # PEP 257: """2つの数を足し算する。"""
    #    ↓
    # Epytext: 概要 + @param/@type + @return/@rtype

    print(f"  [Epytext版] 実行: {x} + {y}")
    print(f"  [Epytext版] @ 記法で記述（レガシー）")
    result = x + y
    print(f"  [Epytext版] 結果: {result}")
    print(f"  [書き換え成功] PEP 257 → Epytext")
    return result


# テスト実行
print("\n▼ パターン1のテスト実行")
x, y = 10, 5
print(f"入力値: x={x}, y={y}\n")

print("1-0. 元のPEP 257:")
calc_original_pep(x, y)

print("\n1-1. PEP 257 → Google:")
calc_pep_to_google(x, y)

print("\n1-2. PEP 257 → NumPy:")
calc_pep_to_numpy(x, y)

print("\n1-3. PEP 257 → reST:")
calc_pep_to_rest(x, y)

print("\n1-4. PEP 257 → Epytext:")
calc_pep_to_epytext(x, y)


# ====================================
# パターン2: Google から書き換え
# ====================================

print("\n\n" + "=" * 70)
print("【パターン2】Google → 他の4記法へ書き換え")
print("=" * 70)


# ----- 元: Google -----
def calc_original_google(x, y, z=10):
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
    # 【この関数の目的】
    # - xをyで割る
    # - zを足す
    # - yが0ならエラー

    print(f"  [Google元] 実行: ({x} / {y}) + {z}")
    if y == 0:
        print(f"  [Google元] エラー: yが0です")
        raise ValueError("yは0以外")

    result = x / y + z
    print(f"  [Google元] 結果: {result}")
    return result


print("\n--- Google → PEP 257 への書き換え ---")


def calc_google_to_pep(x, y, z=10):
    """(x / y) + z を計算する。"""
    # 【書き換え内容】
    # Google: 概要 + Args + Returns + Raises
    #    ↓
    # PEP 257: 概要のみ（詳細情報は削除）

    print(f"  [PEP257版] 実行: ({x} / {y}) + {z}")
    print(f"  [PEP257版] 簡略化（引数・戻り値の説明を削除）")

    if y == 0:
        print(f"  [PEP257版] エラー: yが0です")
        raise ValueError("yは0以外")

    result = x / y + z
    print(f"  [PEP257版] 結果: {result}")
    print(f"  [書き換え成功] Google → PEP 257")
    return result


print("\n--- Google → NumPy への書き換え ---")


def calc_google_to_numpy(x, y, z=10):
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
    # 【書き換え内容】
    # Google: Args: + Returns: + Raises:
    #    ↓
    # NumPy: Parameters + ハイフン + Returns + Raises

    print(f"  [NumPy版] 実行: ({x} / {y}) + {z}")
    print(f"  [NumPy版] Args→Parameters, ハイフン追加, インデント形式")

    if y == 0:
        print(f"  [NumPy版] エラー: yが0です")
        raise ValueError("yは0以外")

    result = x / y + z
    print(f"  [NumPy版] 結果: {result}")
    print(f"  [書き換え成功] Google → NumPy")
    return result


print("\n--- Google → reST への書き換え ---")


def calc_google_to_rest(x, y, z=10):
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
    # 【書き換え内容】
    # Google: x (float): 説明
    #    ↓
    # reST: :param x: 説明 + :type x: float（2行に分割）

    print(f"  [reST版] 実行: ({x} / {y}) + {z}")
    print(f"  [reST版] 各引数を :param と :type の2行で記述")

    if y == 0:
        print(f"  [reST版] エラー: yが0です")
        raise ValueError("yは0以外")

    result = x / y + z
    print(f"  [reST版] 結果: {result}")
    print(f"  [書き換え成功] Google → reST")
    return result


print("\n--- Google → Epytext への書き換え ---")


def calc_google_to_epytext(x, y, z=10):
    """
    (x / y) + z を計算する。

    @param x: 割られる数
    @type x: float
    @param y: 割る数
    @type y: float
    @param z: 加算する数（デフォルト: 10）
    @type z: float
    @return: 計算結果
    @rtype: float
    @raise ValueError: yが0の場合
    """
    # 【書き換え内容】
    # reST: :param, :type, :return, :rtype, :raises
    #    ↓
    # Epytext: @param, @type, @return, @rtype, @raise

    print(f"  [Epytext版] 実行: ({x} / {y}) + {z}")
    print(f"  [Epytext版] : を @ に置き換え")

    if y == 0:
        print(f"  [Epytext版] エラー: yが0です")
        raise ValueError("yは0以外")

    result = x / y + z
    print(f"  [Epytext版] 結果: {result}")
    print(f"  [書き換え成功] Google → Epytext")
    return result


# テスト実行
print("\n▼ パターン2のテスト実行")
x2, y2, z2 = 20.0, 4.0, 10.0
print(f"入力値: x={x2}, y={y2}, z={z2}\n")

print("2-0. 元のGoogle:")
calc_original_google(x2, y2, z2)

print("\n2-1. Google → PEP 257:")
calc_google_to_pep(x2, y2, z2)

print("\n2-2. Google → NumPy:")
calc_google_to_numpy(x2, y2, z2)

print("\n2-3. Google → reST:")
calc_google_to_rest(x2, y2, z2)

print("\n2-4. Google → Epytext:")
calc_google_to_epytext(x2, y2, z2)


# ====================================
# パターン3: NumPy から書き換え
# ====================================

print("\n\n" + "=" * 70)
print("【パターン3】NumPy → 他の4記法へ書き換え")
print("=" * 70)


# ----- 元: NumPy -----
def calc_original_numpy(values):
    """
    リストの統計を計算する。

    Parameters
    ----------
    values : list of float
        数値のリスト

    Returns
    -------
    mean : float
        平均値
    total : float
        合計値
    """
    # 【この関数の目的】
    # - リストを受け取る
    # - 平均と合計を計算
    # - タプルで返す

    print(f"  [NumPy元] 実行: values={values}")
    total = sum(values)
    mean = total / len(values)
    print(f"  [NumPy元] 合計={total}, 平均={mean}")
    return mean, total


print("\n--- NumPy → PEP 257 への書き換え ---")


def calc_numpy_to_pep(values):
    """リストの統計を計算する。"""
    # 【書き換え内容】
    # NumPy: Parameters + ハイフン + Returns
    #    ↓
    # PEP 257: 概要のみ

    print(f"  [PEP257版] 実行: values={values}")
    print(f"  [PEP257版] 詳細削除（概要のみ残す）")

    total = sum(values)
    mean = total / len(values)
    print(f"  [PEP257版] 合計={total}, 平均={mean}")
    print(f"  [書き換え成功] NumPy → PEP 257")
    return mean, total


print("\n--- NumPy → Google への書き換え ---")


def calc_numpy_to_google(values):
    """
    リストの統計を計算する。

    Args:
        values (list of float): 数値のリスト

    Returns:
        tuple: (mean, total) のタプル
            mean (float): 平均値
            total (float): 合計値
    """
    # 【書き換え内容】
    # NumPy: values : list of float (次の行に説明)
    #    ↓
    # Google: values (list of float): 説明（1行にまとめる）

    print(f"  [Google版] 実行: values={values}")
    print(f"  [Google版] ハイフン削除, 1行形式に変換")

    total = sum(values)
    mean = total / len(values)
    print(f"  [Google版] 合計={total}, 平均={mean}")
    print(f"  [書き換え成功] NumPy → Google")
    return mean, total


print("\n--- NumPy → reST への書き換え ---")


def calc_numpy_to_rest(values):
    """
    リストの統計を計算する。

    :param values: 数値のリスト
    :type values: list of float
    :return: (mean, total) のタプル
    :rtype: tuple
    """
    # 【書き換え内容】
    # NumPy: values : list of float (ハイフン + インデント)
    #    ↓
    # reST: :param values: + :type values: (2行形式)

    print(f"  [reST版] 実行: values={values}")
    print(f"  [reST版] ハイフン削除, :param/:type形式")

    total = sum(values)
    mean = total / len(values)
    print(f"  [reST版] 合計={total}, 平均={mean}")
    print(f"  [書き換え成功] NumPy → reST")
    return mean, total


print("\n--- NumPy → Epytext への書き換え ---")


def calc_numpy_to_epytext(values):
    """
    リストの統計を計算する。

    @param values: 数値のリスト
    @type values: list of float
    @return: (mean, total) のタプル
    @rtype: tuple
    """
    # 【書き換え内容】
    # reST: :param, :type, :return, :rtype
    #    ↓
    # Epytext: @param, @type, @return, @rtype

    print(f"  [Epytext版] 実行: values={values}")
    print(f"  [Epytext版] : を @ に置き換え")

    total = sum(values)
    mean = total / len(values)
    print(f"  [Epytext版] 合計={total}, 平均={mean}")
    print(f"  [書き換え成功] NumPy → Epytext")
    return mean, total


# テスト実行
print("\n▼ パターン3のテスト実行")
values = [10.0, 20.0, 30.0]
print(f"入力値: values={values}\n")

print("3-0. 元のNumPy:")
calc_original_numpy(values)

print("\n3-1. NumPy → PEP 257:")
calc_numpy_to_pep(values)

print("\n3-2. NumPy → Google:")
calc_numpy_to_google(values)

print("\n3-3. NumPy → reST:")
calc_numpy_to_rest(values)

print("\n3-4. NumPy → Epytext:")
calc_numpy_to_epytext(values)


# ====================================
# 最終まとめ
# ====================================

print("\n\n" + "=" * 70)
print("【最終まとめ】全パターンの書き換え完了")
print("=" * 70)
print(
    """
✅ パターン1: PEP 257 → 他の4記法（完了）
✅ パターン2: Google → 他の4記法（完了）
✅ パターン3: NumPy → 他の4記法（完了）

【書き換えのポイント】
- PEP 257: 概要のみ（最小限）
- Google: Args/Returns形式（読みやすい）
- NumPy: ハイフン + インデント（表形式）
- reST: :記法 + 2行ずつ（Sphinx用）
- Epytext: @記法（レガシー）

【デバッグプリントで確認できたこと】
✓ 各関数が何をしているか
✓ 書き換え前後の違い
✓ 実行結果が正しいか
✓ 書き換えが成功したか

新人エンジニアの皆さん、頑張ってください！
"""
)
