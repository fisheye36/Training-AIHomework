FROM python:3.9

# environment
ENV FLASK_ENV="production"
EXPOSE 8080

HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl -f "http://localhost:8080/health" || exit 1

RUN mkdir /application
WORKDIR /application

RUN pip install --upgrade pip setuptools

# install dependencies
COPY requirements.txt /application
RUN pip install -r requirements.txt

# copy source code
COPY . /application

CMD ["gunicorn", "service:app", "--bind", "0.0.0.0:8080"]
