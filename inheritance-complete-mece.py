"""
====================================
🐰 ふわふわ大福店で学ぶPython継承
完全ガイド - 1行ずつコメント付き
====================================

このコードで学べること:
1. 単一継承（親 → 子）
2. 階層継承（親 → 子 → 孫）
3. 多重継承（親A + 親B → 子）
4. それぞれの使い分け
"""

# ====================================
# 第1部: 単一継承（最もシンプル）
# ====================================
print("=" * 70)
print("【第1部】単一継承 - 1つの親から1つの子へ")
print("=" * 70)

# 親クラスの定義
class DaifukuShop:
    """
    大福店の基本クラス（親クラス）
    
    役割: すべての大福店の基本機能を定義
    """
    
    def __init__(self, owner_name, stock):
        """
        コンストラクタ - インスタンス作成時に実行
        
        引数:
            owner_name (str): 店長の名前
            stock (int): 初期在庫数
        """
        # インスタンス変数の初期化
        self.owner_name = owner_name  # 店長名を保存
        self.stock = stock  # 在庫数を保存
        self.sold = 0  # 累計販売数を0で初期化
        
        # 開店メッセージを表示
        print(f"🏪 {self.owner_name}店長の基本店舗を開店しました")
    
    def sell(self, quantity):
        """
        大福を販売するメソッド（親クラスの基本機能）
        
        引数:
            quantity (int): 販売する個数
        
        戻り値:
            bool: 販売成功ならTrue、失敗ならFalse
        """
        # 在庫が足りるかチェック
        if quantity > self.stock:
            # 在庫不足の場合
            print(f"❌ 在庫不足！（在庫: {self.stock}個）")
            return False  # 失敗を返す
        
        # 在庫を減らす
        self.stock -= quantity
        
        # 累計販売数を増やす
        self.sold += quantity
        
        # 販売成功メッセージ
        print(f"💰 {quantity}個販売しました（残り在庫: {self.stock}個）")
        
        # 成功を返す
        return True
    
    def show_info(self):
        """店舗情報を表示するメソッド"""
        # 区切り線を表示
        print(f"\n{'='*50}")
        
        # 店舗情報を表示
        print(f"🏪 {self.owner_name}店長の店")
        print(f"📦 在庫: {self.stock}個")
        print(f"💰 累計販売: {self.sold}個")
        
        # 区切り線を表示
        print(f"{'='*50}\n")


# 子クラスの定義（単一継承）
class PremiumDaifukuShop(DaifukuShop):
    """
    プレミアム大福店クラス（子クラス）
    
    継承: DaifukuShopを継承（単一継承）
    役割: 基本店舗の機能 + プレミアム機能
    """
    
    def __init__(self, owner_name, stock, vip_count):
        """
        コンストラクタ（子クラス）
        
        引数:
            owner_name (str): 店長名
            stock (int): 初期在庫
            vip_count (int): VIP会員数（子クラス固有）
        """
        # super()で親クラスのコンストラクタを呼び出す
        # これにより owner_name, stock, sold が初期化される
        super().__init__(owner_name, stock)
        
        # 子クラス固有のインスタンス変数
        self.vip_count = vip_count  # VIP会員数を保存
        
        # プレミアム店舗のメッセージ
        print(f"✨ プレミアム機能追加（VIP会員: {vip_count}名）")
    
    def sell_premium(self, quantity):
        """
        プレミアム販売（子クラス固有のメソッド）
        
        特徴: 通常価格の1.5倍で販売
        
        引数:
            quantity (int): 販売個数
        
        戻り値:
            bool: 販売成功ならTrue
        """
        # 親クラスのsellメソッドを呼び出す
        result = super().sell(quantity)
        
        # 販売に成功した場合
        if result:
            # プレミアム価格を計算（150円 × 1.5 = 225円）
            premium_price = quantity * 225
            
            # プレミアム販売メッセージ
            print(f"✨ プレミアム価格: ¥{premium_price}")
        
        # 結果を返す
        return result
    
    def add_vip(self, count=1):
        """
        VIP会員を追加（子クラス固有のメソッド）
        
        引数:
            count (int): 追加する会員数（デフォルト1）
        """
        # VIP会員数を増やす
        self.vip_count += count
        
        # 追加メッセージ
        print(f"👑 VIP会員が{count}名増えました（合計: {self.vip_count}名）")
    
    def show_info(self):
        """
        店舗情報を表示（オーバーライド）
        
        親のメソッドを拡張してVIP情報を追加
        """
        # 親クラスのshow_infoを呼び出す
        # これで基本情報（店長名、在庫、販売数）が表示される
        super().show_info()
        
        # 子クラス固有の情報を追加
        print(f"👑 VIP会員: {self.vip_count}名")
        print(f"{'='*50}\n")


