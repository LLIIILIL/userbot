FROM sandy1709/catuserbot:slim-buster


RUN git clone https://github.com/perdark/per-sed /root/userbot 
WORKDIR /root/userbot
RUN pip3 install -m -r requirements.txt
CMD python3 sedthon.py
