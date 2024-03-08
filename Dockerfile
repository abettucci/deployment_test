FROM python:3.9

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Lambda function code
COPY lambda_function.py .

CMD ["python", "lambda_function.py"]
