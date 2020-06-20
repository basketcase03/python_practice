module = "os"
import inspect
import importlib
import types
module=importlib.import_module(module)
lst=inspect.getmembers(module)
#print(module.__doc__)
for obj in lst:
    #print(type(obj))
    if(inspect.isfunction(obj[1])):
        print(obj[0])