# ==========================================
# 単一継承のデモンストレーション
# ==========================================
print("\n【単一継承のデモ】")
print("-" * 70)

# 親クラスのインスタンスを作成
basic_shop = DaifukuShop("うさうさ", 20)  # 基本店舗

# 親クラスのメソッドを使用
basic_shop.sell(5)  # 5個販売
basic_shop.show_info()  # 情報表示

# 子クラスのインスタンスを作成
premium_shop = PremiumDaifukuShop("もちもち", 30, 5)  # プレミアム店舗

# 親から継承したメソッドを使用
premium_shop.sell(3)  # 親のsellメソッド

# 子クラス固有のメソッドを使用
premium_shop.sell_premium(2)  # 子のsell_premiumメソッド
premium_shop.add_vip(2)  # 子のadd_vipメソッド

# オーバーライドしたメソッドを使用
premium_shop.show_info()  # 親+子の情報を表示


# ====================================
# 第2部: 階層継承（親 → 子 → 孫）
# ====================================
print("\n" + "=" * 70)
print("【第2部】階層継承 - 親から子、子から孫へ")
print("=" * 70)

# 孫クラスの定義（階層継承）
class VIPDaifukuShop(PremiumDaifukuShop):
    """
    VIP専門大福店クラス（孫クラス）
    
    継承: PremiumDaifukuShopを継承（階層継承）
    継承チェーン: DaifukuShop → PremiumDaifukuShop → VIPDaifukuShop
    役割: プレミアム店舗の機能 + VIP専門機能
    """
    
    def __init__(self, owner_name, stock, vip_count, concierge_count):
        """
        コンストラクタ（孫クラス）
        
        引数:
            owner_name (str): 店長名
            stock (int): 初期在庫
            vip_count (int): VIP会員数
            concierge_count (int): コンシェルジュ数（孫クラス固有）
        """
        # super()で親クラス（PremiumDaifukuShop）のコンストラクタを呼び出す
        # これにより祖父クラスの初期化も自動的に行われる
        super().__init__(owner_name, stock, vip_count)
        
        # 孫クラス固有のインスタンス変数
        self.concierge_count = concierge_count  # コンシェルジュ数を保存
        
        # VIP専門店のメッセージ
        print(f"👑 VIP専門店機能追加（コンシェルジュ: {concierge_count}名）")
    
    def sell_vip_exclusive(self, quantity):
        """
        VIP限定販売（孫クラス固有のメソッド）
        
        特徴: プレミアム価格の2倍で販売（超高級）
        
        引数:
            quantity (int): 販売個数
        
        戻り値:
            bool: 販売成功ならTrue
        """
        # 親クラス（PremiumDaifukuShop）のsell_premiumメソッドを呼び出す
        result = super().sell_premium(quantity)
        
        # 販売に成功した場合
        if result:
            # VIP限定価格を計算（225円 × 2 = 450円）
            vip_price = quantity * 450
            
            # VIP限定販売メッセージ
            print(f"👑 VIP限定価格: ¥{vip_price}")
            print(f"📞 コンシェルジュがお届けします")
        
        # 結果を返す
        return result
    
    def concierge_service(self):
        """
        コンシェルジュサービス（孫クラス固有のメソッド）
        """
        # サービス内容を表示
        print(f"\n👔 コンシェルジュサービス")
        print(f"   専任スタッフ: {self.concierge_count}名")
        print(f"   VIP会員様: {self.vip_count}名")
        print(f"   お一人様あたり専任コンシェルジュが対応します\n")
    
    def show_info(self):
        """
        店舗情報を表示（さらにオーバーライド）
        
        親と祖父のメソッドを拡張してコンシェルジュ情報を追加
        """
        # 親クラスのshow_infoを呼び出す
        # これで祖父クラスと親クラスの情報が表示される
        super().show_info()
        
        # 孫クラス固有の情報を追加
        print(f"👔 コンシェルジュ: {self.concierge_count}名")
        print(f"{'='*50}\n")


