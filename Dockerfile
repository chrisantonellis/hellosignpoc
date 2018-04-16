# debian & python3.7
FROM python:3.7-rc
RUN apt-get update && apt-get -y upgrade

# pip requirements
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# add app
ADD ./app /app

# open ports
EXPOSE 5000

# run forever
CMD tail -f /dev/null
