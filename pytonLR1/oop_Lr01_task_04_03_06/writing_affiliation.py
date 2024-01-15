# Программирование на языке высокого уровня (Python).
# Задание № 04_03_06. Вариант 17
#
# Выполнил: Попов Антон
# Группа: ПИН-б-о-22-1
# E-mail: anton_32_99@mail.ru



class WritingAffiliation:
    NAME = 'Пишущая принадлежность'

    def __init__(self, *, color: str, width: float | int) -> None:
        self._color = color
        self._width = width

    def __str__(self) -> str:
        return self.NAME

    @property
    def color(self) -> str:
        return self._color

    @property
    def width(self) -> float | int:
        return self._width

    def write(self, text: str) -> bool:
        if text:
            print(f'С помощью "{self.NAME.capitalize()}" написали "{text}"')
        return bool(text)