# ==========================================
# 階層継承のデモンストレーション
# ==========================================
print("\n【階層継承のデモ】")
print("-" * 70)

# 孫クラスのインスタンスを作成
vip_shop = VIPDaifukuShop("ぴょんぴょん", 40, 10, 3)

# 祖父クラスから継承したメソッド
vip_shop.sell(2)  # 基本販売

# 親クラスから継承したメソッド
vip_shop.sell_premium(3)  # プレミアム販売
vip_shop.add_vip(1)  # VIP追加

# 孫クラス固有のメソッド
vip_shop.sell_vip_exclusive(1)  # VIP限定販売
vip_shop.concierge_service()  # コンシェルジュサービス

# オーバーライドしたメソッド（全情報表示）
vip_shop.show_info()

# 継承チェーンを確認
print("継承チェーン:")
for i, cls in enumerate(VIPDaifukuShop.__mro__, 1):
    # MRO（メソッド解決順序）を表示
    # __mro__はメソッドを探す順番を示す
    print(f"  {i}. {cls.__name__}")
print()


# ====================================
# 第3部: 多重継承（複数の親から）
# ====================================
print("\n" + "=" * 70)
print("【第3部】多重継承 - 複数の親クラスから機能を組み合わせ")
print("=" * 70)

# 親クラスA: 基本店舗機能
class ShopBase:
    """
    店舗の基本機能（多重継承用の親A）
    
    役割: 店舗としての基本的な販売機能
    """
    
    def __init__(self, owner_name, stock):
        """
        コンストラクタ
        
        引数:
            owner_name (str): 店長名
            stock (int): 在庫数
        """
        # インスタンス変数を初期化
        self.owner_name = owner_name  # 店長名
        self.stock = stock  # 在庫数
        self.sold = 0  # 累計販売数
        
        # 初期化メッセージ
        print(f"🏪 店舗機能: {owner_name}店長")
    
    def sell(self, quantity):
        """
        基本的な販売処理
        
        引数:
            quantity (int): 販売個数
        
        戻り値:
            bool: 販売成功ならTrue
        """
        # 在庫チェック
        if quantity > self.stock:
            # 在庫不足
            print(f"❌ 在庫不足")
            return False
        
        # 在庫を減らす
        self.stock -= quantity
        
        # 累計販売数を増やす
        self.sold += quantity
        
        # 販売メッセージ
        print(f"💰 {quantity}個販売")
        
        # 成功を返す
        return True


# 親クラスB: オンライン機能
class OnlineServiceMixin:
    """
    オンライン注文機能（多重継承用の親B）
    
    役割: オンラインでの注文受付機能
    注意: ミックスイン（機能追加専用クラス）
    """
    
    def __init__(self):
        """コンストラクタ"""
        # オンライン注文数を初期化
        self.online_orders = 0  # オンライン注文の累計
        
        # 初期化メッセージ
        print(f"🌐 オンライン機能: システム起動")
    
    def receive_online_order(self, customer, quantity):
        """
        オンライン注文を受け付ける
        
        引数:
            customer (str): 顧客名
            quantity (int): 注文個数
        """
        # 注文番号を増やす
        self.online_orders += 1
        
        # 注文受付メッセージ
        print(f"🌐 オンライン注文 #{self.online_orders}")
        print(f"   顧客: {customer}様")
        print(f"   数量: {quantity}個")


