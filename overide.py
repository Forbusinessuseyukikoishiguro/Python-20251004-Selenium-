# class Parent:
#     def greet(self):
#         print("こんにちは、親クラスです！")

# class Child(Parent):
#     def greet(self):  # 親の greet を上書き
#         print("こんにちは、子クラスです！")

# c = Child()
# c.greet()

class Parent:
    def greet(self):
        print("こんにちは、親クラスです！")

class Child(Parent):
    def greet(self):
        print("子クラスの挨拶前処理")
        super().greet()  # 親クラスのメソッドを呼ぶ
        print("子クラスの挨拶後処理")

c = Child()
c.greet()
