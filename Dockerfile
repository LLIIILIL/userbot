FROM debian:latest

#clonning repo 
RUN git clone https://github.com/perdark/per-sed /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt
CMD python3 sedthon.py
