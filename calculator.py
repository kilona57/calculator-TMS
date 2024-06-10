from custom_exceptions import NotNumberError, UnknownOperationError
from math_operations import calculate

def is_number(value: str) -> bool:
    
    try:
        float(value)
        return True
    
    except ValueError:
        return False
    
def handle_exception(e: Exception) -> None:
    if isinstance(e, NotNumberError):
        print(str(e))   
    elif isinstance(e, UnknownOperationError):
        print(str(e)) 
    elif isinstance(e, ZeroDivisionError):
        print(f"Ошибка: Деление на ноль.") 
    else:
        print(f"Непредвиденная ошибка: {str(e)}") 
        
def main() -> None:
    
    print("Добро пожаловать в калькулятор!")

    while True:
        try:
            number_one_str = input("Введите первое число: ")
            if not is_number(number_one_str):
                raise NotNumberError("Первое число неявляется числом. Попробуй еще раз.")
            number_one = float(number_one_str)
                
            operation = input('Введите операцию (+, -, *, /, **): ')
            
            number_two_str = input("Введите первое число: ")
            if not is_number(number_two_str):
                raise NotNumberError("Второе число неявляется числом. Попробуй еще раз.")
            number_two = float(number_two_str)
            
            result = calculate(number_one, number_two, operation)
            print(f"Результат: {result}")
        
        except Exception as e:
            handle_exception(e)
        except KeyboardInterrupt:
            print("\nВыход из калькулятора.")
            break

if __name__ == "__main__":
    main()