#from os import *

#system("pip list")

import math
import sys
import time

#import this

def sepl_def(str=""):
    sepl='|'*16*3
    print(f'''{str}
{sepl}
    ''')

def f_def(output="", text=None, comment1="", comment2="",line=">>>"):
    if text==None:
        text=output
    print(f'{line} {comment1}{text} = {eval(output)}{comment2}')

#sepl_def()
#a,b=999,124

#c=a/b

#c=int(a/b) #int
#res=c*b

#c=int(c)
#output=f''' c=int({a}/{b})
# c
# {c}
# res={c}*{b}
# res
# {res}'''.replace(" ",'>>> ')
#print(output)

#sepl_def()
#'''pi=math.pi
#print(f"{pi.as_integer_ratio()=}")
#pi=pi.as_integer_ratio()
#print(f"{pi[0]=}\n{pi[1]=}")
#print(f"{pi[0]/pi[1]=}\n{math.pi=}")
#sepl_def()'''
#'''output="'False'[True]"
#output=f'print(f"{output=}")'
#print(output, f'{output=}')
#sepl_def()'''
#help("int")

#print("Загрузка", end="", flush=True)
#for i in range(3):
#    time.sleep(0.5)
#    print(".", end="", flush=True)
#    
# Define a decorator function

def log_function_call(func):
    def wrapper(*args, **kwargs):
        output=f'''
{func.__name__}({str(args)[1:-1]}, {kwargs = }) #log\n'''
        result = func(*args, **kwargs)
        output += f'return {result}\n'
        print(f'\n{"#log":|<32}{16*"|"}\n{output}\n{"#log":|<32}{16*"|"}\n')
        return result
    return wrapper

@log_function_call
def f(*text):
    return list(text)

sepl_def()

print('list = f(6,0,24)')
list = f(6,0,24)
print('list[1] = bool(~-list[1])')
list[1] = bool(~-list[1])

f_def("list[1]")

f_def('(lambda f: [f.append(f[-1] + f[-2]) or f[-1] for _ in range(list[2] - 2)] and f)([int(0), int(1)])')
sepl_def()

output='''output=""

for i in range(list[2]):
    output+=f"{1 << i}, "
'''
print(output)
output=""
for i in range(list[2]):
    output+=f"{1 << i}, "
f_def(output,"output")
sepl_def()
list = []
list.append(list)
output='''list = []
list.append(list)'''
print(output)
f_def('list')
sepl_def()
f_def('(a := 6, 9) == ((a := 6), 9)')

sepl_def()

f_def('hash(float("inf"))')
value=10
valuе=1
f_def('value==valuе')
f_def('-~1000')

sepl_def()
#n1,n2=0,1
#for i in range(10):
#    print(n1)
#    n1, n2=n2, n1+n2
#print(f'{list((9,9,9))=}')

#sys.setrecursionlimit(2000)
#def f(): return f()
#f()
#help("sys")
