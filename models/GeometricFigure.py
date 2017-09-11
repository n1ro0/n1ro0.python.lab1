from abc import ABC, abstractmethod

class GeometricFigure(ABC):

    @abstractmethod
    def draw(self):
        pass
