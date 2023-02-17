# 32 Задание
class Box:
    def __init__(self, letter=None):
        self.letter = letter
        self.nextletter = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addToEnd(self, newletter):
        newbox = Box(newletter)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextletter):
            lastbox = lastbox.nextletter
        lastbox.nextletter = newbox

    def get(self, letterIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= letterIndex:
            if boxIndex == letterIndex:
                return lastbox.letter
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextletter

    def removeBox(self, rmletter):
        headletter = self.head

        if headletter is not None:
            if headletter.letter == rmletter:
                self.head = headletter.nextletter
                headletter = None
                return
        while headletter is not None:
            if headletter.letter == rmletter:
                break
            lastletter = headletter
            headletter = headletter.nextletter
        if headletter == None:
            return
        lastletter.nextletter = headletter.nextletter
        headletter = None

    def contains(self, letter):
        lastbox = self.head
        while (lastbox):
            if letter == lastbox.letter:
                return True
            else:
                lastbox = lastbox.nextletter
        return False


lnkd = LinkedList()
lst = list('Eeny, meeny, miney, moe; Catch a tiger by his toe.')
for i in lst:
    lnkd.addToEnd(i)

for i in 'AaEeUuIiOo':
    while lnkd.contains(i):
        for j in 'AaEeUuIiOo':
            if lnkd.contains(j):
                lnkd.removeBox(j)
                #print(j)
for i in range(len(lst)):
    try:
        print(lnkd.get(i), end='')
    except AttributeError:
        pass
