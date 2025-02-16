"""
Я сначала увидел решение через указатели, с использованим цикла do-while
Идея: переставлять указатели left и right до тех пор, пока
right не выйдет за рамки длины строки.
Из минусов, при таком счете нужно считать локальные суммы.
По условиям - если текущий элемент меньше предыдущего - л_сумму увеличиваем
Иначе - л_сумму вычисляем как текущее минус прошлое.
Ну и плюс счёт.
Как по мне - слишком много вычислений и переменных, сложно.

Пока задумался, заметил, что читая римское число задом наперед,
достаточно только ОДНОГО указателя и ОДНОЙ суммы. Причем обход циклом
вызовет не выше O(n). То, что нужно.
Из условий: если текущее значение - первая итерация или
если текущий элемент больше прошлого (left > right) - прибавляем значение
иначе - вычетаем.
P.s. ну и объявление "прошлого значения" вынес вне цикла для избежания
повторного вычисления и двух обращений к списку/словарю. 
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        meaning_of_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        value = meaning_of_roman[s[0]]
        for index in range(len(s)):
            last_value = value
            value = meaning_of_roman[s[-1 - index]]
            if (
                index == 0 or
                value >= last_value
            ):
                result += value
            else:
                result -= value
        return result


solution = Solution()

print('Example 1:', solution.romanToInt(s='III'))
print('Example 2:', solution.romanToInt(s='LVIII'))
print('Example 3:', solution.romanToInt(s='MCMXCIV'))
