def displayInventory(inventory):
    sum = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        sum += v
    print("tong so items la: " + str(sum))
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(str(item),0)
        inventory[item] += 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)
displayInventory(inv)
