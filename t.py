def collision(speed, pos):
    # Write your code here
    print(speed, pos)

    counter=0

    for i in range(0,pos):
        #print(i)
        if speed[pos] < speed[i]:
            print('yes')
            counter+=1
    for i in range(pos+1,len(speed)):
        print(speed[pos])
        if speed[pos] > speed[i]:
            counter+=1
    print(counter)



#collision([6,6,1,6,3,4,6,8],2)
collision([8,3,6,3,2,2,4,8,1,6],7)