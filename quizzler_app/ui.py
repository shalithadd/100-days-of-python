import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = tk.Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('regular', 12))
        self.label_score.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_textbox = self.canvas.create_text(150,
                                                        125,
                                                        width=280,
                                                        text='',
                                                        font=FONT,
                                                        fill=THEME_COLOR)
        self.canvas.grid(pady=50, row=1, column=0, columnspan=2)

        true_image = tk.PhotoImage(file='../quizzler_app/images/true.png')
        false_image = tk.PhotoImage(file='../quizzler_app/images/false.png')

        self.button_true = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(pady=20, row=2, column=0)

        self.button_false = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(pady=20, row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label_score.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_textbox, text=q_text)
        else:
            self.canvas.itemconfig(self.question_textbox, text='You have reached the end of the quiz!')
            self.button_true.config(state='disabled')
            self.button_false.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)

