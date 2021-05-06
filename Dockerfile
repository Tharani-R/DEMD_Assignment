FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python main.py