class Toy:
    price = 100

    def get_current_price(self):
        print(f"Current Price: {self.price}")

    # 建立 class method
    @classmethod
    def get_original_price(cls):
        # 透過 cls 可應用 class attribute
        print(f"Original Price: {cls.price}")

car = Toy()
# 修改 instance attribute (price)
car.price = 80
car.get_original_price() # 將會取得 instance attribute (price)
car.get_current_price() # 將會取得 class attribute (price)

# 不用生成 object，可直接使用
Toy.get_original_price() # 同樣可取得 class attribute (price)
Toy.get_current_price() # 會噴錯，因為不是 instance object