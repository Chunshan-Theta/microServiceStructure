#FROM python:3.7.3-alpine
FROM  python:3.7
EXPOSE 8088


WORKDIR /app
ADD . /app

#Using pip:
RUN python -m pip install -r requirements.txt
RUN apt-get update

CMD /bin/bash
CMD python3 server.py
