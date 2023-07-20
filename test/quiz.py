import socket
import json

# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"
port = 5050

# 클라이언트 프로그램 시작
chat_log=["짐의 이름은 이도이니라.,0","짐은 조선의 제4대 왕이다.,0","6조 직계제는 국정 운영에서 국왕의 역할을 강화시켰으나, 반면 국왕이 막대한 업무량에 시달려야 하는 단점이 있었다네. 이에 따라 짐의 통치시절에는 나의 건강 악화로 인하여 의정부 서사제가 다시 부활하였지.,2"]

# 챗봇 엔진 서버 연결
mySocket = socket.socket()
mySocket.connect((host, port))

while chat_log:
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

        print("퀴즈 : ")
        print(ret_data['Answer'])
        print("\n")
        print("답 : ")
        print(ret_data['label'])
        print("\n")

    else:
        ret_data = {
            'Answer': '대화를 통해 학습을 진행해 보세요.'
        }


# 챗봇 엔진 서버 연결 소켓 닫기
mySocket.close()