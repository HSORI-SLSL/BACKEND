# 베이스 이미지 설정
FROM nvcr.io/nvidia/tensorrt:19.03-py3

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일을 컨테이너에 복사
COPY app.py .
COPY chatbot.py .

# Flask 애플리케이션 실행
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


'''# Use the existing Flask app image as a base image
FROM python:3

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the Flask app source code and requirements file
COPY requirements.txt ./
COPY app.py ./
COPY chatbot.py ./  # Add the chatbot.py file

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the ports for both Flask and chatbot
EXPOSE 5000
EXPOSE 5050

# Command to start both Flask app and chatbot
CMD [ "python", "./app.py" ]
'''