FROM python:3
WORKDIR /usr/scr/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY my_app_test.py .
EXPOSE 5000
CMD ["python3","app.py"]