from typing import List

class Stack:
    """
    Basic Stack object, used to ease processing and cut corners
    """
    stack: List
    name: str

    def __init__(self, name="", premade=[]):
        """
        premade is a list of something that you want as a stack already,
        Whatever the order of premade is will be the order of the stack from bot
        to top

        if premade is not a list, it is ignored

        """
        if isinstance(premade, list):
            self.stack = premade
        else:
            self.stack = []
        self.name = name

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, obj) -> None:
        self.stack.append(obj)

    def pull(self) -> 'Any':
        """
        Removes the top obj on the stack and returns it
        """
        if self.is_empty():
            print("Stack: {} is empty and was pulled".format(self.name))
            raise Exception
        return self.stack.pop()

    def height(self) -> int:
        """
        Returns height of stack, how many obj in it
        """
        return len(self.stack)

    def remove_objs(self, position: int, destruction: int ) -> None:
        """
        Removes destruction amount of obj's in order below the position obj
        Preserves order of stack after removal

        position is the position in the stack of the obj, from bottom to top
        """
        height = self.height()
        holder = []

        while height != position:
            holder.append(self.pull())
            height = self.height()

        holder.reverse()
        for i in range(destruction):
            self.pull()

        self.stack.extend(holder)

    def __str__(self) -> str:
        formatting = 'Height: ' + str(len(self.stack)) + '\n'
        for thing in self.stack[::-1]:
            formatting += str(thing) + ': ' + str(self.stack.index(thing)) + '\n'
        return formatting


if __name__ == '__main__':
    s = Stack()
    t = range(7)
    for i in t:
        s.push(i)
    s.pull()
    print(s)
    s.remove_objs(4, 4)
    print(s)

