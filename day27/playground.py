def add(*args):
    input_nums=[]
    for n in args:
        input_nums.append(n)
    print(f"Input numbers: {input_nums}")
    print(f"The sum is: {sum(args)}")

add(10, 10, 20)

def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"Key: {key}, Value: {value}")
        
    # print(kwargs["add"])
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n) #25
    
calculate(2, add=3, multiply=5)

class Car():
    
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # In order to not crash when model wasnot writen we use get
        self.make = kw.get("make")
        self.model = kw.get("model")
        
        
my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model)