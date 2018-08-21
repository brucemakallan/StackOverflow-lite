import datetime

from flask import render_template, jsonify, request, make_response

from app import create_app
from app.answer import Answer
from app.data import RawData
from app.question import Question


app = create_app()


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
    if 'question' not in input_data.keys():
        return custom_response(400, 'Bad Request', "Request must contain 'question' data")
    question = input_data['question']
    date_posted = datetime.datetime.now()
    id = RawData().questions[-1].id + 1
    new_question = Question(id, question, date_posted)
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
    if 'answer' not in input_data.keys():
        return custom_response(400, 'Bad Request', "Request must contain 'answer' data")
    answer = input_data['answer']
    date_posted = datetime.datetime.now()
    id = RawData().answers[-1].id + 1
    new_answer = Answer(id, question_id, answer, date_posted)
    RawData().answers.append(new_answer)
    return jsonify(new_answer.obj_to_dict()), 201


def custom_response(status_code, status_message, friendly_message):
    response = make_response(
        jsonify({'status_code': str(status_code) + ': ' + status_message + ', ' + friendly_message}),
        status_code)
    response.headers['Status-Code'] = str(status_code) + ': ' + status_message + ', ' + friendly_message
    return response
