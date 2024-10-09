from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import UserResult
from . import db, quiz_questions

main = Blueprint('main', __name__)

@main.route('/')
def index():
    highscore = UserResult.query.order_by(UserResult.score.desc()).first()
    return render_template('index.html', highscore=highscore.score if highscore else 0)

@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0
        session['answers'] = []

    if request.method == 'POST':
        selected_option = request.form.get('answer')
        question_index = session['current_question']
        correct_answer = quiz_questions[question_index]['answer']

        if selected_option == correct_answer:
            session['score'] += 1

        session['answers'].append(selected_option)
        session['current_question'] += 1

        if session['current_question'] >= len(quiz_questions):
            new_result = UserResult(session['score'])
            db.session.add(new_result)
            db.session.commit()
            return redirect(url_for('main.result'))

    question_index = session['current_question']
    question = quiz_questions[question_index]
    total = len(quiz_questions)
    highscore = UserResult.query.order_by(UserResult.score.desc()).first()
    return render_template('quiz.html', question=question, question_number=question_index+1, total=total, highscore=highscore.score if highscore else 0)

@main.route('/result')
def result():
    score = session.get('score', 0)
    total = len(quiz_questions)
    highscore = UserResult.query.order_by(UserResult.score.desc()).first()

    session.pop('current_question', None)
    session.pop('answers', None)
    session.pop('score', None)

    return render_template('result.html', score=score, total=total, highscore=highscore.score if highscore else 0)