class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка, пуст ли стек"""
        return len(self.items) == 0

    def push(self, item):
        """Добавление элемента на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удаление верхнего элемента и возврат его значения"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Возврат верхнего элемента без удаления"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        """Возврат количества элементов"""
        return len(self.items)
