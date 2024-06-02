# Class method
# 帶有 cls 參數，代表 class 自身
# object 可以使用，但無須生成 object 也能直接使用

class Toy:
    price = 100

    # instance method
    def get_current_price(self): 
        print(f"Current Price: {self.price}")

    # 建立 class method
    @classmethod #Default定義裝飾器 
    def get_original_price(cls):
        # 透過 cls 可應用 class attribute
        print(f"Original Price: {cls.price}")

car = Toy()
# 修改 instance attribute (price)
car.price = 80
car.get_original_price() # 將會取得 class attribute (price)
car.get_current_price() # 將會取得 instance attribute (price)
# 不用生成 object，可直接使用
Toy.get_original_price() # 因為是class method 所以可直接取得 class attribute (price)
Toy.get_current_price() # 會噴錯，因為get_current_price是實例方法，必須通過實例來調用，不能直接通過類別來調用。


# Static method
# 不帶 self 或 cls 參數
#class 和 object 都可以直接使用

class Person:
    # 建立 static method
    @staticmethod #Default定義裝飾器
    def say_hello():
        print("Hello World!")

# Class 可直接使用
Person.say_hello()

# Object 也可使用
john = Person()
john.say_hello()