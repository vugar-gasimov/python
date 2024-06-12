import tkinter as tk

THEME_COLOR = "#375362"

class QuizInterfaces:
    def __init__(self):
        self.window = tk.Tk(className="Quizzler")
        self.window.title("Quizzler")
        self.window.config(
            padx=30, 
            pady=30, 
            background=THEME_COLOR
            )
        self.canvas = tk.Canvas(
            width=400, 
            height=300, 
            background="white"
            )
        self.canvas.grid(
            row=1, 
            column=0, 
            columnspan=2, 
            pady=50
            )
        self.score=0
        self.score_text= tk.Label(
            self.window, 
            text=f"Score: {self.score}", 
            background=THEME_COLOR, 
            font=("Arail", 16), 
            fg="white",  
            )
        self.score_text.grid(
            row=0, 
            column=1 )
        self.question_text = self.canvas.create_text(
            200, 
            150, 
            text="Questions ?", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR, 
            width=280
            )
        self.right_btn_img = tk.PhotoImage(file=fr"day34\quizzler-app-start\images\true.png")
        self.wrong_btn_img = tk.PhotoImage(file=fr"day34\quizzler-app-start\images\false.png")
        self.right_btn = tk.Button(image=self.right_btn_img, highlightthickness=0, )
        self.right_btn.grid(row=2, column=1)
        self.wrong_btn = tk.Button(
            image=self.wrong_btn_img, 
            highlightthickness=0,
            )
        self.wrong_btn.grid(row=2, column=0)
        
        
        self.window.mainloop()