def printtext():
    global e
    string = e.get()
    print(string)
def deleteentry():
    global e1
    global e2
    global e3
    global e4

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

f = open("filename.txt", "w+")
f.write(file_path)
#call soil type prediction model
#soil type prediction model reads file for image

root = Tk()
root.title('Questionnaire')


lb1 = Label(root, text="Enter annual rainfall in cm")
lb2 = Label(root, text="Enter month")
lb3 = Label(root, text="Enter annual temperature")
lb4 = Label(root, text="Enter availability of irrigation[Y/N]")

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

lb1.grid(row=0)
lb2.grid(row=1)
lb3.grid(row=2)
lb4.grid(row=3)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

rain = e1.get()
month = e2.get()
temp = e3.get()
irri = e4.get()

b = Button(root, text='okay', command=deleteentry)
b.grid(columnspan=2)


root.mainloop()
