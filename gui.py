import tkinter as tk
from tkinter import Button
from PIL import Image, ImageDraw
from predict import predict_digit

class App:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.root.title("Handwritten Digit Recognizer")
        heading = tk.Label(
        self.root,
        text="Handwritten Digit Recognizer",
        font=("Arial",18,"bold"),
        bg="#f5f5f5"
    )
        heading.pack(pady=10)
        self.canvas = tk.Canvas(
            self.root,
            width=280,
            height=280,
            bg="white"
        )

        self.canvas.pack()

        self.image = Image.new("L",(280,280),255)
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>",self.paint)

        Button(
    self.root,
    text="Predict",
    bg="#4CAF50",
    fg="white",
    font=("Arial",12,"bold"),
    command=self.predict
).pack(pady=5)
        
        Button(
    self.root,
    text="Clear",
    bg="#f44336",
    fg="white",
    font=("Arial",12,"bold"),
    command=self.clear
).pack(pady=5)
        
        self.result = tk.Label(
    self.root,
    text="Draw a digit",
    font=("Arial",14,"bold"),
    bg="#f5f5f5"
)

        self.result.pack()

        self.root.mainloop()

    def paint(self,event):

        x = event.x
        y = event.y

        r = 8

        self.canvas.create_oval(
            x-r,
            y-r,
            x+r,
            y+r,
            fill="black",
            outline="black"
        )

        self.draw.ellipse(
            (x-r,y-r,x+r,y+r),
            fill=0
        )

    def predict(self):

        self.image.save("digit.png")

        digit,confidence = predict_digit("digit.png")

        self.result.config(
            text=f"Digit : {digit}    Confidence : {confidence:.2f}%"
        )

    def clear(self):

        self.canvas.delete("all")

        self.draw.rectangle(
            (0,0,280,280),
            fill=255
        )

        self.result.config(
            text="Draw a digit"
        )