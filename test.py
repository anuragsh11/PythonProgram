#  this is hacker earth problem for the Jack Jump
#  I have it in Java too
#
def maxStep(n, k):
    # Write your code here
    current=0
    for i in range(1,n+1):
        print(i,current)
        original = current
        current += i
        if i >= 1 and current == k:
            current = original + (i-1)

    print(current)


#maxStep(3,3)
maxStep(3,6)
