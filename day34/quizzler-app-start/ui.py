import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterfaces:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
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
        self.right_btn = tk.Button(
            image=self.right_btn_img, 
            highlightthickness=0, 
            command=self.right_btn_handle
            )
        self.right_btn.grid(row=2, column=1)
        
        self.wrong_btn = tk.Button(
            image=self.wrong_btn_img, 
            highlightthickness=0,
            command=self.wrong_btn_handle
            )
        self.wrong_btn.grid(row=2, column=0)
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
        
    def right_btn_handle(self):
        self.show_feedback(self.quiz.check_answer("True"))
        # is_right = self.quiz.check_answer("True")
        # self.show_feedback(is_right)
        
    
    def wrong_btn_handle(self):
        self.show_feedback(self.quiz.check_answer("False"))
        # is_right = self.quiz.check_answer("False")
        # self.show_feedback(is_right)
    def show_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
        
        
