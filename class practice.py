
class Smartphone:
    """
    Smartphone Class
    """
    smartphone_count = 0
    
    def __init__(self, brand, informations):
        self._brand = brand
        self._informations = informations
        Smartphone.smartphone_count += 1

    def __str__(self):
        return f'str : {self._brand} - {self._informations}'

    def __repr__(self):
        return f'repr : {self._brand} - {self._informations}'

    def detail_info(self):
        print(f'Current Id : {id(self)}')
        print(f'Smartphone Detail Info : {self._brand} {self._informations.get("price")}')

    def get_price(self):
        return f'Before Smartphone Price -> brand : {self._brand}, price : {self._informations.get("price")}'

    def get_price_culc(self):
        return f'After Smartphone Price -> brand : {self._brand}, price : {self._informations.get("price") * Smartphone.price_per_raise}'

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        return 'Succeed! price increased.'

    @staticmethod
    def is_iphone(inst):
        if inst._brand == 'Iphone':
            return f'OK! This Smartphone is {inst._brand}.'
        return 'Sorry. This Smartphone is not Iphone.'
    
    
Smartphone1 = Smartphone('Iphone', {'color' : 'White', 'price': 10000})
Smartphone2 = Smartphone('Galaxy', {'color' : 'Black', 'price': 8000})
# 기본 정보
print(Smartphone1)
print(Smartphone2)

Smartphone1._informations
Smartphone2._informations

print(Smartphone1.get_price())
print(Smartphone2.get_price())

# 가격 인상(클래스 메소드 미사용)
# 이렇게 직접 접근은 좋지 않아요
Smartphone.price_per_raise = 1.2

# 가격 정보
print(Smartphone1.get_price_culc())
print(Smartphone2.get_price_culc())

# 가격 인상
Smartphone.raise_price(1.6)

# 가격 정보
print(Smartphone1.get_price_culc())
print(Smartphone2.get_price_culc())

def is_iphone(inst):
    if inst._brand == 'Iphone':
        return f'OK! This Smartphone is {inst._brand}.'
    return 'Sorry. This Smartphone is not Iphone.'

print(is_iphone(Smartphone2))

print('Static : ', Smartphone.is_iphone(Smartphone1))
print('Static : ', Smartphone.is_iphone(Smartphone2))