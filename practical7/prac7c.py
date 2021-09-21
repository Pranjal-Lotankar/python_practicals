'''Create a class called Numbers, which has a single class attribute called
MULTIPLIER, and a constructor which takes the parameters x and y (these should
all be numbers).
i. Write a method called add which returns the sum of the attributes x and y.
ii. Write a class method called multiply, which takes a single number
parameter a and returns the product of a and MULTIPLIER.
iii. Write a static method called subtract, which takes two number parameters, b
and c, and returns b - c.
iv. Write a method called value which returns a tuple containing the values of x
and y. Make this method into a property, and write a setter and a deleter for
manipulating the values of x and y.'''

class Numbers:

    # MULTIPLIER = 3.5

    def init(self, x, y):
        self.x = x
        self.y = y
        self.__value = ''

    def add(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y

    @classmethod
    def multiply(self, a):
        self.a = a
        MULTIPLIER = 3.5
        return (MULTIPLIER * self.a)

    @staticmethod
    def subtract(b, c):
        return b - c

    # Using @property decorator
    @property
    # Getter method
    def value(self):
        print("Getting value...")
        return self.__value

        # Setter method

    @value.setter
    def value(self, xy_tuple):
        print("Setting value...")
        self.__value = xy_tuple

    # Deleter method
    @value.deleter
    def value(self):
        del self.__value


# Creating object
n = Numbers()

# Setting value
n.value = '(3,5)'
print(n.value)
# Deletes name
# del n.value

# As name is deleted above this
# will throw an error


# Prints value
print(n.value)
print(n.add(2,3))
print(n.multiply(3))
print(n.subtract(3,4))