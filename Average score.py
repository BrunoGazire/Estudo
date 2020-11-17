class Application():

    def average_score():

        scores = []
        limit = float(input("How many scores would you like to calculate: "))
        i = 1
        while i <= limit:
            scores.append(float(input(" Please enter the score " + str(len(scores) + 1) + ": ")))
            i += 1
        scores.sort()
        scores.pop(0)
        total = sum(scores) // len(scores)
        print("This is your average score ",total)

average_score()
from tkinter import *
root = Tk()
root.mainloop()



