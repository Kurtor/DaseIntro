import random
import time
def Merge(list,begin,mid,end):
    sublist = []
    i = begin
    j = mid + 1
    while i <= mid and j <= end:
        if list[i] <list[j]:
            sublist.append(list[i])
            i += 1
        else:
            sublist.append(list[j])
            j += 1
    while i > mid and j <= end:
        sublist.append(list[j])
        j += 1
    while i <= mid and j > end:
        sublist.append(list[i])
        i += 1
    k = begin
    for i in range(len(sublist)):
        list[k] = sublist[i]
        k += 1
    return
def MergeSort(list,begin,end):
    if(begin >= end):
        return
    else:
        mid = int((begin + end)/2)
        MergeSort(list,begin,mid)
        MergeSort(list,mid + 1,end)
        Merge(list,begin,mid,end)
        return


list = []
for i in range(4,5):
    t = 0.0
    for j in range(0,1):
        m = 0
        while m < 10**i:
            num = random.randint(0,10000)
            if num not in list:
                m += 1
                list.append(num)
    start = time.time()
    MergeSort(list,0,len(list)-1)
    end = time.time()
    t+=end-start
    print(list)