class Question:

    def __init__(self, id, details, date_posted):
        self.id = id
        self.details = details
        self.date_posted = date_posted

    def obj_to_dict(self):
        question_dict = dict()
        question_dict['id'] = self.id
        question_dict['details'] = self.details
        question_dict['date_posted'] = self.date_posted
        return question_dict
