FROM python:3.9

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project directory into the image
COPY . .

# Copy lib1.py into the image
COPY lib1.py /app/lib/lib1.py

# Set PYTHONPATH to include the 'lib' directory
ENV PYTHONPATH="${PYTHONPATH}:/app/lib"

CMD ["python", "lambda_function.py"]
