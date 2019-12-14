def main():
    number = eval(input("Enter a non-negative integer:                    "))
    product = 1
    for i in range(number):
        product = product*(i+1)
    print(product) 
    main()
main()
