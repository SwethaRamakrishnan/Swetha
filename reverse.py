def main():
    string = str(input("Enter the string : "))
    n =len(string)
    l = list(string)
    ans = l[n-1]
    while(n>1):
        ans = ans+l[n-2]
        n -= 1
    print(ans)

if __name__ == '__main__':
    main()

   
