from numpy import random


class Checker:
    def sizecheck(self):
        while True:
            try:
                size1: int = int(input("Enter Minesweeper size:   "))
            except ValueError:
                print("Invalid Input!")
                continue
            else:
                if size1 > 5:
                    print("Invalid Input! ")
                else:
                    return size1

    def bombcheck(self):
        while True:
            try:
                bombs1: int = int(input("Enter number of BOMBS:   "))
            except ValueError:
                print("Invalid Input!")
                continue
            else:
                if bombs1 > (size * size - 1):
                    print("Invalid Input! ")
                else:
                    return bombs1

    def posXCheck(self):
        while True:
            try:
                pos: int = int(input("Input ROW: "))
            except ValueError:
                print("Invalid Input!")
                continue
            else:
                if pos > size-1:
                    print("Invalid Input! ")
                else:
                    return pos

    def posYCheck(self):
        while True:
            try:
                pos = int(input("Input COLUMN: "))
            except ValueError:
                print("Invalid Input!")
                continue
            else:
                if pos > size-1:
                    print("Invalid Input! ")
                else:
                    return pos


class Container:
    def fillingElements(self):
        for x in range(size):
            hold.append([])
            proxy.append([])
            open.append([])
            for y in range(size):
                hold[x].append(int(0))
                proxy[x].append(False)
                open[x].append(int(0))

    def managingBombs(self):
        for x in range(bombs):
            count1 = 0
            while count1 == 0:
                xrand = random.randint(size)
                yrand = random.randint(size)

                if hold[xrand][yrand] != 1:
                    hold[xrand][yrand] = 1
                    count1 = 1
    def countBombs(self):
        total = 0
        for x in range(3):
            x = x - 1
            row = xAxis + x
            for y in range(3):
                y = y - 1
                column = yAxis + y
                if container.isInside(column, row):
                    total += hold[row][column]
        return total

    def isInside(self, col, row):
        if col < 0 or col >= size or row < 0 or row >= size:
            return False
        else:
            return True


# -checked- is OBJECT for Checker class
checked = Checker()
# getting size and making sure taking the right input
size = checked.sizecheck()
# getting number of bombs and making sure to take the right input
bombs = checked.bombcheck()

# array holders
hold = []
open = []
proxy = []


# This fills in the array we -hold- and -proxy- so we can change it later
container = Container()
container.fillingElements()

# This makes sure that the number of bombs is accurate
container.managingBombs()
# Shows the cheat sheet
print("CHEAT SHEET")
for x in range(size):
    print()
    for y in range(size):
        print("[", end="")
        if hold[x][y] == 1:
            print("X",end="")
        else:
            print(" ",end="")
        print("]",end="")

print("\n ----GAME START!----")

# This is what the user supposed to see
for x in range(size):
    print()
    for y in range(size):
        if not proxy[x][y]:
            print("[ ] ", end="")
        else:
            held = f"[{hold[x][y]}] "
            print(held, end="")

test = 0
flag = 0
thebombs = (size*size) - bombs
while test != thebombs:
    print("\n \n")
    print("-Taking POSITION-")
    xAxis = checked.posXCheck()
    yAxis = checked.posYCheck()

    while proxy[xAxis][yAxis]:
        print("Repeated Input!")
        xAxis = checked.posXCheck()
        yAxis = checked.posYCheck()

    bomb = container.countBombs()
    open[xAxis][yAxis] = bomb
    proxy[xAxis][yAxis] = True
    if hold[xAxis][yAxis] == 1:
        flag = 1
        break
    else:
        for x in range(size):
            print()
            for y in range(size):
                if not proxy[x][y]:
                    print("[ ] ", end="")
                else:
                    held = f"[{open[x][y]}] "
                    print(held, end="")

        if hold[xAxis][yAxis] == 0:
            test += 1

if flag == 1:
    print("\n You stepped on a Bomb!")
else:
    print("\n WIN")


