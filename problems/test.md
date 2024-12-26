
<metadata>

{   
    "created":"24/12/2024",
    "categories":["optimization","test"]
}

</metadata>
<setup>
import math
class A:
    def __init__(self):
        self.data=[]
    def add(self,v):
        self.data.append(v)
    def get(self):
        return(self.data)
a=A()
print=display
</setup>

# Problem 2
Everything begins somewhere!

So this is a *description* of a problem you will be solving today.

Let's also insert a [link]() here.

# 

To solve this problem you will need to write python code here ->

# Python Code Example

```python
def greet(name):
    """
    Function to greet the user with their name.
    """
    if not name:
        return "Hello, Stranger!"
    return f"Hello, {name}!"

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

```

After that click the button "Run!" to try it out!

# 

The scope of your today's task is to fill the list with possibly lot objects!

You can do that calling the function 

`a.add(object_to_add)`

To get the value of the list use

`a.getValue()`

The one with the longest list wins!

# 




<check>
display(f"Your list is: {a.get()}")
display(f"Score: {len(a.get())}")
</check>