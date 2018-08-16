import datetime

from flask import Flask, render_template, jsonify, request

from data import RawData
from question import Question

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', title='Home')


@app.route("/profile")
def profile():
    return render_template('profile.html', title='Profile')


@app.route("/question")
def question():
    return render_template('question.html', title='Question')


@app.route("/questions")
def questions():
    return render_template('questions.html', title='Questions')


@app.route("/signup")
def signup():
    return render_template('signup.html', title='Signup')


# get all questions
@app.route("/api/v1/questions", methods=['GET'])
def api_questions():
    # turn question objects (from data file) into dictionaries and store in one list
    all_questions = [question_obj.obj_to_dict() for question_obj in RawData().questions]
    return jsonify(all_questions)


# get specific question
@app.route("/api/v1/questions/<int:questionId>", methods=['GET'])
def api_quesiton(questionId):
    question_selected = []
    for question_obj in RawData().questions:
        if question_obj.id == questionId:
            question_selected.append(question_obj.obj_to_dict())
            break
    return jsonify(question_selected)


# add a question
@app.route("/api/v1/questions", methods=['POST'])
def api_add_question():
    input_data = request.get_json(force=True)
    details = input_data['details']
    date_posted = datetime.datetime.now()
    id = RawData().questions[-1].id + 1
    new_question = Question(id, details, date_posted)
    RawData().questions.append(new_question)
    return jsonify(new_question.obj_to_dict())


if __name__ == '__main__':
    app.run(debug=True)
