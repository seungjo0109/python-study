 ## 1. Follow the PEP8 Style Guide
* Python Enhancement Proposal #8, otherwise known as PEP 8, is the style guide for how to format Python code.
* Using a consitent style makes your code more approach able and easier to read.
* Sharing a common style with other Python programmers in the larger community facilitates collaboration on projects.

</br>

* PEP 8 provides a wealth of details about how to write clear Python code. It continues to be updated as the Python language evolves.
* It's worth reading the whole guide online(https://www.python.org/dev/peps/pep-0008/)

</br>

### Whitespace
* In Python, whitespace is syntactically significant. Python programmers are especially sensitive to the effects of whitespace on code clarity.
    * Use spaces instead of tabs for indentation.
    * Use four spaces for each level of syntatically significant indenting.
    * Lines should be 79 characters in length or less.
    * Continuations of long expressions onto additional lines should be indented by four extra spaces from their normal indentation level.
    * In a file, functions and classes should be seperated by two blank lines.
    * In a class, methods should be seperated by one black line.
    * In a dictionary, put no whitesapce between each key and colon. and put a single space before the corresponding value if it fits on the same line.
    * Put one - and only one - space before and after the = operator in a variable assignment.
    * For type annotations, ensure that there is no seperation between the variable name and the colon, and  use a space before the type information.

</br>

### Naming
* PEP 8 suggests unqiue styles of naming for different parts in the language. These conventions make it easy to distinguish which type correspond to each name when reading code.
    * Functions, variables, and attributes should be in lowercasse_underscore format.
    * Protected instance attributes should be in _leading_underscore format
    * Private instance attrubutes should be in __double_leading_underscore format.
    * Classes (including exceptions) should be in CapitalizedWord format.
    * module-level constants should be in ALL_CAPS format.
    * Instance methods in classes should use self, which refers to the object, as the name of the first parameter.
    * Class methods should use cls, which refers to the class, as the name of the first parameter.

</br>

### Expressions and Statements
* The `Zen of Python` states: "There should be one-and preferably only one-obvious way to do it." PEP 8 attempts to codify this style in its guidance for expressions and statements:
    * Use inline negation (if a is not b) instead of negation of positive expressions(if not a is b)
    * Don't check for empty containers or sequences (like [] or '') by comparing the length to zero (if len(somelist) == 0). `Use if not somelist` and assume that empty values willl implicitly evaluate to `False`.
    * The same thing goes for non-empty containers or sequences(like [1] or 'hi'). The statement if `somelist` is implicitly `True` for non-empty values.
    * Avoid single-line if statements, for and while loops, and except compound statements. Spread these over multiple lines for clarity.
    * If you can't fit an expression on one line, surround it with parentheses and add line breaks and indentation to make it easier to read.
    * Prefer surrounding multiline expressions with parentheses over using the \ line continuation character.

</br>

### Imports
* PEP 8 suggests some guidelines for how to import modules and use them in your code:
    * Always put import statements (including from x import y) at the top of a file.
    * Always use absolute names for modules when importing them, not names relative to the current module's own path. For exmplae, to import the `foo` module from within the `bar` package, you should use `from bar import foo`, not just `import foo`.
    * If you must do relative imports, use the explcit syntax `from . import foo`.
    * Imports should be in sections in the following order: standard library modules, third-party modules, your own modules. Each subsection should have imports in alphabetical order.

</br>

### Note
* The Pylint tool(https://www.pylint.org) is a popular static analyze for Python source code. Pylont provides automated enforcement of the PEP 8 style guide and detects many other types of common erros in Python programs.

</br>

### Reference: Effective Python: 90 Specific Ways to Write Better Python (Effective Software Development Series) 2nd Edition
