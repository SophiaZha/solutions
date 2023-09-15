# Using Python language, please implement a Product class and an exception class that represent a warehouse that can house a limited number of products. After the limit is reached, if there is an attempt to add additional product instance, it throws a custom error.
#
# Create two classes:
#
# 1. Product
# 	1. __init__(self, name) -- initialize the instance variable with its name attribute
# 	2. __del__(self) delete the instance.
# 	3. Track the number of Product instances.
# 		1. The number of allowed products can be changed dynamically. It is retrived by calling Limit.get_limit()
# 			1.If the number of Product instances is less than the current limit, create a new product instance.
# 			2.Otherwise, throw a UserLimitExceeded exception with the message "Product {name} can not be created. Maximum {limit} product allowed". Do not create a new instance.
# 2.User LimitExceeded(Exception) - This is an exception class. It accepts an error message in its constructor and throws an exception.
#

class UserLimitExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)


class Limit:
    max_limit = 5  # Initial maximum product limit

    @staticmethod
    def get_limit():
        return Limit.max_limit


class Product:
    product_count = 0

    def __init__(self, name):
        self.name = name
        Product.product_count += 1
        if Product.product_count > Limit.get_limit():
            Product.product_count -= 1
            raise UserLimitExceeded(f"Product {name} can not be created. Maximum {Limit.get_limit()} products allowed.")

    def __del__(self):
        Product.product_count -= 1
        del self


# Example usage:
try:
    # Set the maximum product limit
    Limit.max_limit = 3

    # Creating product instances
    try:
        p1 = Product("Product1")
        print("Product1 created.")
    except UserLimitExceeded as e:
        print(str(e))

    try:
        p2 = Product("Product2")
        print("Product2 created.")
    except UserLimitExceeded as e:
        print(str(e))

    try:
        p3 = Product("Product3")
        print("Product3 created.")
    except UserLimitExceeded as e:
        print(str(e))

    try:
        p4 = Product("Product4")
        print("Product4 created.")
    except UserLimitExceeded as e:
        print(str(e))

except UserLimitExceeded as e:
    print(str(e))
finally:
    # Explicitly delete some product instances
    del p1
    del p2

    # Trying to create a new product instance
    try:
        p5 = Product("Product5")
        print("Product5 created.")
    except UserLimitExceeded as e:
        print(str(e))







