#Homework 1: ToDo List Application
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'Incomplete'

    def mark_complete(self):
        self.status = 'Complete'

    def __str__(self):
        return f"{self.title} - {self.description} - Due: {self.due_date} - Status: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_all_tasks(self):
        return [str(task) for task in self.tasks]

    def list_incomplete_tasks(self):
        return [str(task) for task in self.tasks if task.status == 'Incomplete']

# Main CLI Program
def todo_cli():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List ---")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added.")
        elif choice == '2':
            title = input("Task title to mark complete: ")
            if todo.mark_task_complete(title):
                print("Task marked complete.")
            else:
                print("Task not found.")
        elif choice == '3':
            print("\nAll Tasks:")
            for task in todo.list_all_tasks():
                print(task)
        elif choice == '4':
            print("\nIncomplete Tasks:")
            for task in todo.list_incomplete_tasks():
                print(task)
        elif choice == '5':
            break
        else:
            print("Invalid option.")

# Uncomment to run
# todo_cli()

#Homework 2: Simple Blog System
from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def edit(self, title=None, content=None):
        if title:
            self.title = title
        if content:
            self.content = content

    def __str__(self):
        return f"{self.title} by {self.author} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}\n{self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return [str(post) for post in self.posts]

    def posts_by_author(self, author):
        return [str(post) for post in self.posts if post.author == author]

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                post.edit(new_title, new_content)

    def latest_posts(self, n=5):
        return [str(post) for post in sorted(self.posts, key=lambda p: p.timestamp, reverse=True)[:n]]

# Main CLI Program
def blog_cli():
    blog = Blog()
    while True:
        print("\n--- Simple Blog ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
            print("Post added.")
        elif choice == '2':
            for post in blog.list_posts():
                print(post, "\n")
        elif choice == '3':
            author = input("Author: ")
            for post in blog.posts_by_author(author):
                print(post, "\n")
        elif choice == '4':
            title = input("Title of post to delete: ")
            blog.delete_post(title)
            print("Post deleted.")
        elif choice == '5':
            title = input("Title of post to edit: ")
            new_title = input("New title (leave blank to skip): ")
            new_content = input("New content (leave blank to skip): ")
            blog.edit_post(title, new_title or None, new_content or None)
            print("Post updated.")
        elif choice == '6':
            for post in blog.latest_posts():
                print(post, "\n")
        elif choice == '7':
            break
        else:
            print("Invalid option.")

# Uncomment to run
# blog_cli()

#Homework 3: Simple Banking System
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account: {self.acc_number} - {self.holder_name} - Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_number] = account

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver and sender.withdraw(amount):
            receiver.deposit(amount)
            return True
        return False

# Main CLI Program
def bank_cli():
    bank = Bank()
    while True:
        print("\n--- Simple Bank System ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            acc_number = input("Account Number: ")
            holder_name = input("Holder Name: ")
            balance = float(input("Initial Balance: "))
            bank.add_account(Account(acc_number, holder_name, balance))
            print("Account created.")
        elif choice == '2':
            acc_number = input("Account Number: ")
            acc = bank.get_account(acc_number)
            print(f"Balance: ${acc.balance:.2f}" if acc else "Account not found.")
        elif choice == '3':
            acc_number = input("Account Number: ")
            amount = float(input("Amount to deposit: "))
            acc = bank.get_account(acc_number)
            if acc:
                acc.deposit(amount)
                print("Deposit successful.")
            else:
                print("Account not found.")
        elif choice == '4':
            acc_number = input("Account Number: ")
            amount = float(input("Amount to withdraw: "))
            acc = bank.get_account(acc_number)
            if acc and acc.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds or account not found.")
        elif choice == '5':
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Amount to transfer: "))
            if bank.transfer(from_acc, to_acc, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed.")
        elif choice == '6':
            acc_number = input("Account Number: ")
            acc = bank.get_account(acc_number)
            print(acc if acc else "Account not found.")
        elif choice == '7':
            break
        else:
            print("Invalid option.")

# Uncomment to run
# bank_cli()
