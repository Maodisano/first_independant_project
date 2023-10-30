# template recipe

# 1. Describe the problem:

# _Put or write the use story here. Add any clarifying notes you might have._ 
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


# 2. Design the function signature:
# _Include the name of the function, its parameters, return value and side effects._ 

class TaskTracker():
    def add(self, task):

    def list_incomplete():

    def mark_completed():





# 3. Create examples examples as tests:

Initally there are no tasks

tracker = TaskTracker()
tacker.list_incomplete() 
> return - []

test 2

when we add a task it is reflected in the list

tracker = TaskTracker()
tacker.add("Clean kitchen") 
tracker.list_incomplete()
> return - ["Clean kitchen"]

test 3

when we add multiple tasks there are reflected in list

tracker = TaskTracker()
tacker.add("Clean kitchen") 
tacker.add("shopping")
tacker.add("Wash dog")
tracker.list_incomplete()
> return - ["Clean kitchen", "shopping", "wash dog"]

test 4

when we add multiple tasks and one is comleted remove itfrom the list 

tracker = TaskTracker()
tacker.add("Clean kitchen") 
tacker.add("shopping")
tacker.add("Wash dog")
tracker.mark_complete(1)
tracker.list_incomplete()
> return - ["Clean kitchen", "wash dog"]







    