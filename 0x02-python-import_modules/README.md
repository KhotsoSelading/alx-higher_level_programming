# 0x02-Python-import_modules

## 0. Import a simple function from a simple file
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

### Task 0 Solution Explained:
1. The first line, `#!/usr/bin/python3`, is called a shebang. It specifies the interpreter to be used when executing the script. In this case, it indicates that the script should be run using Python 3.
2. The `if __name__ == "__main__":` line is a common idiom in Python. It checks if the script is being run directly as the main program, as opposed to being imported as a module. The code block following this condition will only be executed if the script is the main program.
3. The `from add_0 import add` line imports a function named `add` from the `add_0` module. The `add_0` module is assumed to be a separate Python file in the same directory as the script. This line allows the code to use the `add` function defined in the `add_0` module.
4. The next two lines, `a = 1` and `b = 2`, assign the values 1 and 2 to variables `a` and `b`, respectively.
5. The `print("{} + {} = {}".format(a, b, add(a, b)))` line uses the `print` function to display a formatted string. It uses curly braces `{}` as placeholders to insert the values of `a`, `b`, and the result of calling the `add` function with `a` and `b` as arguments. The `format` method is used to substitute the placeholders with the actual values.

## 1. My first toolbox!
Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

### Task 1 Solution Explained:
1. The first line, `#!/usr/bin/python3`, is a shebang that specifies the interpreter to be used when executing the script.
2. The `if __name__ == "__main__":` line checks if the script is being run directly as the main program.
3. The `from calculator_1 import add, sub, mul, div` line imports the functions `add`, `sub`, `mul`, and `div` from a module named `calculator_1`. This module is assumed to be a separate Python file in the same directory as the script. This line allows the code to use these arithmetic operations defined in the `calculator_1` module.
4. The next two lines, `a = 10` and `b = 5`, assign the values 10 and 5 to the variables `a` and `b`, respectively.
5. The following four lines use the `print` function to display formatted strings that perform arithmetic operations using the imported functions.
   - `print("{} + {} = {}".format(a, b, add(a, b)))` prints the sum of `a` and `b` using the `add` function.
   - `print("{} - {} = {}".format(a, b, sub(a, b)))` prints the difference of `a` and `b` using the `sub` function.
   - `print("{} * {} = {}".format(a, b, mul(a, b)))` prints the product of `a` and `b` using the `mul` function.
   - `print("{} / {} = {}".format(a, b, div(a, b)))` prints the division of `a` by `b` using the `div` function.

## 2. How to make a script dynamic!
Write a program that prints the number of and the list of its arguments.

### Task 2 Solution Explained:
1. The first line, `#!/usr/bin/python3`, is a shebang that specifies the interpreter to be used when executing the script.
2. The `if __name__ == "__main__":` line checks if the script is being run directly as the main program.
3. The `import sys` line imports the `sys` module, which provides access to system-specific parameters and functions. It is commonly used for accessing command-line arguments.
4. The line `iCounter = len(sys.argv) - 1` calculates the number of command-line arguments passed to the script. `sys.argv` is a list that contains the command-line arguments, where `sys.argv[0]` is the name of the script itself. By subtracting 1, we obtain the number of additional arguments.
5. The code block following the `if` condition checks the value of `iCounter` to determine the appropriate message to display.
   - If `iCounter` is 0, it means no additional arguments were passed, so it prints `"0 arguments."`.
   - If `iCounter` is 1, it means only one additional argument was passed, so it prints `"1 argument:"`.
   - If `iCounter` is greater than 1, it means multiple additional arguments were passed, so it prints the number of arguments using the format `"{} arguments:"`.
6. The subsequent `for` loop iterates `iCounter` times to print each command-line argument with its corresponding index.
   - In each iteration, the line `print("{}: {}".format(i + 1, sys.argv[i + 1]))` prints the argument index (`i + 1`) and the corresponding argument value (`sys.argv[i + 1]`).

## 3. Infinite addition
Write a program that prints the result of the addition of all arguments

### Task 3 Solution Explained:
1. The first line, `#!/usr/bin/python3`, is a shebang that specifies the interpreter to be used when executing the script.
2. The `if __name__ == "__main__":` line checks if the script is being run directly as the main program.
3. The `import sys` line imports the `sys` module, which provides access to system-specific parameters and functions. It is commonly used for accessing command-line arguments.
4. The line `theResult = 0` initializes a variable named `theResult` with a value of 0. This variable will be used to store the sum of the command-line arguments.
5. The `for` loop iterates over the command-line arguments passed to the script. `sys.argv` is a list that contains the command-line arguments, where `sys.argv[0]` is the name of the script itself. The loop starts from index 1 to skip the script name.
6. In each iteration of the loop, `int(sys.argv[i + 1])` converts the command-line argument to an integer. Since `sys.argv` is a list of strings, this conversion is necessary to perform addition later.
7. The line `theResult += int(sys.argv[i + 1])` adds the converted command-line argument to the `theResult` variable.
8. Finally, the line `print("{}".format(theResult))` uses the `print` function to display the value of `theResult`.

## 4. Who are you?
Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

### Task 4 Solution Explained:
1. The first line, `#!/usr/bin/python3`, is a shebang that specifies the interpreter to be used when executing the script.
2. The `if __name__ == "__main__":` line checks if the script is being run directly as the main program.
3. The `import hidden_4` line imports a module named `hidden_4`. This module is assumed to be a separate Python file or module located in the same directory as the script.
4. The `for` loop iterates over the names of the objects in the `hidden_4` module. The `dir()` function returns a list of names in the given module or object.
5. Inside the loop, the `if` condition checks if the name does not start with two underscores (`__`). This condition filters out special attributes and methods, as they typically start and end with double underscores in Python.
6. If the name passes the condition, it is printed using the `print(name)` statement. This will display the names of the objects defined in the `hidden_4` module that are not considered special attributes or methods.

## 5. Everything can be imported
Write a program that imports the variable a from the file variable_load_5.py and prints its value.

### Task 5 Solution Explained:
1. The first line, `#!/usr/bin/python3`, is a shebang that specifies the interpreter to be used when executing the script.
2. The `if __name__ == "__main__":` line checks if the script is being run directly as the main program.
3. The `from variable_load_5 import a` line imports a variable named `a` from a module named `variable_load_5`. This module is assumed to be a separate Python file or module located in the same directory as the script.
4. The `print(a)` line outputs the value of the variable `a` using the `print` function.
