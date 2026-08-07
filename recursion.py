##def count(n):
##    if n<1:
##        return
##    print(n)
##    return count(n+1)
##count(2)

##def fact(n):
##    if n<1:
##        return 1
##    return n*fact(n-1)
##print(fact(10))

##r=[]
##def flat(n):
##    for i in n:
##        if isinstance(i,list):
##            flat(i)
##        else:
##            r.append(i)
##flat([1,2,3,4,[5,[6,7,8,[9,10,11],12,13,[14,[15,[16,17,18]]]]]])
##print(r)
##print('Max=',max(r))
##print('Min=',min(r))
##print('Sum=',sum(r))
##print(r[::-1])
