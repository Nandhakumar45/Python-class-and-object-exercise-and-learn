def repeat(n):
    def wrapper():
        repeat(4)
    return wrapper


@repeat(4)
def hello():
    print("Hello")
hello()