# 親クラスC: 配達機能
class DeliveryServiceMixin:
    """
    配達サービス機能（多重継承用の親C）
    
    役割: 商品の配達機能
    注意: ミックスイン（機能追加専用クラス）
    """
    
    def __init__(self):
        """コンストラクタ"""
        # 配達回数を初期化
        self.deliveries = 0  # 配達の累計回数
        
        # 初期化メッセージ
        print(f"🚚 配達機能: サービス開始")
    
    def deliver(self, address):
        """
        商品を配達する
        
        引数:
            address (str): 配達先住所
        """
        # 配達回数を増やす
        self.deliveries += 1
        
        # 配達メッセージ
        print(f"🚚 配達 #{self.deliveries}: {address}へ配達中")


# 親クラスD: 会員機能
class MembershipServiceMixin:
    """
    会員サービス機能（多重継承用の親D）
    
    役割: 会員の登録と管理
    注意: ミックスイン（機能追加専用クラス）
    """
    
    def __init__(self):
        """コンストラクタ"""
        # 会員リストを初期化
        self.members = []  # 会員名のリスト
        
        # 初期化メッセージ
        print(f"💳 会員機能: システム起動")
    
    def register_member(self, name):
        """
        会員を登録する
        
        引数:
            name (str): 会員名
        """
        # 会員リストに追加
        self.members.append(name)
        
        # 登録メッセージ
        print(f"💳 {name}様を会員登録（会員数: {len(self.members)}名）")
    
    def is_member(self, name):
        """
        会員かどうかチェック
        
        引数:
            name (str): チェックする名前
        
        戻り値:
            bool: 会員ならTrue
        """
        # 会員リストに名前があるかチェック
        return name in self.members


# 子クラス: 多重継承で4つの機能を統合
class HybridDaifukuShop(ShopBase, OnlineServiceMixin, DeliveryServiceMixin, MembershipServiceMixin):
    """
    ハイブリッド大福店（多重継承）
    
    継承元:
    - ShopBase（店舗機能）
    - OnlineServiceMixin（オンライン機能）
    - DeliveryServiceMixin（配達機能）
    - MembershipServiceMixin（会員機能）
    
    役割: すべての機能を統合した最先端店舗
    """
    
    def __init__(self, owner_name, stock):
        """
        コンストラクタ（多重継承）
        
        注意: すべての親クラスを初期化する必要がある
        
        引数:
            owner_name (str): 店長名
            stock (int): 初期在庫
        """
        # 開始メッセージ
        print(f"\n{'='*60}")
        print(f"🌟 ハイブリッド店舗を起動中...")
        print(f"{'='*60}")
        
        # 各親クラスを初期化（順番に呼び出す）
        ShopBase.__init__(self, owner_name, stock)  # 親A
        OnlineServiceMixin.__init__(self)  # 親B
        DeliveryServiceMixin.__init__(self)  # 親C
        MembershipServiceMixin.__init__(self)  # 親D
        
        # 完了メッセージ
        print(f"✅ すべての機能が利用可能です")
        print(f"{'='*60}\n")
    
    def process_order(self, customer, quantity, address, is_member=False):
        """
        統合注文処理（すべての機能を組み合わせ）
        
        処理の流れ:
        1. オンライン注文受付（OnlineServiceMixin）
        2. 販売処理（ShopBase）
        3. 配達処理（DeliveryServiceMixin）
        4. 会員登録（MembershipServiceMixin）
        
        引数:
            customer (str): 顧客名
            quantity (int): 注文個数
            address (str): 配達先住所
            is_member (bool): 会員かどうか
        """
        # 処理開始メッセージ
        print(f"\n{'='*60}")
        print(f"📝 注文処理開始: {customer}様")
        print(f"{'='*60}")
        
        # 1. オンライン注文受付（親Bのメソッド）
        self.receive_online_order(customer, quantity)
        
        # 2. 販売処理（親Aのメソッド）
        if self.sell(quantity):
            # 販売成功の場合
            
            # 3. 配達処理（親Cのメソッド）
            self.deliver(address)
            
            # 4. 会員登録処理（親Dのメソッド）
            if is_member and not self.is_member(customer):
                # 会員で、まだ登録されていない場合
                self.register_member(customer)
            
            # 成功メッセージ
            print(f"✅ 注文処理完了")
        else:
            # 販売失敗の場合
            print(f"❌ 注文処理失敗")
        
        # 処理終了メッセージ
        print(f"{'='*60}\n")
    
    def show_all_stats(self):
        """すべての統計情報を表示"""
        # タイトル
        print(f"\n{'='*60}")
        print(f"📊 ハイブリッド店舗 総合統計")
        print(f"{'='*60}")
        
        # 店舗情報（親Aから）
        print(f"🏪 店長: {self.owner_name}")
        print(f"📦 在庫: {self.stock}個")
        print(f"💰 累計販売: {self.sold}個")
        
        # オンライン情報（親Bから）
        print(f"🌐 オンライン注文: {self.online_orders}件")
        
        # 配達情報（親Cから）
        print(f"🚚 配達回数: {self.deliveries}回")
        
        # 会員情報（親Dから）
        print(f"💳 会員数: {len(self.members)}名")
        
        # 区切り線
        print(f"{'='*60}\n")


