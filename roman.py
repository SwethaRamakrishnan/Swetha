def main():
    roman=str(input("enter roman charater:"))
    arr=[]
    s=int_convert(roman_eq(roman,arr))
    print("Integer value of %s is %d"%(roman,s))
    
def roman_eq(r,a):
    length=len(r)
    for i in range(length):
        if(r[i]=='V'):
            a.append(5)
        elif(r[i]=='I'):
             a.append(1)
        elif(r[i]=='X'):
             a.append(10)
        elif(r[i]=='L'):
            a.append(100)
        elif(r[i]=='D'):
            a.append(500)
        elif(r[i]=='M'):
            a.append(1000)
        else:
            print("Enter valid charater")
            a.append(0)
    return a
    
def int_convert(a):
    i = len(a) - 1
    k = a[i]
    while(i>0):
        if(a[i]>a[i-1]):
            k -= a[i-1]
        elif(a[i] == a[i-1] or a[i]<a[i-1]):
            k += a[i-1]
        else:
            pass
        i -= 1
    return k

if __name__ == '__main__':
    main()
    
        
    

