"""型宣言をした変数に違う型の値を入れる"""
num: int = 1
name: str = '1'

num = name

print(num, type(num))