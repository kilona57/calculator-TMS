class UnknownOperationError(Exception):
    """Ошибка при вводе неизвестной операции"""
    def __str__(self) -> str:
        return f"Ошибка: Введена неизвестная операция. Попробуй снова."

class NotNumberError(Exception):
    """Ошибка при вводе не числа"""
    def __str__(self) -> str:
        return f"Ошибка: Введено значение, которое не является числом. Попробуй снова."