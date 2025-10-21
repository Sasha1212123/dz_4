from stack_class import Stack


def check_balance(sequence):
    """Проверка сбалансированности скобок"""
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == "__main__":
    sequence = input("Введите последовательность скобок: ")
    result = check_balance(sequence)
    print(result)