# ==========================================
# 多重継承のデモンストレーション
# ==========================================
print("\n【多重継承のデモ】")
print("-" * 70)

# ハイブリッド店舗を作成
hybrid = HybridDaifukuShop("ふわふわ", 50)

# すべての機能を使った注文処理
hybrid.process_order("田中太郎", 5, "東京都渋谷区", is_member=True)
hybrid.process_order("佐藤花子", 3, "東京都新宿区", is_member=True)
hybrid.process_order("鈴木一郎", 4, "東京都港区", is_member=False)

# 総合統計を表示
hybrid.show_all_stats()

# MRO（メソッド解決順序）を確認
print("多重継承のMRO（メソッド解決順序）:")
for i, cls in enumerate(HybridDaifukuShop.__mro__, 1):
    # どの順番でメソッドを探すかを表示
    print(f"  {i}. {cls.__name__}")
print()


# ====================================
# 第4部: 3つの継承の比較まとめ
# ====================================
print("\n" + "=" * 70)
print("【第4部】3つの継承パターンの比較まとめ")
print("=" * 70)

print("""
┌──────────────────────────────────────────────────────────┐
│ 1. 単一継承（最もシンプル・推奨）                           │
├──────────────────────────────────────────────────────────┤
│ 構造:   親 → 子                                            │
│ 特徴:   - 1つの親から1つの子                               │
│         - 最もシンプルで理解しやすい                        │
│         - メソッド解決が明確                                │
│ 使う時: - 基本機能を少し拡張したい                          │
│         - is-a関係が明確                                   │
│ 例:     DaifukuShop → PremiumDaifukuShop                  │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ 2. 階層継承（段階的な拡張）                                 │
├──────────────────────────────────────────────────────────┤
│ 構造:   祖父 → 父 → 子                                     │
│ 特徴:   - 親から子、子から孫へと続く                        │
│         - 段階的に機能を追加                                │
│         - 2-3階層が推奨                                     │
│ 使う時: - 段階的に特化させたい                              │
│         - カテゴリーが明確                                  │
│ 例:     DaifukuShop → Premium → VIP                       │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ 3. 多重継承（機能の組み合わせ）                             │
├──────────────────────────────────────────────────────────┤
│ 構造:   親A + 親B + 親C → 子                               │
│ 特徴:   - 複数の親から機能を継承                            │
│         - 独立した機能を組み合わせ                          │
│         - 複雑になりやすい                                  │
│ 使う時: - 独立した複数の機能が必要                          │
│         - ミックスインパターン                              │
│ 例:     Shop + Online + Delivery → Hybrid                 │
└──────────────────────────────────────────────────────────┘
""")

# 推奨される使用頻度
print("推奨される使用頻度:")
print("  単一継承: ★★★★★ (90% のケースで使用)")
print("  階層継承: ★★★☆☆ (状況に応じて使用)")
print("  多重継承: ★★☆☆☆ (慎重に使用)")
print()

# 判断基準
print("どれを使うか迷ったら:")
print("  1. まず単一継承を検討")
print("  2. 段階的な拡張が必要なら階層継承（2-3階層まで）")
print("  3. 独立した機能の組み合わせなら多重継承（慎重に）")
print()

print("=" * 70)
print("🎉 すべてのデモンストレーション完了！")
print("=" * 70)
