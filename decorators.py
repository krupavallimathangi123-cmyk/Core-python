#def fun(a, b):
 #  print(a + b)
#fun(10, 20)
#   def Inner(x, y):
 #       print("starting this function")
  #      fun(x, y)
   # print(f"func:{func}")
    #print(f"Inner:{Inner}")
   # return Inner0
#def dec(fun):
#    def add(a,b):
#        print(a,b)
#    return add
#@dec
#def fun1(a,b):
#    print(a+b)
#fun1("hello","hi")
#fun1(10,"hello")
import functools
def dec(func):
    @functools.wraps(func)
    def Inner():
        fun()
    return Inner

@dec
def fun():
    """ this is docstring"""
    print("hello")
print(fun.__doc__)
print(fun.__name__)


import time
def timer(func):
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        start=time.asctime()
        start=time.time()
        print("started:",start)
        print(f"sum :{func(*args,**kwargs)}:")
        end=time.time()
        print(f"end: {end}")
        print("Time taken: ",end-start)
    return wraper
@timer
def add(x,y):
    """this is a doc string"""
    su=0
    for i in range(1,x+y+1):
        su+=1
    return su
add(100000,200000)
print(add.__doc__)
print(time.asctime())
print(list(time.asctime().split()))

