FROM debian:latest

#clonning repo 
RUN git clone https://github.com/perdark/per-sed
#working directory 
WORKDIR /root

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt
CMD python3 sedthon.py
