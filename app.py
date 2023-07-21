from flask import Flask, request, jsonify, abort, render_template
from flask import *
import socket
import json
from flask_cors import CORS
from crawling.crawling_watcha import crawl_watcha
from crawling.crawling_youtube import crawl_youtube

# 챗봇 엔진 서버 정보
host = "127.0.0.1"      # 챗봇 엔진 서버 IP
port = 5050             # 챗봇 엔진 port

# Flask 애플리케이션
app = Flask(__name__)
cors = CORS(app)


# 전역 변수로 채팅 로그 리스트 초기화
chat_log = []


# 챗봇 엔진 서버와 통신
def get_answer_from_engine(bottype, query):

    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': bottype
    }
    message = json.dumps(json_data)

    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    answer = ret_data['Answer']
    lab = ret_data['label']
    # answer와 lab을 쉼표로 이어서 chat_log에 추가
    chat_log.append(f"{answer},{lab}")

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data

# 챗봇 엔진 서버와 퀴즈
def get_quiz_from_engine(bottype):

    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    if chat_log:
        last_question = chat_log.pop()
        json_data = {
            'Query': last_question,
            'BotType': 'QUIZ'
        }
        message = json.dumps(json_data)

        mySocket.send(message.encode())

        # 챗봇 엔진 답변 출력
        data = mySocket.recv(2048).decode()
        ret_data = json.loads(data)
    else:
        ret_data = {
            'Answer': '대화를 통해 학습을 진행해 보세요.'
        }

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data


# 챗봇 엔진 query 전송 API
@app.route('/query/<bot_type>', methods=['GET', 'POST'])
def query(bot_type):
    body = request.get_json()
    if bot_type == 'NORMAL':
        # 일반 질의응답 API
        ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
        return jsonify(ret)
    elif bot_type == 'QUIZ':
        # 퀴즈출제 API
        ret = get_quiz_from_engine(bottype=bot_type)
        return jsonify(ret)

# 왓차피디아 크롤링
@app.route('/query/crawl_watcha', methods=['GET'])
def crawl_watcha_api():
    request.get_json()
    crawl_watcha()
    return jsonify({'message': 'Watcha crawling complete.'})

# 유튜브 크롤링
@app.route('/query/crawl_youtube', methods=['GET'])
def crawl_youtube_api():
    crawl_youtube()
    return jsonify({'message': 'YouTube crawling complete...'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)