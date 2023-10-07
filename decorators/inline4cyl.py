from decorators.abs_decorators import AbsDecorator


class Red(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', inline 4 cylinder'
    
    @property
    def cost(self):
        return self.car.cost + 500.00
