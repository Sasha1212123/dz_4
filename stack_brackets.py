class Stack:
    """Класс реализует структуру данных стек (LIFO)."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка стека на пустоту."""
        return len(self.items) == 0

    def push(self, item):
        """Добавление элемента на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаление верхнего элемента и его возврат."""
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.items.pop()

    def peek(self):
        """Возвращает верхний элемент без удаления."""
        if self.is_empty():
            raise IndexError("Попытка посмотреть элемент в пустом стеке")
        return self.items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)


def is_balanced(sequence):
    """Проверка сбалансированности скобок."""
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


if __name__ == '__main__':
    sequence = input("Введите последовательность скобок: ").strip()

    if is_balanced(sequence):
        print("Сбалансированно")
    else:
        print("Несбалансированно")
