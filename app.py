import tkinter as tk

class BookPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        # Create the application variable.
        self.id = tk.IntVar()
        self.name = tk.StringVar()
        self.subject = tk.StringVar()

        tk.Label(self, text="Id").grid(row=0, column=0)
        tk.Label(self, text="Name").grid(row=1, column=0)
        tk.Label(self, text="Subject").grid(row=2, column=0)

        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1)
        self.id_entry["textvariable"] = self.id


        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1)
        self.name_entry["textvariable"] = self.name


        self.subject_entry = tk.Entry(self)
        self.subject_entry.grid(row=2, column=1)
        self.subject_entry["textvariable"] = self.subject_entry

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        #self.entrythingy.bind('<Key-Return>', self.print_contents)

        self.submit_button = tk.Button(self, command=self.handle_submit, text='Submit',width=20,bg='brown',fg='white', height=2).grid(row=3)

    def handle_submit(self, event = None):
        firstname = self.id.get()
        lastname = self.name.get()
        personnr = self.subject.get()
        valid = all([firstname != "",
                lastname != "",
                personnr != ""
                ])

        if valid: self.submit_callback()

    def submit_callback(self):
        print(
            self.id.get(),
            self.name.get(),
            self.subject.get()
              )

class StudentPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        # Create the application variable.
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.personnr = tk.StringVar()

        tk.Label(self, text="First Name").grid(row=0, column=0)
        tk.Label(self, text="Last Name").grid(row=1, column=0)
        tk.Label(self, text="Person Number").grid(row=2, column=0)

        self.firstname_entry = tk.Entry(self)
        self.firstname_entry.grid(row=0, column=1)
        self.firstname_entry["textvariable"] = self.firstname


        self.lastname_entry = tk.Entry(self)
        self.lastname_entry.grid(row=1, column=1)
        self.lastname_entry["textvariable"] = self.lastname


        self.personnr_entry = tk.Entry(self)
        self.personnr_entry.grid(row=2, column=1)
        self.personnr_entry["textvariable"] = self.personnr

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        #self.entrythingy.bind('<Key-Return>', self.print_contents)

        self.submit_button = tk.Button(self, command=self.handle_submit, text='Submit',width=20,bg='brown',fg='white', height=2).grid(row=4)

    def handle_submit(self, event = None):
        firstname = self.firstname.get()
        lastname = self.lastname.get()
        personnr = self.personnr.get()
        valid = all([firstname != "",
                lastname != "",
                personnr != ""
                ])

        if valid: self.submit_callback()

    def submit_callback(self):
        print(
            self.firstname.get(),
            self.lastname.get(),
            self.personnr.get()
              )

class App(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}


        menubar = tk.Menu(self)
        menubar.add_command(label="student", command= lambda : self.show_frame(StudentPage))
        menubar.add_command(label="book", command= lambda : self.show_frame(BookPage))

        self.config(menu=menubar)

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StudentPage, BookPage):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StudentPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

