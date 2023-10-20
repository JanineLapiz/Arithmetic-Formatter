# Arithmetic Formatter
_NOTE: This is [a Python exercise from freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)._

## Description
This is for transforming an array of elementary arithmetic problems into a readable format, e.g:
```
['23 + 125', '3452 - 123', '653 + 234']
```
becomes
```
   23      3452      653
+ 125    -  123    + 234
-----    ------    -----
```

## Rules and Limitations
1. Only addition and subtraction are accepted.
2. Five problems is the limit.
3. Operands must not be more than 4 digits.
4. There cannot be more than 2 operands.
6. Operands and operators must be separated by a space.