lst=eval(input('enter elements of list separated by commas'))
l1=list(lst)
print(l1)
for x in range(len(l1)):
    m=l1[x]
    if (m>0):
        print(m,end=' ,')
