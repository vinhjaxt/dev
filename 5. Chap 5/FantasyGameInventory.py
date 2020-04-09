stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    sum = 0
    for k, v in inventory.items():
            print(str(v) + ' ' +  k)
            sum += v
    print('tong so items la: ' + str(sum))
displayInventory(stuff)