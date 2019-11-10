def sort_array(arr,d):
    anoarray=[]
    for i in range(d):
        if arr[i] >= 0:
            anoarray.append(arr[i])


    anoarray=sorted(anoarray)
    print(anoarray)
    j=0
    for i in range(d):
        if arr[i] >= 0:
            arr[i] = anoarray[j]
            j +=1

    print(arr)


arr=[1,6,-1,2,-5,11,9]
n = len(arr)
sort_array(arr,n)