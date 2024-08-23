# import logging

# logger = logging.getLogger(__name__)

# logging.basicConfig(filename='myapp.log', level=logging.DEBUG)

# def add(x, y):
#     return x + y

# x = 1
# y = 2

# logger.debug(f"{x} + {y} = {add(x, y)}")
import re
print(re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
       r'static PyObject*\npy_\1(void)\n{',
       'def myfunc():'))