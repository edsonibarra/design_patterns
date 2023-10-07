from decorators.abs_decorators import AbsDecorator


class Vinyl(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', Vinyl'
    
    @property
    def cost(self):
        return self.car.cost + 500.00
    