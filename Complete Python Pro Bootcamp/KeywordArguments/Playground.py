#Function takes on an unlimited number of arguments and sums them all up
def add(*args):
    arguments = args
    sum = 0

    for i in arguments:
        sum += i    
 
    print(f'The sum of the tuple is: {sum}')
    #return print(sum(args))

#Function takes on a list and sums up it's items
def test(l):
    sum = 0

    for i in l:
        sum += i

    print(sum)
    
#Function takes 2 dictionairies and uses it for arithmetic operations
def arithmethic(**keyargs):
    add = 0
    multiply = 1
    add += keyargs['add']
    multiply *= keyargs['multiply']

    print(f'The sum is: {add}')
    print(f'The multiplication is: {multiply}')

#Class test
class Aircraft():
    def __init__(self, **kwargs):
        # self.type = kwargs['type']
        # self.name = kwargs['name']
        
        #Another way of writing it
        self.type = kwargs.get('type')
        self.name = kwargs.get('name')