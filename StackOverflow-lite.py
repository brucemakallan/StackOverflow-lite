from flask import Flask, render_template, jsonify

from data import RawData

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


@app.route("/api/v1/questions", methods=['GET'])
def api_questions():
    # turn question objects into dictionaries and store in one list
    all_questions = []
    for question_obj in RawData().questions:
        question_dict = dict()
        question_dict['id'] = question_obj.id
        question_dict['details'] = question_obj.details
        question_dict['date_posted'] = question_obj.date_posted
        all_questions.append(question_dict)
    return jsonify(all_questions)


if __name__ == '__main__':
    app.run()
