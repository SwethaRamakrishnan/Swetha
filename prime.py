def prime():
    min = int(input("Enter the minimum value : "))
    max = int(input("Enter the maximum vale : "))
    for num in range(min+1,max+1):
        count = 0
        for i in range(2,num):
            if((num%i) == 0):
                count = 1
                break
        if(count == 0):
            print(num)
 prime()
