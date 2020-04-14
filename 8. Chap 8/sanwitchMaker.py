import pyinputplus as pyip

breadType = {'wheat': 10, 'white': 15, 'sourdough': 20}
proteinType = {'chicken': 10, 'turkey': 15, 'ham': 20, 'tofu': 25}
cheeseType = {'cheddar': 10, 'swiss': 15, 'mozzarella': 20}



def inputMenu(breadType, proteinType, cheseeType):
    cost = 0
    for a, b in breadType.item():
        breadChoose = input('breadType:  ?')
        if not breadChoose in a:
            print('You must choose wheat, white or sourdough')
            break
        else:
            
