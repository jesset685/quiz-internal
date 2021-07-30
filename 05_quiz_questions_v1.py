from functools import partial  # To prevent unwanted windows.
from tkinter import *
import random


class Quiz:
    def __init__(self, parent):
        # Formatting variables
        self.parent = parent
        background_color = "salmon"


        # quiz Main Screen GUI
        self.quiz_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.quiz_frame.grid()

        self.quiz_label = Label(self.quiz_frame, text="              Quiz               ",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # User Instructions (row 1)
        self.brief_label = Label(self.quiz_frame,
                                             text="Click to begin!",
                                             font="Arial 11 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.brief_label.grid(row=1)

        # Start quiz button frame (row 3)
        self.start_frame = Frame(self.quiz_frame)
        self.start_frame.grid(row=3, pady=10)

        self.start_button = Button(self.start_frame, font="Arial 12 bold",
                                   text="Start Quiz", width=8, padx=5, command=self.start)
        self.start_button.grid(row=0, column=1)

        # History / Help button frame (row 5)
        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        print("You asked for help?")
        get_help = Help(self)
        get_help.help_text.configure(text="Click 'Start Quiz' in order to start the quiz. \n"
                                          "Four answers will be shown on the window labelled through A-D. \n"
                                          "\nNote that there will be a timer from 20 seconds.")
    def start(self):
        get_start = Start(self)


class Start:
    def __init__(self, partner):
        background = "white"
        question_prompts = [
            "Which country won the 2010 FIFA World Cup?",
            "Which team has won the most Super Rugby titles?",
            "Who has the most All Black caps?",
        ]
        # set up child window (ie start box)
        self.start_box = Toplevel()

        # set up GUI frame
        self.start_frame = Frame(self.start_box, width=300, bg=background,
                                 pady=10)
        self.start_frame.grid()

        # set up start heading
        self.start_heading = Label(self.start_frame, text="Question 1",
                                   font=("Arial", "16"),
                                   bg=background, padx=10)
        self.start_heading.grid(row=0)

        # question text (label, row 1)
        self.start_text = Label(self.start_frame, text=question_prompts[1],
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.start_text.grid(row=1)

        # Answers Frame
        self.answers_frame = Frame(self.start_frame)
        self.answers_frame.grid(row=0)

        self.A_frame = Frame(self.start_frame)
        self.A_frame.grid(row=0, pady=10, column=5, padx=10)
        self.A_button = Button(self.A_frame, font="Arial 11 bold",
                                  text="A. Hurricanes", width=5, bg="red")
        self.A_button.grid(row=0, column=20)

        self.B_frame = Frame(self.start_frame)
        self.B_frame.grid(row=0, pady=10, column=10, padx=10)
        self.B_button = Button(self.B_frame, font="Arial 11 bold",
                                  text="B. Blues", width=5, bg="green")
        self.B_button.grid(row=0, column=20)

        self.C_frame = Frame(self.start_frame)
        self.C_frame.grid(row=0, pady=10, column=15, padx=10)
        self.C_button = Button(self.C_frame, font="Arial 11 bold",
                                  text="C. Crusaders", width=5, bg="lightBlue")
        self.C_button.grid(row=0, column=20)

        self.D_frame = Frame(self.start_frame)
        self.D_frame.grid(row=0, pady=10, column=20, padx=10)
        self.D_button = Button(self.D_frame, font="Arial 11 bold",
                                  text="D. Brumbies", width=5, bg="Orange")
        self.D_button.grid(row=0, column=20)

    def answer_check(self):
        print()

class Help:
    def __init__(self, partner):
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie help box)
        self.help_box = Toplevel()

        # if user press cross at top, closes help and releases button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background,
                                pady=10)
        self.help_frame.grid()

        # set up help heading
        self.how_heading = Label(self.help_frame, text="Help & Information",
                                 font=("Arial", "16", "bold"),
                                 bg=background, padx=10)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="Enter a number in the box...",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sports Quiz")
    something = Quiz(root)
    root.mainloop()
