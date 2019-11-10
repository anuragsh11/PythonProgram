def check_pair(arr,l,sum):
    s = set()

    for i in range(0,l):
        temp=sum-arr[i]
        if temp in s:
            return (arr[i] ,temp)
        else:
            s.add(arr[i])

arr =[1,4,2,7,33,5,8]
len = len(arr)
sum= 40
print(check_pair(arr,len,sum))

