from functools import wraps

def beforet(func):
    @wraps(func)
    def p():
        print("pstart")
        func()
        print("pend")
    return p
@beforet
def main():
    print("main")

main()
