import React, { useState } from 'react';
import { ChevronDown, ChevronRight, Users, Star, Sparkles } from 'lucide-react';

const InheritanceGuide = () => {
  const [activeSection, setActiveSection] = useState('single');
  const [expandedCode, setExpandedCode] = useState({});

  const toggleCode = (id) => {
    setExpandedCode(prev => ({...prev, [id]: !prev[id]}));
  };

  const CodeBlock = ({ id, title, lines, explanation }) => (
    <div className="mb-4 border border-pink-200 rounded-lg overflow-hidden bg-white">
      <button
        onClick={() => toggleCode(id)}
        className="w-full px-4 py-3 bg-pink-50 hover:bg-pink-100 flex items-center justify-between transition-colors"
      >
        <span className="font-semibold text-pink-800">{title}</span>
        {expandedCode[id] ? <ChevronDown size={20} /> : <ChevronRight size={20} />}
      </button>
      {expandedCode[id] && (
        <div className="p-4">
          <div className="bg-gray-900 text-green-400 p-4 rounded-lg mb-3 overflow-x-auto">
            <pre className="text-sm font-mono whitespace-pre">
              {lines.map((line, i) => (
                <div key={i} className="hover:bg-gray-800 px-2 -mx-2">
                  {line}
                </div>
              ))}
            </pre>
          </div>
          <div className="bg-blue-50 p-3 rounded-lg border-l-4 border-blue-400">
            <p className="text-sm text-gray-700 whitespace-pre-line">{explanation}</p>
          </div>
        </div>
      )}
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 to-purple-50 p-6">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-xl shadow-lg p-8 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <span className="text-4xl">🐰</span>
            <h1 className="text-3xl font-bold text-gray-800">
              Python継承 完全ガイド
            </h1>
          </div>
          <p className="text-gray-600 mb-4">
            プログラミング初心者のための、やさしい継承の教科書
          </p>
          <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 rounded">
            <p className="text-sm font-semibold text-yellow-800">
              💡 継承とは? → 親の機能を子供が受け継ぐこと!
            </p>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
          {[
            { id: 'single', icon: '👤', label: '単一継承', color: 'green' },
            { id: 'multi', icon: '👨‍👩‍👧', label: '階層継承', color: 'blue' },
            { id: 'multiple', icon: '👨‍👩‍👧‍👦', label: '多重継承', color: 'purple' }
          ].map(section => (
            <button
              key={section.id}
              onClick={() => setActiveSection(section.id)}
              className={`px-6 py-3 rounded-lg font-semibold transition-all whitespace-nowrap ${
                activeSection === section.id
                  ? `bg-${section.color}-500 text-white shadow-lg scale-105`
                  : 'bg-white text-gray-600 hover:bg-gray-50'
              }`}
            >
              <span className="mr-2">{section.icon}</span>
              {section.label}
            </button>
          ))}
        </div>

        {/* Section 1: 単一継承 */}
        {activeSection === 'single' && (
          <div className="bg-white rounded-xl shadow-lg p-8">
            <div className="flex items-center gap-3 mb-6">
              <Star className="text-green-500" size={32} />
              <h2 className="text-2xl font-bold text-gray-800">
                単一継承 - 一番簡単な継承!
              </h2>
            </div>

            <div className="bg-green-50 p-6 rounded-lg mb-6">
              <h3 className="font-bold text-green-800 mb-3">📖 イメージ図</h3>
              <div className="text-center py-6">
                <div className="inline-block bg-green-500 text-white px-6 py-3 rounded-lg mb-4">
                  親クラス (DaifukuShop)<br/>
                  <span className="text-sm">基本の大福店</span>
                </div>
                <div className="text-3xl my-2">↓</div>
                <div className="inline-block bg-green-600 text-white px-6 py-3 rounded-lg">
                  子クラス (PremiumDaifukuShop)<br/>
                  <span className="text-sm">プレミアム大福店</span>
                </div>
              </div>
              <p className="text-center text-gray-700 mt-4">
                子クラスは親クラスの全機能 + 新機能を持つ!
              </p>
            </div>

            <CodeBlock
              id="parent-class"
              title="ステップ1: 親クラスを作る"
              lines={[
                '# 親クラスの定義',
                'class DaifukuShop:',
                '    """大福店の基本クラス"""',
                '    ',
                '    def __init__(self, owner_name, stock):',
                '        # self = このインスタンス(このお店)自身',
                '        self.owner_name = owner_name  # 店長名を保存',
                '        self.stock = stock            # 在庫数を保存',
                '        self.sold = 0                 # 販売数は0から',
                '        print(f"🏪 {owner_name}店長の店を開店!")',
                '    ',
                '    def sell(self, quantity):',
                '        """大福を販売するメソッド"""',
                '        if quantity > self.stock:',
                '            print("❌ 在庫不足!")',
                '            return False',
                '        ',
                '        self.stock -= quantity  # 在庫を減らす',
                '        self.sold += quantity   # 販売数を増やす',
                '        print(f"💰 {quantity}個売れた!")',
                '        return True'
              ]}
              explanation={`【一行ずつ解説】

class DaifukuShop:
→ 「DaifukuShop」という名前のクラス(設計図)を作る

def __init__(self, owner_name, stock):
→ __init__ = 初期化メソッド(お店を作る時に実行される)
→ self = このお店自身
→ owner_name = 店長の名前
→ stock = 在庫の数

self.owner_name = owner_name
→ 引数でもらった店長名を、このお店の変数として保存

def sell(self, quantity):
→ sell = 販売するメソッド(機能)
→ quantity = 売る個数

if quantity > self.stock:
→ もし売る個数が在庫より多かったら...
→ エラーを出して終了

self.stock -= quantity
→ 在庫から売った分を引く
→ -= は「引き算して代入」の意味`}
            />

            <CodeBlock
              id="child-class"
              title="ステップ2: 子クラスを作る (継承!)"
              lines={[
                'class PremiumDaifukuShop(DaifukuShop):',
                '    """プレミアム大福店 - 親を継承!"""',
                '    ',
                '    def __init__(self, owner_name, stock, vip_count):',
                '        # super() = 親クラスを呼び出す魔法の言葉',
                '        super().__init__(owner_name, stock)',
                '        ',
                '        # 子クラス独自の変数',
                '        self.vip_count = vip_count',
                '        print(f"✨ VIP会員: {vip_count}名")',
                '    ',
                '    def sell_premium(self, quantity):',
                '        """プレミアム販売 - 子クラス独自の機能!"""',
                '        # 親のsellメソッドを使う',
                '        result = super().sell(quantity)',
                '        ',
                '        if result:',
                '            price = quantity * 225  # 高級価格',
                '            print(f"✨ プレミアム価格: ¥{price}")',
                '        return result'
              ]}
              explanation={`【継承の仕組み】

class PremiumDaifukuShop(DaifukuShop):
→ カッコの中に親クラス名を書く!
→ これで「DaifukuShopを継承します」という意味

super().__init__(owner_name, stock)
→ super() = 親クラスのこと
→ 親の__init__を呼ぶ = 親の初期化処理を実行
→ これで owner_name と stock が設定される

self.vip_count = vip_count
→ 子クラス独自の変数を追加
→ 親にはない、プレミアム店だけの情報

def sell_premium(self, quantity):
→ 子クラス独自のメソッド(機能)を追加
→ 親のsellに加えて、sell_premiumも使える!

result = super().sell(quantity)
→ 親のsellメソッドを呼んで使う
→ 継承してるから親のメソッドが使える!`}
            />

            <CodeBlock
              id="single-usage"
              title="ステップ3: 使ってみる!"
              lines={[
                '# 親クラスのインスタンスを作る',
                'basic = DaifukuShop("うさうさ", 20)',
                'basic.sell(5)',
                '',
                '# 子クラスのインスタンスを作る',
                'premium = PremiumDaifukuShop("もちもち", 30, 5)',
                'premium.sell(3)         # 親から継承したメソッド',
                'premium.sell_premium(2) # 子クラス独自のメソッド'
              ]}
              explanation={`【使い方の解説】

basic = DaifukuShop("うさうさ", 20)
→ 親クラスのインスタンス(お店)を作る
→ "うさうさ"店長、在庫20個でスタート

premium = PremiumDaifukuShop("もちもち", 30, 5)
→ 子クラスのインスタンス(お店)を作る
→ VIP会員5名の情報も追加

premium.sell(3)
→ 子クラスだけど、親のメソッドが使える!
→ これが継承の力!

premium.sell_premium(2)
→ 子クラス独自のメソッドも使える
→ 親の機能 + 子の機能 = 両方使える!`}
            />

            <div className="bg-green-50 p-6 rounded-lg mt-6">
              <h3 className="font-bold text-green-800 mb-3">✅ 単一継承のポイント</h3>
              <ul className="space-y-2 text-gray-700">
                <li>• 一番シンプルで理解しやすい</li>
                <li>• 90%のケースはこれで十分</li>
                <li>• 親の機能を全部使える + 新機能も追加できる</li>
                <li>• 迷ったらまずこれを使う!</li>
              </ul>
            </div>
          </div>
        )}

        {/* Section 2: 階層継承 */}
        {activeSection === 'multi' && (
          <div className="bg-white rounded-xl shadow-lg p-8">
            <div className="flex items-center gap-3 mb-6">
              <Users className="text-blue-500" size={32} />
              <h2 className="text-2xl font-bold text-gray-800">
                階層継承 - 親→子→孫と続く継承
              </h2>
            </div>

            <div className="bg-blue-50 p-6 rounded-lg mb-6">
              <h3 className="font-bold text-blue-800 mb-3">📖 イメージ図</h3>
              <div className="text-center py-6">
                <div className="inline-block bg-blue-300 text-white px-6 py-3 rounded-lg mb-4">
                  祖父クラス (DaifukuShop)<br/>
                  <span className="text-sm">基本店</span>
                </div>
                <div className="text-3xl my-2">↓</div>
                <div className="inline-block bg-blue-500 text-white px-6 py-3 rounded-lg mb-4">
                  父クラス (PremiumDaifukuShop)<br/>
                  <span className="text-sm">プレミアム店</span>
                </div>
                <div className="text-3xl my-2">↓</div>
                <div className="inline-block bg-blue-700 text-white px-6 py-3 rounded-lg">
                  孫クラス (VIPDaifukuShop)<br/>
                  <span className="text-sm">VIP専門店</span>
                </div>
              </div>
              <p className="text-center text-gray-700 mt-4">
                段階的に機能を追加していく!
              </p>
            </div>

            <CodeBlock
              id="grandchild-class"
              title="孫クラスを作る"
              lines={[
                'class VIPDaifukuShop(PremiumDaifukuShop):',
                '    """VIP専門店 - プレミアム店を継承!"""',
                '    ',
                '    def __init__(self, owner_name, stock, vip_count, concierge):',
                '        # 親(PremiumDaifukuShop)の__init__を呼ぶ',
                '        # すると自動的に祖父(DaifukuShop)も初期化される!',
                '        super().__init__(owner_name, stock, vip_count)',
                '        ',
                '        # 孫クラス独自の変数',
                '        self.concierge = concierge',
                '        print(f"👑 コンシェルジュ: {concierge}名")',
                '    ',
                '    def sell_vip_exclusive(self, quantity):',
                '        """VIP限定販売 - 孫クラス独自の機能!"""',
                '        result = super().sell_premium(quantity)',
                '        if result:',
                '            price = quantity * 450  # 超高級',
                '            print(f"👑 VIP限定: ¥{price}")',
                '        return result'
              ]}
              explanation={`【階層継承の仕組み】

class VIPDaifukuShop(PremiumDaifukuShop):
→ プレミアム店(父)を継承する
→ すると祖父の機能も自動的に受け継ぐ!

super().__init__(owner_name, stock, vip_count)
→ 父のPremiumDaifukuShopの__init__を呼ぶ
→ 父の中でさらに祖父の__init__が呼ばれる
→ つまり: 孫 → 父 → 祖父 の順に初期化される

self.concierge = concierge
→ 孫クラス独自の変数

result = super().sell_premium(quantity)
→ 父のsell_premiumメソッドを呼ぶ
→ 父の中で祖父のsellが呼ばれる
→ 3世代の連鎖!

【継承の連鎖】
祖父: owner_name, stock, sell()
父: 祖父の全部 + vip_count, sell_premium()
孫: 父の全部 + concierge, sell_vip_exclusive()

孫は全部使える!`}
            />

            <CodeBlock
              id="multi-usage"
              title="孫クラスを使ってみる"
              lines={[
                'vip = VIPDaifukuShop("ぴょん", 40, 10, 3)',
                '',
                'vip.sell(2)              # 祖父から継承',
                'vip.sell_premium(3)      # 父から継承',
                'vip.sell_vip_exclusive(1) # 孫独自'
              ]}
              explanation={`vip.sell(2)
→ 祖父クラス(DaifukuShop)のメソッド
→ 孫でも使える!

vip.sell_premium(3)
→ 父クラス(PremiumDaifukuShop)のメソッド
→ 孫でも使える!

vip.sell_vip_exclusive(1)
→ 孫クラス独自のメソッド

つまり、孫は3世代全部の機能が使える!
祖父の機能 + 父の機能 + 孫の機能 = 全部!`}
            />

            <div className="bg-blue-50 p-6 rounded-lg mt-6">
              <h3 className="font-bold text-blue-800 mb-3">⚠️ 注意点</h3>
              <ul className="space-y-2 text-gray-700">
                <li>• 階層は2-3階層までがおすすめ</li>
                <li>• 深すぎると複雑になる</li>
                <li>• super()の連鎖を理解する</li>
              </ul>
            </div>
          </div>
        )}

        {/* Section 3: 多重継承 */}
        {activeSection === 'multiple' && (
          <div className="bg-white rounded-xl shadow-lg p-8">
            <div className="flex items-center gap-3 mb-6">
              <Sparkles className="text-purple-500" size={32} />
              <h2 className="text-2xl font-bold text-gray-800">
                多重継承 - 複数の親から継承
              </h2>
            </div>

            <div className="bg-purple-50 p-6 rounded-lg mb-6">
              <h3 className="font-bold text-purple-800 mb-3">📖 イメージ図</h3>
              <div className="text-center py-6">
                <div className="flex justify-center gap-4 mb-4">
                  <div className="bg-purple-400 text-white px-4 py-3 rounded-lg text-sm">
                    親A<br/>店舗機能
                  </div>
                  <div className="bg-purple-400 text-white px-4 py-3 rounded-lg text-sm">
                    親B<br/>オンライン
                  </div>
                  <div className="bg-purple-400 text-white px-4 py-3 rounded-lg text-sm">
                    親C<br/>配達
                  </div>
                  <div className="bg-purple-400 text-white px-4 py-3 rounded-lg text-sm">
                    親D<br/>会員
                  </div>
                </div>
                <div className="text-3xl my-2">↓</div>
                <div className="inline-block bg-purple-700 text-white px-6 py-3 rounded-lg">
                  子クラス (HybridDaifukuShop)<br/>
                  <span className="text-sm">全機能統合!</span>
                </div>
              </div>
              <p className="text-center text-gray-700 mt-4">
                複数の親の機能を全部組み合わせる!
              </p>
            </div>

            <CodeBlock
              id="multiple-parents"
              title="4つの親クラスを作る"
              lines={[
                '# 親A: 店舗機能',
                'class ShopBase:',
                '    def __init__(self, owner_name, stock):',
                '        self.owner_name = owner_name',
                '        self.stock = stock',
                '',
                '# 親B: オンライン機能',
                'class OnlineServiceMixin:',
                '    def __init__(self):',
                '        self.online_orders = 0',
                '',
                '# 親C: 配達機能',
                'class DeliveryServiceMixin:',
                '    def __init__(self):',
                '        self.deliveries = 0',
                '',
                '# 親D: 会員機能',
                'class MembershipServiceMixin:',
                '    def __init__(self):',
                '        self.members = []'
              ]}
              explanation={`4つの独立した機能を作る

親A (ShopBase):
→ 店舗としての基本機能

親B (OnlineServiceMixin):
→ オンライン注文の機能
→ Mixin = 機能追加専用クラス

親C (DeliveryServiceMixin):
→ 配達サービスの機能

親D (MembershipServiceMixin):
→ 会員管理の機能

それぞれ独立した機能
= 組み合わせ自由!`}
            />

            <CodeBlock
              id="hybrid-class"
              title="4つを統合した子クラス"
              lines={[
                'class HybridDaifukuShop(ShopBase, ',
                '                        OnlineServiceMixin,',
                '                        DeliveryServiceMixin,',
                '                        MembershipServiceMixin):',
                '    """ハイブリッド店 - 4つの親を継承!"""',
                '    ',
                '    def __init__(self, owner_name, stock):',
                '        # 全ての親を初期化する必要がある!',
                '        ShopBase.__init__(self, owner_name, stock)',
                '        OnlineServiceMixin.__init__(self)',
                '        DeliveryServiceMixin.__init__(self)',
                '        MembershipServiceMixin.__init__(self)',
                '        print("✅ 全機能OK!")'
              ]}
              explanation={`【多重継承の書き方】

class HybridDaifukuShop(親A, 親B, 親C, 親D):
→ カッコの中に複数の親をカンマ区切りで書く!
→ これで4つ全部の機能を継承

def __init__(self, owner_name, stock):
→ 全ての親を初期化する必要がある!

親A.__init__(self, owner_name, stock)
→ 親Aを直接呼んで初期化

親B.__init__(self)
→ 親Bを直接呼んで初期化

注意: super()じゃなくて親名.__init__()を使う!
なぜなら複数の親があるから

結果:
→ 店舗 + オンライン + 配達 + 会員
→ 全部の機能が使える!`}
            />

            <div className="bg-purple-50 p-6 rounded-lg mt-6">
              <h3 className="font-bold text-purple-800 mb-3">⚠️ 注意点</h3>
              <ul className="space-y-2 text-gray-700">
                <li>• 一番複雑なパターン</li>
                <li>• 慎重に使う必要がある</li>
                <li>• 全ての親を初期化すること</li>
                <li>• 本当に必要な時だけ使う</li>
              </ul>
            </div>
          </div>
        )}

        {/* Summary */}
        <div className="bg-gradient-to-r from-pink-500 to-purple-500 text-white rounded-xl shadow-lg p-8 mt-6">
          <h3 className="text-2xl font-bold mb-4">🎯 まとめ</h3>
          <div className="space-y-3">
            <div className="bg-white bg-opacity-20 p-4 rounded-lg">
              <p className="font-semibold">単一継承 ★★★★★</p>
              <p className="text-sm">一番簡単! 迷ったらこれ!</p>
            </div>
            <div className="bg-white bg-opacity-20 p-4 rounded-lg">
              <p className="font-semibold">階層継承 ★★★☆☆</p>
              <p className="text-sm">段階的に機能追加したい時</p>
            </div>
            <div className="bg-white bg-opacity-20 p-4 rounded-lg">
              <p className="font-semibold">多重継承 ★★☆☆☆</p>
              <p className="text-sm">複雑! 本当に必要な時だけ</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InheritanceGuide;