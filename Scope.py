#Local Scope - A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myFunc():
    x = 300
    print(x)

myFunc()

def myOuterFunction():
  x = 300
  def myInnerFunc():
    print(x)
  myInnerFunc()

myOuterFunction()

'''
Global Scope - 
A variable created in the main body of the Python code is a global variable and belongs to the global scope. 
Global variables are available from within any scope, global and local.
'''

x = 300

def myGlobalFunc():
  print(x)

myGlobalFunc()

print(x)

'''
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
'''

def myfunc():
  global x
  x = 300

myfunc()

print(x)

'''
Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.
'''
def myfunc1():
    x = "Arun"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())