class WalkingMixin:
    def walk(self):
        return f"{self.name} {self.gait()} forward"
    
class Person(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"
