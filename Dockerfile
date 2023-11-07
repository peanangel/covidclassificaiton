#
FROM python:3.9

#
WORKDIR /covid
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

#
COPY ./requirements.txt /covid/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /covid/requirements.txt

#
COPY ./app /covid/app
COPY ./model /covid/model

ENV PYTHONPATH "${PYTHONPATH}:/covid"

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
