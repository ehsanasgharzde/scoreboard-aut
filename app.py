import os
import tkinter
import winsound
from PIL import Image
from PIL import ImageTk
from files import Files
from plots import Plots
from tkinter import filedialog


class App:
    def __init__(self, path: str = "files/team-scores.csv"):
        self.files = Files(path)
        self.plots = Plots()
        self.dataset = None
        self.canvas = None
        self.path = None
        self.img = None

    def create(self):
        def create():
            columns = featureinput.get().split(", ")

            self.dataset = self.files.create(columns)
            self.files.save(self.dataset)

            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

            master.destroy()

        master = tkinter.Toplevel(self.master)
        frame = tkinter.Frame(master)
        master.title("Create Dateset")
        master.minsize(336, 128)
        master.maxsize(336, 128)

        featurelabel = tkinter.Label(
            frame, text="Enter dataset's features: (comma separated)", highlightthickness=0)
        featurelabel.grid(row=0, column=0, columnspan=2, pady=10)

        featureinput = tkinter.Entry(frame, width=50)
        featureinput.grid(row=1, column=0, pady=10, padx=10)
        featureinput.focus()

        createbutton = tkinter.Button(frame, text="Create", highlightthickness=0, width=14, command=create)
        createbutton.grid(row=2, column=0, pady=10)

        frame.pack()

    def load(self):
        file = filedialog.askopenfilename(
            title="Select", filetypes=[("All files", "*.*")])
        path = os.path.abspath(file)

        self.dataset = self.files.load(path)

    def add(self):
        def add():
            name = nameinput.get()
            time = float(timeinput.get())
            obstacles = float(obstaclesinput.get())
            airtime = float(airtimeinput.get())
            size = float(sizeinput.get())
            qr = float(qrinput.get())
            smartify = float(smartifyinput.get())

            row = {
                "name": [name],
                "time": [time],
                "obstacles": [obstacles],
                "air-time": [airtime],
                "size": [size],
                "qr": [qr],
                "smartify": [smartify],
            }

            self.dataset = self.files.add(self.dataset, row)
            self.files.save(self.dataset)

            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

            master.destroy()

        master = tkinter.Toplevel(self.master)
        frame = tkinter.Frame(master)
        master.title("Add")
        master.minsize(192, 304)
        master.maxsize(192, 304)

        namelabel = tkinter.Label(frame, text="Name:", highlightthickness=0)
        namelabel.grid(row=0, column=0, sticky="w", pady=5)

        nameinput = tkinter.Entry(frame, width=20)
        nameinput.grid(row=0, column=1, sticky="w", pady=5)
        nameinput.focus()

        timelabel = tkinter.Label(frame, text="Time:", highlightthickness=0)
        timelabel.grid(row=1, column=0, sticky="w", pady=5)

        timeinput = tkinter.Entry(frame, width=20)
        timeinput.grid(row=1, column=1, sticky="w", pady=5)

        obstacleslabel = tkinter.Label(
            frame, text="Obstacles:", highlightthickness=0)
        obstacleslabel.grid(row=2, column=0, sticky="w", pady=5)

        obstaclesinput = tkinter.Entry(frame, width=20)
        obstaclesinput.grid(row=2, column=1, sticky="w", pady=5)

        airtimelabel = tkinter.Label(
            frame, text="Air Time:", highlightthickness=0)
        airtimelabel.grid(row=3, column=0, sticky="w", pady=5)

        airtimeinput = tkinter.Entry(frame, width=20)
        airtimeinput.grid(row=3, column=1, sticky="w", pady=5)

        sizelabel = tkinter.Label(frame, text="Size:", highlightthickness=0)
        sizelabel.grid(row=4, column=0, sticky="w", pady=5)

        sizeinput = tkinter.Entry(frame, width=20)
        sizeinput.grid(row=4, column=1, sticky="w", pady=5)

        qrlabel = tkinter.Label(frame, text="QR:", highlightthickness=0)
        qrlabel.grid(row=5, column=0, sticky="w", pady=5)

        qrinput = tkinter.Entry(frame, width=20)
        qrinput.grid(row=5, column=1, sticky="w", pady=5)

        smartifylabel = tkinter.Label(
            frame, text="Smartify:", highlightthickness=0)
        smartifylabel.grid(row=6, column=0, sticky="w", pady=5)

        smartifyinput = tkinter.Entry(frame, width=20)
        smartifyinput.grid(row=6, column=1, sticky="w", pady=5)

        addbutton = tkinter.Button(
            frame, text="Add", highlightthickness=0, width=14, command=add)
        addbutton.grid(row=7, column=0, pady=40, columnspan=2, sticky="")

        frame.pack()

    def calculate(self):
        axis = self.plots.calculate(self.dataset)
        self.path = self.plots.save(axis)

        print(self.path)

    def display(self):
        self.img = Image.open(self.path).resize((368, 276))
        self.img = ImageTk.PhotoImage(self.img, width=368, height=276)
        self.canvas.itemconfigure(self.plot, image=self.img)

    def clear(self):
        self.img = tkinter.PhotoImage(file="plots/default.png", width=368, height=276)
        self.canvas.itemconfigure(self.plot, image=self.img)

    def save(self):
        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

    def launch(self):
        self.master = tkinter.Tk()
        self.master.title("AUT Scoreboard")
        self.master.minsize(896, 416)
        self.master.maxsize(896, 416)

        datasetlabel = tkinter.Label(text="Dataset:", highlightthickness=0)
        datasetlabel.grid(row=0, column=0)

        createbutton = tkinter.Button(text="Create", highlightthickness=0, width=14, height=2, command=self.create)
        createbutton.grid(row=1, column=1, pady=5)

        loadbutton = tkinter.Button(text="Load", highlightthickness=0, width=14, height=2, command=self.load)
        loadbutton.grid(row=2, column=1, pady=5)

        addbutton = tkinter.Button(text="Add", highlightthickness=0, width=14, height=2, command=self.add)
        addbutton.grid(row=3, column=1, pady=5)

        plotlabel = tkinter.Label(text="Plots:", highlightthickness=0)
        plotlabel.grid(row=4, column=0)

        calculatebutton = tkinter.Button(text="Calculate", highlightthickness=0, width=14, height=2, command=self.calculate)
        calculatebutton.grid(row=5, column=1, pady=5)

        displaybutton = tkinter.Button(text="Display", highlightthickness=0, width=14, height=2, command=self.display)
        displaybutton.grid(row=6, column=1, pady=5)

        clearbutton = tkinter.Button(text="Clear", highlightthickness=0, width=14, height=2, command=self.clear)
        clearbutton.grid(row=7, column=1, pady=5)

        savebutton = tkinter.Button(text="Save", highlightthickness=0, width=14, height=2, command=self.save)
        savebutton.grid(row=8, column=1, pady=5)

        self.canvas = tkinter.Canvas(width=640, height=368, background="white")
        image = tkinter.PhotoImage(file="plots/default.png", width=368, height=276)
        self.plot = self.canvas.create_image(320,184, anchor="center", image=image)
        self.canvas.grid(row=1, column=2, rowspan=10, padx=20)

        self.master.mainloop()
