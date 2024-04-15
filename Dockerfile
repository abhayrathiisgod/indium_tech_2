FROM python 

ENV PYTHONUNBUFFERED 1

WORKDIR /CODE

COPY req.txt .
RUN pip install -r req.txt
COPY . .
EXPOSE 8000
CMD ["python3","manage.py","runserver"]



