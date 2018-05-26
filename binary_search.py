# 二分查找

def binary_search(find, list):
    low = 0
    high = len(list)
    while low <= high:
        mid = int((low + high) / 2)
        if list[mid] == find:
            return mid
        elif list[mid] > find:
            high = mid - 1
        else:
            low = mid + 1
    return -1

list = [1,23,4,5,62,2,57,45,2,35]
list.sort()

try:
    find = int(input("输入需要查找的数:"))
except:
    print("请输入整数")
    exit()
result = binary_search(find, list)
if result != -1:
    print("查找元素%d的序号为:%d" %(find, result))
else:
    print("未找到")

