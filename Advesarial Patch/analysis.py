from densenet_attack import attack


img = [
    'gibbon.jpg',
    'cat.jpg',
    'dog.jpg',
    'pig.jpg',
    'toaster.jpg',
    'chair.jpg',
    'table.jpg',
    'tree.jpg',
    'flower.jpg',
    'bottle.jpg',
    'fan.jpg',
    'bulb.jpg',
    'sign.jpg',
    'cake.jpg',
    'bread.jpg',
    'building.jpg',
    'eiffel.jpg',
    'drone.jpg',
    'shirt.jpg',
    'belt.jpg',
    'boots.jpg',
    'skirt.jpg',
    'cow.jpg',
    ]

for i, j in enumerate(img):
    print(i)
    attack(j)
