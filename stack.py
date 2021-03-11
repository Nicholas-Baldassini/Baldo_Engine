""" Basic python stack ADT implementation """
from typing import List, Any


class Stack:
    """
    Basic Stack object, used to ease processing and cut corners wherever
    possible
    """
    stack: List
    name: str

    def __init__(self, name="", default=None):
        """
        default is a list of something that you want as a stack already,
        Whatever the order of default is will be the order of the stack from bot
        to top

        if default is not a list, it is ignored
        """
        if type(default) is not list:
            self.stack = []
        else:
            self.stack = default
        self.name = name

    def is_empty(self) -> bool:
        """
        Return True if stack is empty, contains no items
        Return False if elements exist in the stack
        """
        return len(self.stack) == 0

    def push(self, obj) -> None:
        """
        Push an item to the end of the stack, append to the end of the list
        """
        self.stack.append(obj)

    def pull(self) -> Any:
        """
        Removes the top item on the stack and returns it
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

    def remove_item(self, position: int, destruction: int) -> None:
        """
        Removes a destruction amount of item's in order below the position obj
        Preserves order of stack after removal

        position is the position in the stack of the obj, from bottom to top,
        the first added item is position 1

        >>> s = Stack(default=[1, 2, 3, 4, 5])
        >>> s.remove_item(4, 3)
        >>> s.stack
        [4, 5]
        """
        height = self.height()
        holder = []

        # Store all items from position to height
        while height != position - 1:
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
    import doctest
    doctest.testmod()

    # s = Stack()
    # t = range(7)
    # for i in t:
    #     s.push(i)
    # s.pull()
    # print(s)
    # s.remove_item(4, 4)
    # print(s)

