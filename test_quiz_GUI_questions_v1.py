from tkinter import *


class answers:
    def __init__(self, partner):
        background = "white"
        question_prompts = [
            "Which country won the 2010 FIFA World Cup?",
            "Which team has won the most Super Rugby titles?",
            "Who has the most All Black caps?",
        ]
        # set up child window (ie answers box)
        self.answers_box = Toplevel()

        # set up GUI frame
        self.answers_frame = Frame(self.answers_box, width=150, pady=10)
        self.answers_frame.grid()


        # set up answers heading
        self.answers_heading = Label(self.answers_frame, text="Question 1",
                                   font=("Arial", "16"),
                                   bg=background, padx=10)
        self.answers_heading.grid(row=0)

        # question text (label, row 1)
        self.answers_text = Label(self.answers_frame, text=question_prompts[1],
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.answers_text.grid(row=1)

        # Answers Frame

        self.A_frame = Frame(self.answers_frame)
        self.A_frame.grid(row=10, pady=10, column=5, padx=10)
        self.A_button = Button(self.A_frame, font="Arial 11 bold",
                                  text="A.  ", width=5)
        self.A_button.grid(row=0, column=20)

        self.B_frame = Frame(self.answers_frame)
        self.B_frame.grid(row=10, pady=10, column=10, padx=10)
        self.B_button = Button(self.B_frame, font="Arial 11 bold",
                                  text="B. ", width=5)
        self.B_button.grid(row=0, column=20)

        self.C_frame = Frame(self.answers_frame)
        self.C_frame.grid(row=10, pady=10, column=15, padx=10)
        self.C_button = Button(self.C_frame, font="Arial 11 bold",
                                  text="C. ", width=5)
        self.C_button.grid(row=0, column=20)

        self.D_frame = Frame(self.answers_frame)
        self.D_frame.grid(row=10, pady=10, column=20, padx=10)
        self.D_button = Button(self.D_frame, font="Arial 11 bold",
                                  text="D. ", width=5)
        self.D_button.grid(row=0, column=20)

    def answer_check(self):
        print()
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sports Quiz")
    something = answers(root)
    root.mainloop()
