import datetime

from flask import Flask, render_template, jsonify, request, make_response, current_app

from answer import Answer
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
    if len(all_questions) == 0:
        return custom_response(204, 'No Content', 'There are no Questions in store')
    return jsonify(all_questions), 200


# get specific question
@app.route("/api/v1/questions/<int:question_id>", methods=['GET'])
def api_quesiton(question_id):
    question_selected = []
    for question_obj in RawData().questions:
        if question_obj.id == question_id:
            question_selected.append(question_obj.obj_to_dict())
            break
    if len(question_selected) == 0:
        return custom_response(404, 'Not Found', 'Question with id:' + str(question_id) + ' does not exist')
    return jsonify(question_selected), 200


# add a question
@app.route("/api/v1/questions", methods=['POST'])
def api_add_question():
    input_data = request.get_json(force=True)
    if 'details' not in input_data.keys():
        return custom_response(400, 'Bad Request', "Request must contain 'details' data")
    details = input_data['details']
    date_posted = datetime.datetime.now()
    id = RawData().questions[-1].id + 1
    new_question = Question(id, details, date_posted)
    RawData().questions.append(new_question)
    return jsonify(new_question.obj_to_dict()), 201


# get all answers
@app.route("/api/v1/questions/<int:question_id>/answers", methods=['GET'])
def api_answers(question_id):
    # turn answer objects (from data file) into dictionaries and store in one list
    all_answers = [answer_obj.obj_to_dict() for answer_obj in RawData().answers if answer_obj.question_id == question_id]
    if len(all_answers) == 0:
        return custom_response(204, 'No Content', 'There are no Answers for the selected question')
    return jsonify(all_answers), 200


# add an answer to a specific question
@app.route("/api/v1/questions/<int:question_id>/answers", methods=['POST'])
def api_add_answer(question_id):
    input_data = request.get_json(force=True)
    if 'details' not in input_data.keys() or 'votes' not in input_data.keys():
        return custom_response(400, 'Bad Request', "Request must contain both 'details' and 'votes' data")
    details = input_data['details']
    votes = input_data['votes']
    date_posted = datetime.datetime.now()
    id = RawData().answers[-1].id + 1
    new_answer = Answer(id, question_id, votes, details, date_posted)
    RawData().answers.append(new_answer)
    return jsonify(new_answer.obj_to_dict()), 201


def custom_response(status_code, status_message, friendly_message):
    response = make_response(
        jsonify({'status_code': str(status_code) + ': ' + status_message + ', ' + friendly_message}),
        status_code)
    response.headers['Status-Code'] = str(status_code) + ': ' + status_message + ', ' + friendly_message
    return response


if __name__ == '__main__':
    app.run(debug=True)
