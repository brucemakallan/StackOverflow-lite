import datetime

from question import Question
from answer import Answer


class RawData:

    def __init__(self):
        # set the lists to empty for every instantiation to avoid repetitions
        self.questions = []
        self.answers = []

        # id, details, date
        self.questions.append(Question(1, "What is a variable?", datetime.date(2018, 8, 1)))
        self.questions.append(Question(2, "What is an interpreted language?", datetime.date(2018, 8, 4)))
        self.questions.append(Question(3, "What does 'dynamically typed' mean?", datetime.date(2018, 8, 7)))
        self.questions.append(Question(4, "What is the difference between a String and an Integer?", datetime.date(2018, 8, 10)))
        self.questions.append(Question(5, "What is a programming language?", datetime.date(2018, 8, 12)))

        # id, question_id, votes, details, date
        self.answers.append(Answer(1, 1, 12, "A storage construct whose value can change", datetime.date(2018, 8, 3)))
        self.answers.append(Answer(2, 1, 22, "A simple link to a location in memory", datetime.date(2018, 8, 4)))
        self.answers.append(Answer(3, 2, 1, "An interpreted language doesn't need to be compiled", datetime.date(2018, 8, 4)))
        self.answers.append(Answer(4, 2, 6, "An interpreted language ... another answer", datetime.date(2018, 8, 7)))
        self.answers.append(Answer(5, 2, 5, "According to ... An interpreted language ... this is yet another answer", datetime.date(2018, 8, 12)))
        self.answers.append(Answer(6, 3, 10, "One does not have to explicitly state the data-type of variables", datetime.date(2018, 8, 10)))
        self.answers.append(Answer(7, 4, 14, "One is Stringy and the other is Integer-ry ;)", datetime.date(2018, 8, 3)))
        self.answers.append(Answer(8, 4, 3, "Strings may contain any ASCII character while Integers do not", datetime.date(2018, 8, 1)))
        self.answers.append(Answer(9, 4, 9, "Strings are ... while Integers are ...", datetime.date(2018, 8, 2)))
        self.answers.append(Answer(10, 4, 7, "This is yet another answers about Strings and Integers", datetime.date(2018, 8, 6)))
