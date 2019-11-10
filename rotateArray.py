def rotate_array(arr,d):
    n= len(arr)
    for i in range(d):
        temp=arr[0]
        for i in range(n -1):
            arr[i] =arr[i+1]
        arr[n-1] = temp




array = [1,2,3,4,5,6,7]
rotate_by=2
rotate_array(array,rotate_by)
print(array)