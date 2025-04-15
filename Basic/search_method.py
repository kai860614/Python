# 在已排序又不重複的數列中找出目標資料的位置
# 舉例 [1,2,5,6,7]

#Linear search 線性搜索


def linear_search(numbers,target):
    # 若找到目標的數值則回傳數值的 index
    # enumerate:同時獲取元素的索引和值
    for index,num in enumerate(numbers):
        if num==target:
            return index
        # 找不到資料則回 -1
    return -1

print(linear_search([1,2,5,6,7],1))
print(linear_search([1,2,5,6,7],5))
print(linear_search([1,2,5,6,7],8))


print("-----------------------------------")

#Binary search 二元搜索 (只能對已排序的數列使用)

def binary_search(numbers, target): 
    # left/right/mid 皆為索引值
    left = 0
    right = len(numbers) - 1 
    while left <= right:
        mid = (left + right) // 2   #使用“//”整數除法確保值為整數
        if numbers[mid] > target:
            # 因為mid的值位於target值的右側且不包含mid,因此更新右邊邊界值為mid的前一個索引
            right = mid - 1
        elif numbers[mid] < target:
            # 因為mid的值位於target值的左側且不包含mid,因此更新左邊邊界值為mid的下一個索引
            left = mid + 1
        else:
            return mid              
    return -1


print(binary_search([1,2,5,6,7],1))
print(binary_search([1,2,5,6,7],5))
print(binary_search([1,2,5,6,7],8))

