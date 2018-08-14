from flask import Flask, render_template, url_for

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


if __name__ == '__main__':
    app.run(debug=True)
