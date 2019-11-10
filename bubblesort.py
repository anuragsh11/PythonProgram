def bubble_sort(arr):
    flag = True
    counter=0
    while flag:
        flag=False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                flag = True
                counter+=1
    print(counter)




a_list=[5,4,3,2,1]
print('list without sort',a_list)
bubble_sort(a_list)
print('sorted list is ', a_list)