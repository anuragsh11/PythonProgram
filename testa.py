def a(n,operation):
    arr = [0 for i in range(n)]
    for i in range(len(operation)):
        #print(operation[i])
        ar =operation[i]
        print(ar)
        min = ar[0]
        max = ar[1]
        value = ar[2]
        print(min,max,value)
        for j in range(min, max+1):

            arr[j-1] =arr[j-1] + value
        print(arr)
    arr=[100,300,100,100,200,400,100]
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            max =arr[i]
    return max

print(a(5,[[1,2,100],[2,5,100]]))

program :2
def swap_case(s):
    lis=[]
    for i in s:
        if i.islower() ==True:
            lis.append((i.capitalize()))
        else:
            lis.append((i.lower()))

    newS="".join(lis)
    print(newS)




swap_case("SG.2ehL62pSmsnd7c9XYYsFvV067gybBhsSM0SJ7zpAJWr8pwEFzq3ACtuSAjpL7ZnWXbASGlBnEawSnWs1 gpCySKB2.at bt5S.")