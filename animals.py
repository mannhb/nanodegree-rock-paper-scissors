class Dog:
    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()

class Retreiver(Dog):
    origin = "West"

    def speak(self):
        print("Yahoo!")
        
