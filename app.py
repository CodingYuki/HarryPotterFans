from flask import Flask, render_template, request, jsonify, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 生成随机密钥

# 分院帽问题
sorting_hat_questions = [
    {
        "question": "你最看重什么？",
        "options": [
            {"text": "勇气", "house": "Gryffindor"},
            {"text": "智慧", "house": "Ravenclaw"},
            {"text": "忠诚", "house": "Hufflepuff"},
            {"text": "野心", "house": "Slytherin"}
        ]
    },
    {
        "question": "你最喜欢的魔法课程是什么？",
        "options": [
            {"text": "黑魔法防御术", "house": "Gryffindor"},
            {"text": "魔咒课", "house": "Ravenclaw"},
            {"text": "草药课", "house": "Hufflepuff"},
            {"text": "魔药课", "house": "Slytherin"}
        ]
    }
]

# 哈利波特问答题目
quiz_questions = [
    {
        "question": "哈利波特的第一根魔杖是什么材质的？",
        "options": ["冬青木", "橡木", "柳木", "山毛榉木"],
        "correct": 0
    },
    {
        "question": "霍格沃茨的四个学院分别是什么？",
        "options": ["格兰芬多、拉文克劳、赫奇帕奇、斯莱特林", 
                   "格兰芬多、拉文克劳、赫奇帕奇、斯莱特林", 
                   "格兰芬多、拉文克劳、赫奇帕奇、斯莱特林", 
                   "格兰芬多、拉文克劳、赫奇帕奇、斯莱特林"],
        "correct": 0
    }
]

@app.route('/')
def index():
    print("访问主页")  # 添加调试信息
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    print("访问问答页面")  # 添加调试信息
    return render_template('quiz.html')

@app.route('/sorting-hat')
def sorting_hat():
    print("访问分院帽测试页面")  # 添加调试信息
    return render_template('sorting_hat.html')

@app.route('/game')
def game():
    print("访问游戏页面")  # 添加调试信息
    return render_template('game.html')

@app.route('/school-song')
def school_song():
    print("访问校歌页面")  # 添加调试信息
    return render_template('school_song.html')

@app.route('/api/quiz-question')
def get_quiz_question():
    question = random.choice(quiz_questions)
    return jsonify(question)

@app.route('/api/sorting-hat-question')
def get_sorting_hat_question():
    question = random.choice(sorting_hat_questions)
    return jsonify(question)

@app.route('/api/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    return jsonify({"message": "提交成功"})

@app.route('/api/submit-sorting', methods=['POST'])
def submit_sorting():
    data = request.get_json()
    return jsonify({"house": "Gryffindor"})

if __name__ == '__main__':
    print("启动Flask应用...")  # 添加调试信息
    app.run(host='0.0.0.0', port=5000, debug=True) 