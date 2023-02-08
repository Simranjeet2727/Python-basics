#calling inner function from nested function
def o():
    x="5"
    print("outer function")
    def i():
        print(x)
        print("inner function")
    i()

o()     #calling outer function