FROM debian:latest

RUN apt update && apt upgrade -y
RUN pip3 install --no-cache-dir -r requirements.txt

CMD python3 sedthon.py
