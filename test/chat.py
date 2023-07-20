import socket
import json

# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"
port = 5050
# 전역 변수로 채팅 로그 리스트 초기화
chat_log = []
# 클라이언트 프로그램 시작
while True:
    print("질문 : ")
    query = input()
    if(query == "exit"):
        exit(0)
    print("-" * 40)

    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': "NORMAL"
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

    print("답변 : ")
    print(ret_data['Answer'])
    print("\n")
    print("레이블 : ")
    print(ret_data['label'])
    print("\n")

# 챗봇 엔진 서버 연결 소켓 닫기
mySocket.close()