class Counting:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myCounter = Counting()
myIteration = iter(myCounter)

for x  in myIteration:
    print(x)