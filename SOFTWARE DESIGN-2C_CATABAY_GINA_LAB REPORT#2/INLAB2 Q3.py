class MyAge:
    x = 21
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __repr__ (self):
        return 'MyAge(21 = ' + str(self.x) + '-16-' + self.y + ')'
myObject = MyAge(11, "2001")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())

