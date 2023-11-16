# for List Itrations
list1=[10,10.5,'Apple',34,47] 
length=len(list1) 
while(1): 
    print('*****List Iteration*****') 
    print('1.Using for Loop') 
    print('2.Using for with range') 
    print('3.Using while') 
    print('4.Using list comprehension') 
    print('5.Using Enumeration') 
    print('6.Exit') 
    m=int(input('Enter your choice:')) 
    if(m==1): 
        for i in list1: 
            print(i) 
    elif(m==2): 
        for i in range(length): 
            print(list1[i]) 
    elif(m==3): 
        i=0 
        while i < length: 
            print(list1[i]) 
            i+=1 
    elif(m==4): 
        [print(i) for i in list1] 
    elif(m==5): 
        for i, val in enumerate(list1): 
            print(i,",",val) 
    else: 
        print('Exit from the program') 
    break 
 

 # for Dictionary Iterations

d={'key1':1,'key2':2,'key3':3} 
leng=len(d) 
for k in d: 
    print(k) 
print(list(d)) 
print(type(list(d))) 
while(1): 
    print('*****Dictionary Iteration*****') 
    print('1.Through dictionary keys()') 
    print('2.Through dictionary values()') 
    print('3.Through dictionary items()') 
    print('4.Exit') 
    c=int(input('Enter your choice:')) 
    if(c==1): 
        for k in d.keys(): 
            print(k) 
        print(d.keys()) 
        print(type(d.keys())) 
        print(list(d.keys())) 
        print(type(list(d.keys()))) 
    elif(c==2): 
        for v in d.values(): 
            print(v) 
        print(d.values()) 
        print(type(d.values())) 
    elif(c==3): 
        for k,v in d.items(): 
            print('Key=',k,'Value=',v) 
        print(d.items()) 
        print(type(d.items())) 
    elif(c==4): 
        print('Exit from the program') 
    break