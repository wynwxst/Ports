def allowdir(path):
  import sys
  import os
  import inspect
  currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
  parentdir = path
  sys.path.insert(0, parentdir) 
  


def loadModule(moduleName):
    module = None
    try:
        import sys
        del sys.modules[moduleName]
    except BaseException as err:
        pass
    try:
        import importlib
        module = importlib.import_module(moduleName)
    except BaseException as err:
        serr = str(err)
        print("Error to load the module '" + moduleName + "': " + serr)
    return module

def reloadModule(moduleName):
    module = loadModule(moduleName)
    moduleName, modulePath = str(module).replace("' from '", "||").replace("<module '", '').replace("'>", '').split("||")
    if (modulePath.endswith(".pyc")):
        import os
        os.remove(modulePath)
        module = loadModule(moduleName)
    return module

def getInstance(moduleName, param1, param2, param3):
    module = reloadModule(moduleName)
    instance = eval("module." + moduleName + "(param1, param2, param3)")
    return instance

module = loadModule("main.py")