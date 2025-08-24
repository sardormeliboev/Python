#1. Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

#2. Person Class
from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year
    
    def age(self):
        return date.today().year - self.birth_year

# Test
p = Person("Ali", "Uzbekistan", 2000)
print("Name:", p.name, "| Age:", p.age())

#3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "❌ Division by zero!"

# Test
calc = Calculator()
print(calc.add(10, 5))
print(calc.divide(10, 0))

#4. Shape and Subclasses
import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

# Test
sq = Square(4)
print("Square area:", sq.area())

#5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

# Test
tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(20)
print(tree.search(5) is not None)  # True

#6. Stack Data Structure
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0

# Test
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # 20

#7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.display()

#8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, price):
        self.items[item] = price
    
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
    
    def total_price(self):
        return sum(self.items.values())

# Test
cart = ShoppingCart()
cart.add_item("Book", 10)
cart.add_item("Pen", 2)
print("Total:", cart.total_price())

#9. Stack with Display
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def display(self):
        print("Stack:", self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0

# Test
s = Stack()
s.push(1)
s.push(2)
s.display()

#10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

# Test
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  # 10

#11. Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, balance=0):
        self.accounts[name] = balance
    
    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
    
    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
    
    def get_balance(self, name):
        return self.accounts.get(name, "Account not found")

# Test
bank = Bank()
bank.create_account("Ali", 100)
bank.deposit("Ali", 50)
print("Balance:", bank.get_balance("Ali"))


