from abc import *

class IObserver(ABC):
    @abstractmethod
    def update(self, temp :float, humidity :float, pressure :float):
        pass
    ''' Observer에서 데이터를 가져오는 pull 방식 
    @abstractmethod
    def update(self):
        pass
    '''
