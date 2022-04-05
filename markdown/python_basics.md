To get the most out of this course, follow along with Andrei and code along with the videos. The course will go over how to install Python on your computer later. To start, you can use Python in [Repl.it](https://replit.com/).

- [Python Basics](#python-basics)
- [Learning Python](#learning-python)
- [Python Data Types](#data-types)
- [How to Succeed](#succeed)
- Numbers
- Math Functions
- DEVELOPER FUNDAMENTALS I
- Operator Precedence
- Optional: Bin and Complex
- Variables
- Expressions vs. Statements
- Augmented Assignment Operator
- Strings
- String Concatenation
- Type Conversion
- Escape Sequence
- Formatted Strings
- String Indexes
- Immutability
- Built-in Functions and Methods
- Booleans
- DEVELOPER FUNDAMENTALS II
- Lists
- List Slicing
- Matrix
- List Methods
- Common List Patterns
- List Unpacking
- None
- Dictionaries
- DEVELOPER FUNDAMENTALS III
- Dictionary Keys
- Dictionary Methods
- Dictionary Methods 2
- Tuples
- Sets
- Sets 2

## <a id="learning-python"></a> Learning Python
There are four key things you need to master for learning a programming language, including Python:
1. Terms: things like statements, variables, etc. so you can talk to other programmers
2. Data types: values a program can hold to store information
3. Actions - programming is a way to tell our machines how to store and retrieve data and perform actions on that data
4. Best practices - we need to learn the good ways to write programs with a solid structure

## <a id="data-types"></a> Python Data Types
We will use [Repl.it](https://replit.com/) to write our first Python code so we don't have to worry about installation at first.

Python has several data types. We'll list them out and then discuss them individually. Notice that the REPL will highlight these data types, which clues us in that there is something special about them.

A data type represents a value in Python, and writing a program allows us to take actions on these data types. Examples of actions include creating, changing/manipulating, storing, and removing data types.

Python Data Types:
- int: integer (a whole number)
- float: floating point number
- bool: boolean
- str: string
- list
- tuple
- set
- dict
- None: the absence of value

We can also create our own custom data types using something called classes. We'll explore how to do this later in the course.

We also have specialized data types. They are special packages and modules we can use from libraries. They're a little something extra, an extension, beyond a standard Python data type.

## <a id="succeed"></a> How to Succeed

In order to get the most out of this course, please code along with Andrei throughout the next sections. Hands-on practice is the best way to develop your skills.

## Numbers

This lecture will cover two data types: int and float. An integer is a number, such as 3, 4, or 5. We can use integers to perform mathematical operations in a program. The following code prints new numbers based on the mathematical operations we're performing on two whole numbers numbers.

A float is a floating point number, or a number with a decimal point, such as 0.5. We need to make this distinction because a float takes up more space in memory compared to an integer on our machines. Adding an integer and a float will result in a float as will adding two floats together, even if the result is a whole number. For more information on floating point numbers, check out this [Floating Point Numbers video](https://www.youtube.com/watch?v=PZRI1IfStY0).

If the syntax is intimidated, don't worry! As we work with these concepts more, it will become more familiar. And, if you're ever confused about a Python data type or anything else that has to do with the language, you can learn more about it in the [Python documentation](https://docs.python.org/3/contents.html).


```python
print(2 + 4) # addition - result is 6
print(2 - 4) # subtraction - result is -2
print(2 * 4) # multiplication - result is 8
print(2 / 4) # division - result is 0.5
print(2 ** 3) # exponent - 2 to the 3rd power is 8
print(3 // 4) # double division returns an integer, rounded down to an integer - result is 0
print(5 // 4) # result is 1
# The modulo operator represents the remainder of division. 6 divided by 4 is 1 with a remainder of two.
print(6 % 4)
# type is another action we can perform to check a data type. Content in inner brackets is evaluated first
print(type(2 + 4)) # integer
print(type(2 / 4)) # float
print(type(5.001)) # float
print(type(10 + 1.1)) # float
print(type(9.9 + 1.1)) # float
print(type(0)) # integer
```

    6
    -2
    8
    0.5
    8
    0
    1
    2
    <class 'int'>
    <class 'float'>
    <class 'float'>
    <class 'float'>
    <class 'float'>
    <class 'int'>


## Math Functions

There are specific math functions built into Python that we can use on integers and floating point numbers. Functions are actions we can take on data, such as print() and type(). Try the following out in your REPL.

See this article on [Python Mathematical Functions](https://www.programiz.com/python-programming/modules/math) for more and try Googling for Python math functions as well. Also, keep in mind that you'll never need all of the math functions in Python. We'll go over some of the important once in this course.


```python
print(round(3.1)) # rounding down the number - result is 3
print(round(3.9)) # result is 4
print(abs(-20)) # returns absolute value of the argument (no negative numbers)
```

    3
    4
    20


## DEVELOPER FUNDAMENTALS I
Developer fundamentals will be sprinkled throughout the course and will go over common mistakes in the hopes that we can avoid them as well as tips on how to be a great Python developer.

The first developer fundamental is: Don't read the dictionary. This means, don't worry about every little thing. Look up what we need to in the documentation, but don't try to read or memorize everything. Make sure you understand what exists, what you can use, and learn how to write good Google queries to find the information we need. This ensures we're focusing on the things that actually matter.

## Operator Precedence
Different operators have precedence over others, like multiplication gets evaluated before addition. 

Whatever is wrapped in parentheses gets evaluated first. Exponents get evaluated next, then multiplication and division, and finally, addition and subtraction.

Try these out in your REPL along with the exercises in the following lecture.


```python
print(20 - 3 * 4) # 3 * 4 gets evaluated before 20 - 3 - result is 8
print((20 - 3) + 2 ** 2) # result is 21
```

    8
    21


## Bin and Complex
There is an extra data type we didn't discuss. It's called complex and is a third type of number. We won't focus on it because it's only significant if we're doing complicated math.

Integers and floats get stored as binary numbers. There is an action called bin that we can use to return a binary representation of an integer.


```python
print(bin(5)) # binary number for 5 is 101
print(bin(8))
print(int('0b101', 2)) # convert this base 2 binary number to an integer
```

    0b101
    0b1000
    5


## Variables
All programming languages have variables so that we can store information. Assigning a value is also known as binding. The number below is stored as a binary representation (zeros and ones).

The following are best practices to use when writing Python variables:
* They should be snake_case
* Start with lowercase or underscore
* Use letters, numbers, or underscores
* They are case-sensitive
* Don't overwrite keywords
* Make variable names descriptive

Other things to be aware of:
* Constants should be in capitals, i.e., PI = 3.14
* There are dunder variables that start with two underscores that should not be assigned
* Underscore in Python singnifies a private variable (_user_iq)


```python
user_iq = 190
user_age = user_iq / 4
print(user_age)
```

    47.5



```python
a, b, c = 1, 2, 3
print(b)
```

    2


## Expressions vs. Statements
An expression is the right side of a statement. A statement is an entire line of code that performs some sort of action.

As in the previous example, user_iq / 4 is an expression. user_age = user_iq / 4 and user_iq = 190 are statements.

## Augmented Assignment Operator
In the example below, some_value += 2 makes use of the augmented assignment operator.


```python
some_value = 5
some_value += 2
```

## Strings (str)
A string is a piece of text and can be encapsulated in single or double quotes.


```python
print(type('hellooooo'))
```

    <class 'str'>



```python
username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
 00
---
'''
```


```python
print(long_string)
```

    
    WOW
     00
    ---
    


## String Concatenation
String concatenation is simply adding strings together. This only works with strings in Python. If we added the number 5 + hello, we would get a TypeError


```python
print('hellooooo' + ' Andrei')
```

    hellooooo Andrei


## Type Conversion
With Python, we can convert one data type to another. For instance, we can convert a string to an integer.


```python
print(type(str(100)))
```

    <class 'str'>



```python
print(type(int(str(100))))
```

    <class 'int'>


## Escape Sequence
The following are escape sequences -- a backslash -- that allows us to interpret whatever comes after it as a string.


```python
weather = 'It\'s kind of sunny'
print(weather)
```

    It's kind of sunny



```python
print('\t weather')
```

    	 weather



```python
print('--\nHope you have a good day')
```

    --
    Hope you have a good day


## Formatted Strings
Formatted strings allow us to use strings in a dynamic way instead of hard-coding everything. This is important when we are writing programs to work with users and with databases.

In general, the formatted string is recommended now (f-string) versus .format. Try the exercises below in your own REPL.


```python
name = 'Johnny'
age = 55
print("Hi, " + name)
print(f"Hi {name}. You are {age} years old.") # preferred
print("Hi {}. You are {} years old.".format(name, age)) # python2 syntax
print("Hi {0}. You are {1} years old.".format(name, age))
```

    Hi, Johnny
    Hi Johnny. You are 55 years old.
    Hi Johnny. You are 55 years old.
    Hi Johnny. You are 55 years old.


## String Indexes
str is an ordered sequence of characters that are stored in memory in same order and can be accessed by indeces.


```python
name = "Andrei"
print(name[0])
print(name[0:2])
print(name[0:4:2])
print(name[1:])
print(name[:3])
print(name[::2])
print(name[::1])
print(name[-2])
print(name[::-1]) # reverse a string
```

    A
    An
    Ad
    ndrei
    And
    Ade
    Andrei
    e
    ierdnA


## Immutability
Strings are immutable in Python. If we reassign a string in Python, it will overwrite the original string.
[start:stop:step] is string slicing.

## Built-In Functions and Methods
We have been learning about built-in functions that Python can take on data, such as str(), int(), type(), print(), and float(). Some resources for built-in functions are [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp) [Built-in Functions](https://docs.python.org/3/library/functions.html)



```python
print(len("hellooooo"))
```

    9



```python
greet = "hellooooo"
print(greet[:])
print(greet[0:len(greet)])
```

    hellooooo
    hellooooo


A good code editor will show available methods after we add dot notation.


```python
quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find('be')) # index of the word 'be'
print(quote.replace('be', 'me')) # replace all occurances of 'be' with 'me'
print(quote) # after the code above prints, it is removed from memory. The original string is not modified
```

    TO BE OR NOT TO BE
    To be or not to be
    3
    to me or not to me
    to be or not to be


## Booleans
A boolean can either be set to true or false. We can use them to control the flow of our program.


```python
name = "Andrei"
isCool = True
print(isCool)
```

    True



```python
# convert integers into boolean values
print(bool(1))
print(bool(0))
```

    True
    False


## DEVELOPER FUNDAMENTALS II
As soon as Python sees a #, it adds a comment.

Guidelines for comments:
* When you comment your code, you're adding valuable content to help another programmer or yourself when you review it later.
* Add comments to explain complexity rather than for everything.

## Lists
A list is an ordered sequence of objects that can be of any type. We denote lists with square brackets. We can have different objects inside of these square brackets.

If you're familiar with other programming languages, you might have heard of arrays. Lists are similar, but we'll talk about the differences later in the course.

In Python, we can have lists with mixed data types, as with li3 below.

The list is the first data structure we're learning. Data structures are ways for us to organize information in a program. Think of them as a container around our data with different pros and cons.


```python
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True, 1.67]
```

We can access items in a list similar to how we accessed characters in a string. If we try to access a third item in the list below, we'll get a "list index out of range" error since a third item doesn't exist.


```python
amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])
```

    notebooks
    sunglasses


## List Slicing
We saw square brackets earlier, when we were working with strings. We can use list slicing as we did with string slicing earlier in the course.

Unlike strings, lists are mutuable. We can change our amazon_cart.


```python
amazon_cart2 = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart2)
# Remember: with slicing, the second number is NOT inclusive
print(amazon_cart2[0:2]) # get first two items in the cart
print(amazon_cart2[0::2])
```

    ['notebooks', 'sunglasses', 'toys', 'grapes']
    ['notebooks', 'sunglasses']
    ['notebooks', 'toys']



```python
# Let's change our list!
amazon_cart2[0] = "laptop"
print(amazon_cart2)
print(amazon_cart2[0:3]) # get item 1 - 3, not including 3
```

    ['laptop', 'sunglasses', 'toys', 'grapes']
    ['laptop', 'sunglasses', 'toys']


Every time we slice a list, we create a new copy of our list. But, if we set our list equal to another list, if we modify the new list, we'll modify our old list as well.

This happens because we're setting the lists equal to one another, and they're pointing to the same place in memory. This is different than when we slice a list because slicing makes a copy whereas when we set two lists equal to one another, we're creating conditions under which both lists will be modified.


```python
new_cart = amazon_cart2
new_cart[0] = 'gum'
print(amazon_cart2)
print(new_cart)
```

    ['gum', 'sunglasses', 'toys', 'grapes']
    ['gum', 'sunglasses', 'toys', 'grapes']


## Matrix
A matrix is a way to describe multi-dimensional lists. It's a list with another list inside of it. We have a list with sub lists. These topics come up a lot in machine learning and image processing. Matrices allow us to do some heavy calculations under the hood.


```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1]) # print second item in the first list
print(matrix[2][1]) # print the second item in the last list
print(matrix[1][2]) # print the last item in the second list
```

    2
    8
    6


## List Methods
We can perform a number of actions on lists with list methods. See the [W3Schools Resource](https://www.w3schools.com/python/python_ref_list.asp) for more Python list methods.

Try out the examples below. And remember, if you're using [replit.com](https://replit.com/), as soon as you write the variable plus the dot, the conding environment will tell you which methods you can use.


```python
basket = [1, 2, 3, 4, 5]
# Remember, the length starts counting from one, not zero
print(len(basket)) # calculate the length of the basket
```

    5


The append, insert, and extends methods modify an existing list in place (in memory). They don't create a copy of the list that they modify.

The extends method takes an item we can iterate over, like a list, and modifies it.


```python
# adding items to a list
print(basket)
basket.append(100)
new_list = basket
print(basket)
print(new_list)
```

    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5, 100]
    [1, 2, 3, 4, 5, 100]



```python
# insert an item into a list
basket.insert(4, 50)
print(basket)
```

    [1, 2, 3, 4, 50, 5, 100]



```python
# extending our list
# 101 is added twice because this cell was printed more than once
new_list = basket.extend([101])
print(basket)
```

    [1, 2, 3, 4, 50, 5, 100, 101, 101]



```python
# removing items from our list
basket.pop() # removes last item from the list
print(basket)
```

    [1, 2, 3, 4, 50, 5, 100, 101]


With pop, we give it the index and with remove, we give it the value. Pop also returns the value that was removed. The clear method removes everything from the list.


```python
basket.pop()
basket.pop(0) # remove item at index 0
basket.remove(4) # remove 4 from the list
```


```python
print(basket)
```

    [2, 3, 50, 5, 100]



```python
# remove all items from the list
basket.clear()
print(basket)
```

    []


## List Methods 2
Index is a list method we can use. We give it a value, a start, and a stop.

A Python keyword is a word that means something to the language that we cannot use to name a variable. Examples are True (a boolean) or in. We can use 'in' to see if something is in a list.

We can use 'count' to count how many times an item occurs.


```python
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d'))
print(basket.index('d', 0, 4)) # item to search for, index to start search, index to stop search
```

    3
    3



```python
print('d' in basket)
print('x' in basket)
print('i' in 'hi my name is Ian')
print(basket.count('d'))
```

    True
    False
    True
    1


## List Methods 3
A continuation of list methods, in which we'll look at sorting and reversing the order of the items in a list.


```python
basket.append('d')
basket.insert(2, 'x')
print(basket)
```

    ['a', 'b', 'x', 'c', 'd', 'e', 'd']



```python
basket.sort()
print(basket)
```

    ['a', 'b', 'c', 'd', 'd', 'e', 'x']


We can also use sorted(basket) if we want to produce a new list without modifying the existing one. It creates a new copy of the list as with list slicing.

If we want to do the opposite of sort, we can use the reverse() method. It's a good idea to sort first, however, otherwise the reverse() method may not work as expected.


```python
basket.sort()
basket.reverse()
print(basket)
```

    ['x', 'e', 'd', 'd', 'c', 'b', 'a']


## Common List Patterns

