class MyInt(int):
    
    def __add__(self, x):
        return super().__add__(x) + 1

у = MyInt(2)
result = у + 2
print(result)
