from custom_exceptions import UnknownOperationError

def addition(number_one: float, number_two: float) -> float:
    """
    Выполняет сложение двух чисел.
    
    Args:
        number_one (float): Первое число.
        number_two (float): Второе число.
    
    Returns:
        float: Результат сложения.
    """
    return number_one + number_two

def subtraction(number_one: float, number_two: float) -> float:
    """
    Выполняет вычитание двух чисел.
    
    Args:
        number_one (float): Первое число.
        number_two (float): Второе число.
    
    Returns:
        float: Результат вычитания.
    """
    return number_one - number_two

def multiplication(number_one: float, number_two: float) -> float:
    """
    Выполняет умножение двух чисел.
    
    Args:
        number_one (float): Первое число.
        number_two (float): Второе число.
    
    Returns:
        float: Результат умножения.
    """
    return number_one * number_two

def division(number_one: float, number_two: float) -> float:
    """
    Выполняет деление двух чисел.
    
    Args:
        number_one (float): Первое число.
        number_two (float): Второе число.
    
    Returns:
        float: Результат деления.
    """
    return number_one / number_two

def power(number_one: float, number_two: float) -> float:
    """
    Выполняет возведение числа в степень.
    
    Args:
        number_one (float): Первое число.
        number_two (float): Второе число.
    
    Returns:
        float: Результат возведения в степень.
    """
    return number_one ** number_two

def calculate(number_one: float, number_two: float, operations: str) -> float:
    """
    Выполняет, базовые арифметические опреации над двумя числами.
    
    Args:
        number_one (float): Первое число.
        number_two (float): Второе число.
        operations (str): Арифметическая операция (+, -, *, /,  **)
    
    Returns:
        float: Результат выполненной операции.
        
    Raises:
        UnknownOperationError: Если введена неизвестная операция.
        ZeroDivisionError: Если второе число равно 0.
    """   
    match operations:
        case '+':
            return addition(number_one, number_two)
        case '-':
            return subtraction(number_one, number_two)
        case '*':
            return multiplication(number_one, number_two)
        case '/':
            return division(number_one, number_two)
        case '**':
            return power(number_one, number_two)
        case _:
            raise UnknownOperationError(operations)