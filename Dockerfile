# Use the existing Flask app image as a base image
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
