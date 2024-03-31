class Person:
    def __init__(self,name) -> None:
        self.name=name

        
    def talk(self):
        print('Talk')

Yousuf=Person("Yousuf Khan")
Yousuf.talk()
print(Yousuf.name)