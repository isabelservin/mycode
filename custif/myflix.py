#!/usr/bin/env python3

#cust bookSeries condtionals
bookSeries = input("Select a series number between 1-4: ")
greeting = "We have a wonderful selection of books! You selected Series #" + bookSeries

if bookSeries == "1":
   greeting = greeting + " Harry Potter! Enjoy."
elif bookSeries == "2":
    greeting = greeting + " Hobbit & Lord of The Rings"
elif bookSeries == "3":
    greeting = greeting + " Chronicles of Narnia"
elif bookSeries == "4":
    greeting = greeting + " Indiana Jones"
else:
    greeting = "Not a valid selection"


print(greeting)
print("Come again soon!")
