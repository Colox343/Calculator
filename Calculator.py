from tkinter import *

class Calculator:
    def __init__(self):
        self.operations = []        #List with all the operations to be performed.
        self.delete = False         #Variable to indicate if the data memorized must be deleted.
        self.root = Tk()
        self.WIDTH = self.root.winfo_screenwidth()/7        #Width of the window.
        self.HEIGHT = self.root.winfo_screenheight()/3      #Height of the window.
        self.root.geometry("%dx%d" % (self.WIDTH, self.HEIGHT))     #Set of the dimensions.
        self.root.resizable(0, 0)
        self.root.title("Calculator")
        self.entry1 = Entry(self.root, width=35, justify=RIGHT)     #Text field.
        self.entry1.grid(row=0, columnspan=4)
        self.__create_buttons()     #Creating of buttons.
        self.__insert_buttons()     #Inserting of buttons.

    def __create_buttons(self):     #Creating of buttons
        self.WIDTH_BUTTONS = self.WIDTH/11
        self.HEIGHT_BUTTONS = self.HEIGHT/13
        self.button_1 = Button(self.root, text="1", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,  #Numbers
                               command=lambda: self.__insert_number("1"))
        self.button_2 = Button(self.root, text="2", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("2"))
        self.button_3 = Button(self.root, text="3", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("3"))
        self.button_4 = Button(self.root, text="4", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("4"))
        self.button_5 = Button(self.root, text="5", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("5"))
        self.button_6 = Button(self.root, text="6", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("6"))
        self.button_7 = Button(self.root, text="7", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("7"))
        self.button_8 = Button(self.root, text="8", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("8"))
        self.button_9 = Button(self.root, text="9", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("9"))
        self.button_0 = Button(self.root, text="0", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                               command=lambda: self.__insert_number("0"))

        self.button_div = Button(self.root, text="/", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,    #Actions
                                 command=lambda: self.__action("/"))
        self.button_for = Button(self.root, text="x", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                                 command=lambda: self.__action("*"))
        self.button_minus = Button(self.root, text="-", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                                   command=lambda: self.__action("-"))
        self.button_plus = Button(self.root, text="+", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                                  command=lambda: self.__action("+"))
        self.button_equal = Button(self.root, text="=", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                                   command=lambda: self.__equal())
        self.button_clear = Button(self.root, text="C", padx=self.WIDTH_BUTTONS, pady=self.HEIGHT_BUTTONS,
                                   command=lambda: self.__clear())

    def __insert_buttons(self):     #Inserting of buttons
        self.button_1.grid(row=1, column=0)     #1st row
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.button_div.grid(row=1, column=3)

        self.button_4.grid(row=2, column=0)     #2nd row
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_for.grid(row=2, column=3)

        self.button_7.grid(row=3, column=0)     #3rd row
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.button_minus.grid(row=3, column=3)

        self.button_clear.grid(row=4, column=0)     #4th row
        self.button_0.grid(row=4, column=1)
        self.button_equal.grid(row=4, column=2)
        self.button_plus.grid(row=4, column=3)

    def __clear(self):          #Function connected to the button clear.
        self.entry1.delete(0, END)
        self.operations.clear()

    def __insert_number(self, character):       #Function connected to the number buttons.
        if self.delete:
            self.entry1.delete(0, END)
            self.operations.clear()
            self.delete = False
        self.entry1.insert(len(self.entry1.get()), character)

    def __action(self, op):             #Function connected to the button +-/x.
        if self.delete:
            self.operations.clear()
            self.delete = False
        self.operations.append(self.entry1.get())
        self.operations.append(op)
        self.entry1.delete(0, END)

    def __equal(self):      #Function connected to the button =.
        stop = False        #It indicates if we find or not a division or a multiplication.
        self.operations.append(self.entry1.get())   #update of the operations list.
        self.entry1.delete(0, END)                  #It clears the text-field.
        while not stop:     #It searches a division or a multiplication. If it finds one the cycle repeats.
            stop = True
            for x in self.operations:
                if x=="*" or x=="/":
                    try:            #registeration of the two numbers to process.
                        n1 = int(self.operations[self.operations.index(x)-1])
                    except:
                        n1 = float(self.operations[self.operations.index(x) - 1])
                    n2 = int(self.operations[self.operations.index(x)+1])
                    if x=="*":              #preformance of the operation
                        self.operations[self.operations.index(x)-1] = n1 * n2
                    else:
                        self.operations[self.operations.index(x)-1] = n1 / n2
                    self.operations.pop(self.operations.index(x)+1)         #update of the operations list
                    self.operations.remove(x)
                    stop = False
        while len(self.operations)>1:       #cycle for the additions and subtractions
            n1 = int(self.operations[0])
            n2 = int(self.operations[2])
            if self.operations[1]=="-":
                self.operations[0] = n1 - n2
            else:
                self.operations[0] = n1 + n2
            for x in range(2):
                self.operations.pop(1)
        self.entry1.insert(0, self.operations[0])
        self.delete = True

    def start(self):
        self.root.mainloop()