# 冒泡排序
def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            if seq[j] < seq[i]:
                seq[j],seq[i] = seq[i],seq[j]

list = [12,341,565,733,31,6521,23,6,334,42,8,58,89]
bubble_sort(list)
print("冒泡排序后的结果:%s" %list)