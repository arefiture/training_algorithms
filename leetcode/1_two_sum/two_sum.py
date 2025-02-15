"""
Чтоб не проходить список в два указателя или цикла
можно сохранять пройденные значения в словарь.

Таким образом - обход цикла в n элементов - O(n)
Запись/чтение словаря - O(1) ну и хранилища тоже.
По итогу получаем все те же O(n), в случае, когда
любой и последний элемент списка образуют цель-сумму.
Ну или в случае, когда сумма не найдена. В иных случаях
выходит <O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = {}
        for index in range(len(nums)):
            value = nums[index]
            diff = target - value
            if diff in index_nums:
                return [index, index_nums[diff]]
            index_nums[value] = index
        return []


solution = Solution()

print('Example 1:', solution.twoSum(nums=[2, 7, 11, 15], target=9))
print('Example 2:', solution.twoSum(nums=[3, 2, 4], target=6))
print('Example 3:', solution.twoSum(nums=[3, 3], target=6))
