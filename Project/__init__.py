from tkinter import *
from data import *
""" Import all frames in the application here """
from student import student
from login import login
from takeTest import takeTest
from summativeTestFeedback import summativeTestFeedback
from viewAnswerStudent import viewAnswerStudent
from lecturer import lecturer
from createTest import createTest
from formativeTestFeedback import formativeTestFeedback
from Modify import Modify
from modifyTest import modifyTest
from viewTest import viewTest
from viewTestSummativeLecturer import viewTestSummativeLecturer
from viewIndividualTestSummativeLecturer import viewIndividualTestSummativeLecturer
from statsGen import statsView,Result
from viewTestFormativeLecturer import viewTestFormativeLecturer
from viewIndividualTestFormativeLecturer import viewIndividualTestFormativeLecturer

class App(Tk):
    def __init__(self):
        """
            Initialise the frames imported and move Login Frame to front.
        """
        Tk.__init__(self)

        self.current_frame = None
        self.pages = {'Login': login,
                 'Student': student,
                 'takeTest': takeTest,
                 'summativeTestFeedback': summativeTestFeedback,
                 'viewAnswerStudent': viewAnswerStudent,
                 "Lecturer": lecturer,
                 "createTest": createTest,
                 'formativeTestFeedback': formativeTestFeedback,
                 'modify': Modify,
                 'modifyTest': modifyTest,
                 'viewTest': viewTest,
                 'viewTestSummativeLecturer': viewTestSummativeLecturer,
                 'viewIndividualTestSummativeLecturer': viewIndividualTestSummativeLecturer,
                 'viewStats': statsView,
                 'viewTestFormativeLecturer': viewTestFormativeLecturer,
                 'viewIndividualTestFormativeLecturer': viewIndividualTestFormativeLecturer
                 }

        self.switch_frame('Login')

    def switch_frame(self, frame_name):
        """
            Destroys current frame and replaces it with a new one.
        """
        if self.current_frame is not None:
            self.current_frame.destroy()
        print(str(frame_name))

        new_frame = self.pages[frame_name](self)
        self.current_frame = new_frame

        self.current_frame.pack(side=TOP, fill='both', expand=True)



def main():
    app = App()
    app.title('Application')
    app.state('zoomed')
    app.mainloop()

if __name__ == '__main__':
    main()
