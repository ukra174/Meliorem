<metadata>
{
    "created": "26/12/2024",
    "categories": ["2D", "Optimization"]
}
</metadata>

<setup>
import random
import math

random.seed(12345)

class Warehouse:
    def __init__(self, size=20, num_items=20):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.items = []
        for _ in range(num_items):
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if((x,y) in self.items):
                continue
            self.items.append((x, y))
            self.grid[x][y] = 1  # place an item

    def display_grid(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        return self.grid

    def total_distance(self, path):
        distance = 0
        for i in range(1, len(path)):
            distance += math.sqrt((path[i][0] - path[i-1][0]) ** 2 + (path[i][1] - path[i-1][1]) ** 2)
        return distance

    def all_items_collected(self, path):
        collected = set()
        for step in path:
            if step in self.items:
                collected.add(step)
        return len(collected) == len(self.items)

    def reset(self):
        self.__init__(self.size, len(self.items))

warehouse = Warehouse()
print=display
path = None

</setup>

# AI's Quest: Warehouse Optimization

You are tasked with helping our warehouse robots efficiently collect all the items scattered around the warehouse. Your job is to write a Python function that generates the shortest path for the robots to collect all items.

## Instructions

Here's how you interact with the warehouse:

1. **Display the warehouse grid:**
    ```python
    grid = warehouse.display_grid()
    print(grid)
    ```

2. **Define a path for the robot:**
    Example: 
    ```python
    path = [(0, 0), (1, 2), (3, 4), ...]  # You should provide their logic here
    ```

3. **Calculate the total distance of your path:**
    ```python
    total_distance = warehouse.total_distance(path)
    print(total_distance)
    ```

4. **Check if all items have been collected:**
    ```python
    all_collected = warehouse.all_items_collected(path)
    print(all_collected)
    ```

5. **Reset the warehouse for a fresh start:**
    ```python
    warehouse.reset()
    ```

## Your Goal

Write a function that finds the most efficient path to collect all items in the warehouse. The function should return a list of tuples representing the path. Use the  `total_distance`, and `all_items_collected` methods to help you debug and improve your solution.

<check>
if path:

    if warehouse.all_items_collected(path):
        score = 1000 / warehouse.total_distance(path)
        display(f"Score: {score:.2f}")
    else:
        display("Not all items collected!")
else:
    display("No path were created!")
</check>