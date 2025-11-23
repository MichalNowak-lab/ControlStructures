x = int(input('Enter X: '))
y = int(input('Enter Y: '))
if x == 0:
    print(f'Point P({x},{y}) is located on y axis')
if y == 0:
    print(f'Point P({x},{y}) is located on x axis')
if x>0 and y>0:
    print(f'Point P({x},{y}) is located on 1 quadrant')
if x<0 and y>0:
    print(f'Point P({x},{y}) is located on 2 quadrant')
if x<0 and y<0:
    print(f'Point P({x},{y}) is located on 3 quadrant')
if x>0 and y<0:
    print(f'Point P({x},{y}) is located on 4 quadrant')