<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="Cheat_Sheet-top"></a>

<!--
*** Thanks for checking out the Python-CheatSheet. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



# Python Cheat Sheet

<p align="center">
<img src="assets/images/python_logo.png" alt="Python Logo" width="200" height="200">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#python-basics">Python Basic</a></li>
    <li><a href="#control-flow">Control Flow</a></li>
    <li><a href="#functions">Functions</a></li>
    <li><a href="#classes">Classes</a></li>
    <li><a href="#exception-handling">Exception Handling</a></li>
    <li><a href="#file-handling">File Handling</a></li>
    <li><a href="#libraries">Libraries</a></li>
    <li><a href="#list-comprehensions">List Comprehensions</a></li>
    <li><a href="#lambda-functions">Lambda Functions</a></li>
    <li><a href="#main">__Main__</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
<!-->
Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`
-->
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Python Basics

* Print Statment :
  
```py
    print(f'Hello World')
```   
* Variables:

```py
    x = 5
    y = "S"
    z:char= 'D' #Type set variable
```

* Data Types:

```py
    int_var = 10
    float_var = 10.5
    str_var = "Hello"
    char_var = 'R'
    list_var = [1,2,3]
    tuple_var = (4,5,6)
    dict_var = {"Key1":"Value1","Key2":"Value2"}
```

* Lists:
```py
    my_list = [1,2,3,4]
    my_list.append(5) # Add an element
    my_list[0] = 10 # Modify an element  
```

* Tuples:
```py
    my_tuple = (1,2,3)
```

* Dictionaries:
```py
    my_dict = {"name":"Alice","age":25}
    my_dict["age"] = 26 # Modify Value
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## Control Flow
* If Statement:
```py
    if x>10:
        print(f'x is {x} which is greater than 10')
    elif x==10:
        print(f'x is {x} which is equal to 10')
    else:
        print(f'x is {x} which is less than 10')
```
* For Loop: 
```py
    for i in range(5):
        print(i)
```
* While Loop:
```py
    count:int = 0
    limit:int = 5

    while count < limit:
        print(count)
        count += 1
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## Functions
* Defining a Function:
```py
    def greet(name):
        return f'Hello {name}!'
```
* Calling a Function:
```py
    print(greet("Alice"))
```
<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## Classes
* Defining a Class:
```py
    class Person:
        def __init__(self,name,age):
            self.,name = name
            self.age = age

        def greet(self):
            return f'Hello, my name is {self.name}.'
```
* Creating and Instance:
```py
    person_1 = Person("Alice",30)
    print(person_1.greet())
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## Exception Handling
* Try/Except:
```py
    try:
            x = 1/0
    except ZeroDivisionError:
        print(f'Can not divide by zero')
    finally:
        print('This will always execute')
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## File Handling
* Reading a File:
```py
    with open('file.txt','r') as file:
        content = file.read()
        print(content)
```
* Writting a File:
```py
    with open('file.txt','w') as file:
        file.write('Hello World')
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## Libraries
* Importing a Library:
```py
    import math
    print(math.sqrt(16))
```
* Using Pandas:
```py
    import pandas as pd
    df = pd.DataFrame({"A":[1,2],"B":[3,4]})
    print(df)
```
* Using NumPy:
```py
    import numpy as np
    array = np.array([1,2,3])
    print(array.mean())
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## List Comprehensions
* Basic List Comprehension
```py
    squares = [x**2 for x in range(10)]
```
<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## Lambda Functions
* Lambda Function
```py
    add = lambda x, y: x + y
    print(add(5,3))
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## main
* dunder (double underscore) main Function
```py
    if __name__ == '__main__':
        main()
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

---

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
###### by Simon A. Betts 03/12/2024
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Links for External -->


<!-- Links for Images -->
[Python_Logo]:assets/images/python_logo.png
[Linux_mascot_tux]: assets/images/Linux_mascot_tux.png