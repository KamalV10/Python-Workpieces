def calculate():
    expression = input("Введите выражение (например, 5 + 3). Чтобы возвести число в степень введите ** вместо действия и % для вывода остатка от числа при делении: ")
    parts = expression.split()

    if len(parts) != 3:
        print("Формат неверный. Используйте: число пробел действие пробел число. Примеры: 8 + 2, 8 - 2, 8 * 2, 8 / 2, 8 ** 2, 8 % 2")
    else:
        num1, action, num2 = parts
        try:
            num1 = float(num1)
            num2 = float(num2)
        
            if action == '+': result = num1 + num2
            elif action == '-': result = num1 - num2
            elif action == '*': result = num1 * num2
            elif action == '**': result = num1 ** num2
            elif action == '%': result = num1 % num2
            elif action == '/': 
                if num2 != 0: result = num1 / num2
                else: raise ZeroDivisionError
            
            print("Результат:", result)
        except ValueError:
            print("Ошибка: одно из значений не является числом.")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль.")
while True:
    calculate()