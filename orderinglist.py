#ordering teams


#fuction is created.
def g(x,y):
#reads the value from the list and checks the reason and update the value to d.
    d = x[0]>=y[0] and x[1]>=y[1] and x[2]>=y[2]
#checks the value from the list and checks the below and store the value to e.
    e= x[0]>y[0] or x[1]>y[1] or x[2]>y[2]
#this return the value as true or false
    return d and e
#takes the input from the user and store it to t.
t=int(input())
#checks the values of t in range.
for _ in range(t):
#gets user input and returns a string splits that input on whitespaces, applies the function fn to each element in the sequence, applies int to each string element in the input and turns any iterator/generator to a list 
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))

#checks the list a,b from the above function def g(x,y) and checks wether its satusfy as true or false.
    if g(a,b) and g(b,c):
        print('yes')
#else if part is called and checks the list a,c and agin it goes to above function def g(x,y) and checks true or false.
    elif g(a,c) and g(c,b):
        print('yes')
#else if part is called and checks the list b,a and agin it goes to above function def g(x,y) and checks true or false.
    elif g(b,a) and g(a,c):
        print('yes')
#else if part is called and checks the list b,c and agin it goes to above function def g(x,y) and checks true or false.
    elif g(b,c) and g(c,a):
        print('yes')
#else if part is called and checks the list c,a and agin it goes to above function def g(x,y) and checks true or false.
    elif g(c,a) and g(a,b):
        print('yes')
#else if part is called and checks the list c,b and agin it goes to above function def g(x,y) and checks true or false.
    elif g(c,b) and g(b,a):
        print('yes')
#if all the above value if the list dis-satisy it goes to the else part and print no
    else:
        print('no')
            