# ====================================
# ふわふわ大福店シリーズ：クラスと継承の例
# GoogleスタイルDocstring付き
# ====================================

# ① 親子クラス（単一継承）
class Parent:
    """親クラスの例"""
    def greet(self):
        """親クラスの挨拶メソッド"""
        print("こんにちは！私は親クラスです。")

class Child(Parent):
    """親クラスを継承した子クラス"""
    def greet_child(self):
        """子クラス専用の挨拶"""
        print("私は子クラスです！")

# テスト
c = Child()
c.greet()        # 親のメソッド
c.greet_child()  # 子のメソッド


# ② 階層継承（親→子→孫）
class GrandParent:
    """祖父母クラス"""
    def say(self):
        """祖父母の挨拶"""
        print("祖父母クラスです。")

class Parent2(GrandParent):
    """親クラス"""
    def say_parent(self):
        print("親クラスです。")

class Child2(Parent2):
    """子クラス"""
    def say_child(self):
        print("子クラスです。")

# テスト
c2 = Child2()
c2.say()
c2.say_parent()
c2.say_child()


# ③ 多重継承（複数の親を持つ）
class A:
    def hello(self):
        print("Aクラスからこんにちは")

class B:
    def hello(self):
        print("Bクラスからこんにちは")

class C(A, B):
    """AとBを継承（左側優先）"""
    pass

c3 = C()
c3.hello()  # Aが優先される


# ④ __init__（初期化）
class Shop:
    """お店クラスの例"""
    def __init__(self, name):
        """
        インスタンス生成時に名前を初期化

        Args:
            name (str): お店の名前
        """
        self.name = name
        print(f"{self.name}を開店しました！")

shop = Shop("ふわふわ大福店")


# ⑤ super()（親の処理を呼ぶ）
class ParentInit:
    """親クラスの初期化"""
    def __init__(self):
        print("親クラスの初期化")

class ChildInit(ParentInit):
    """子クラスの初期化"""
    def __init__(self):
        super().__init__()  # 親の初期化を呼ぶ
        print("子クラスの初期化")

c_init = ChildInit()


# ⑦ 特殊メソッド
class Daifuku:
    """大福クラス"""
    def __init__(self, flavor):
        """
        Args:
            flavor (str): 大福の味
        """
        self.flavor = flavor

    def __str__(self):
        """文字列表示"""
        return f"🍡 {self.flavor}大福です"

d = Daifuku("あんこ")
print(d)


# ⑧ クラス変数と⑨ インスタンス変数
class Shop2:
    tax_rate = 0.1  # クラス変数（全員で共有）

    def __init__(self, name):
        self.name = name  # インスタンス変数（個別）

s1 = Shop2("もちもち店")
s2 = Shop2("ぴょんぴょん店")
print(f"{s1.name}の税率: {s1.tax_rate}, {s2.name}の税率: {s2.tax_rate}")


# ⑩ メソッド
class Shop3:
    """販売メソッド"""
    def sell(self, num):
        """
        商品を販売する

        Args:
            num (int): 販売する個数
        """
        print(f"🍡 {num}個販売しました！")

s3 = Shop3()
s3.sell(5)


# ⑪ self
class Shop4:
    """selfの例"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        """インスタンス変数を使った挨拶"""
        print(f"{self.name}へようこそ！")

s4 = Shop4("ふわふわ大福店")
s4.greet()


# ⑫ *args, **kwargs（可変長引数）
class Menu:
    """メニュークラス"""
    def show_items(self, *args, **kwargs):
        """
        可変長引数の例

        Args:
            *args: 商品名のタプル
            **kwargs: 商品と価格の辞書
        """
        print("商品リスト:", args)
        print("価格表:", kwargs)

m = Menu()
m.show_items("あんこ", "いちご", "クリーム", あんこ=150, いちご=200)

#oyakotestsimple.py