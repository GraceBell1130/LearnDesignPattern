
# 파이썬은 객체를 생성과 초기화에 __init__과 __new__를 이용하여 객체를 생성
# __new__는 클래스에 정의되어 있지 않으면 알아서 object클래스의 __new__가 호출되어 객체를 생성
# 생성된 객체에 속성을 추가할 때 __init__이 호출

class Singleton (object):
    __uniqueInstance = None
    def __new__(cls):
        if cls.__uniqueInstance is None:
           cls.__uniqueInstance = super().__new__(cls)
        return cls.__uniqueInstance

# classmethod와 staticmethd의 차이점은 매개변수에 cls의 유무에 차이가 있는데
# cls에 있는 경우 class 관련 속성에 접근이 가능하지만 
# cls가 없는 경우 calss 관련 속성에 접근이 불가능하며 단순히 매개변수에 의존하게 된다.
class SingletonLazy ():
    __uniqueInstance = None
    @classmethod
    def getInstace(cls):
        if cls.__uniqueInstance == None:
            cls.__uniqueInstance = Singleton()
        return cls.__uniqueInstance