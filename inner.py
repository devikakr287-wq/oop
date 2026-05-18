class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the Inner Class")


outer = Outer()
print(outer.name)

inner = outer.Inner()
print(inner.name)