from flask import Flask, render_template, request
from flask import session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'conan_secret'


# 메인 화면
@app.route('/')
def home():
    return render_template('index.html')


# 퀴즈 시작
@app.route('/quiz')
def quiz():

    if 'quiz_list' not in session or not session['quiz_list']:

        count = request.args.get('count', 10, type=int)

        conn = sqlite3.connect('conan.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id
        FROM conan_data
        ORDER BY RANDOM()
        LIMIT ?
        """, (count,))

        rows = cursor.fetchall()

        conn.close()

        session['quiz_list'] = [r[0] for r in rows]
        session['current_index'] = 0
        session['score'] = 0

    current_idx = session['current_index']
    quiz_ids = session['quiz_list']

    current_char_id = quiz_ids[current_idx]

    conn = sqlite3.connect('conan.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ko_name,
           en_name,
           code_name,
           eye_image,
           full_image
    FROM conan_data
    WHERE id = ?
    """, (current_char_id,))

    row = cursor.fetchone()

    conn.close()

    quiz_data = {
        'ko_name': row[0],
        'en_name': row[1],
        'code_name': row[2],
        'eye_image': row[3],
        'full_image': row[4]
    }

    return render_template(
        'quiz.html',
        quiz_data=quiz_data
    )


# 정답 제출
@app.route('/submit', methods=['POST'])
def submit():

    data = request.get_json()

    user_ans = data.get(
        'user_answer',
        ''
    ).strip().lower()

    current_idx = session['current_index']
    quiz_ids = session['quiz_list']

    current_char_id = quiz_ids[current_idx]

    conn = sqlite3.connect('conan.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ko_name,
           en_name,
           code_name,
           eye_image,
           full_image
    FROM conan_data
    WHERE id = ?
    """, (current_char_id,))

    row = cursor.fetchone()

    conn.close()

    quiz_data = {
        'ko_name': row[0],
        'en_name': row[1],
        'code_name': row[2],
        'eye_image': row[3],
        'full_image': row[4]
    }

    db_ko = quiz_data['ko_name'].lower()
    db_en = quiz_data['en_name'].lower()
    db_code = (quiz_data['code_name'] or 'n').lower()
    db_full = quiz_data['full_image']

    is_correct = False

    if db_code != 'n':

        code_en = db_code.split('(')[0].strip()
        code_ko = db_code.split('(')[1].replace(')', '').strip()

        has_code = (
            code_en in user_ans or
            code_ko in user_ans
        )

        has_name = (
            db_ko in user_ans or
            db_en in user_ans
        )

        is_correct = has_code and has_name

    else:

        if (
            user_ans == db_ko or
            user_ans == db_en or
            user_ans.replace(" ", "") ==
            db_en.replace(" ", "")
        ):
            is_correct = True

    if is_correct:
        session['score'] += 1

    return jsonify({
    "is_correct": is_correct,
    "ko_name": db_ko,
    "en_name": db_en,
    "code_name": db_code,
    "full_image": "/static/images/" + db_full
})


# 다음 문제
@app.route('/next_quiz')
def next_quiz():

    session['current_index'] += 1

    current_idx = session['current_index']
    quiz_ids = session['quiz_list']

    # 게임 종료
    if current_idx >= len(quiz_ids):

        score = session['score']

        session.clear()

        return jsonify({
            'game_end': True,
            'score': score
        })

    current_char_id = quiz_ids[current_idx]

    conn = sqlite3.connect('conan.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT eye_image
    FROM conan_data
    WHERE id = ?
    """, (current_char_id,))

    row = cursor.fetchone()

    conn.close()

    return jsonify({

        'game_end': False,

        'eye_image':
            '/static/images/' +
            row[0]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)