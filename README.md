# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

UI URL:
https://brucemakallan.github.io/StackOverflow-lite/UI/


Travis CI [![Build Status](https://travis-ci.com/brucemakallan/StackOverflow-lite.svg?branch=master)](https://travis-ci.com/brucemakallan/StackOverflow-lite)
Coveralls [![Coverage Status](https://coveralls.io/repos/github/brucemakallan/StackOverflow-lite/badge.svg?branch=master)](https://coveralls.io/github/brucemakallan/StackOverflow-lite?branch=master)

## Main Features
1. Users can create an account and log in.
2. Users can post questions.
3. Users can delete the questions they post.
4. Users can post answers.
5. Users can view the answers to questions.
6. Users can accept an answer out of all the answers to his/her question as the preferred answer.

## API Endpoints
The API is hosted on Heroku at:
```
https://stackoverflow-lite-abm.herokuapp.com
```

### Fetch all questions:
```
GET /api/v1/questions
```
For example: https://stackoverflow-lite-abm.herokuapp.com/api/v1/questions

### Fetch a specific question
```
GET /api/v1/questions/<questionId>
```
For example: https://stackoverflow-lite-abm.herokuapp.com/api/v1/questions/1

### Add a question
```
POST /api/v1/questions
```
Provide POST data in JSON format e.g.
```
{
    "question": "Sample text"
}
```

### Get all answers for a specific question
```
GET /api/v1/questions/<questionId>/answers
```
For example: https://stackoverflow-lite-abm.herokuapp.com/api/v1/questions/1/answers

### Add an answer
```
POST /api/v1/questions/<questionId>/answers
```
Provide POST data in JSON format e.g.
```
{
    "answer": "Sample text"
}
```