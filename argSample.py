'''def test_args_kwargs(**kwargs):
    for idx, val in  kwargs.items():
        print(val)

kwargs = {"arg3": 3, "arg2": "two", "arg1": "three"}

test_args_kwargs(**kwargs)

sample_dict = [{"val": 123}, {"val": 213}, {"val": 233}, {"val": 323}]

def makeitalic(arg_fun):
        def wrapper():
            return "<i>" + arg_fun() + "<i>"
        return wrapper

@makeitalic
def say():
   return "Hello"

print(say())



def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
'''
class base:
   baseVar = 'base';

class derived(base):
   derVar = 'derived'
   print("The var derived from {}".format(base.baseVar))

class derived2(derived):
   derived2 = 'derived2'
   print("The var derived from {}".format(derived.derVar))
   
