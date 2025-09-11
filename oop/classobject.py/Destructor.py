class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} destroyed")

# create objects
d1 = Demo("A")
d2 = Demo("B")

# delete one explicitly
del d1

print("End of program")
