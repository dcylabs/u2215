FROM python:3.12.0b1-alpine3.18
WORKDIR /workdir 
RUN pip3 install flask requests
COPY ./main.py /workdir
RUN chmod +x /workdir/main.py
ENTRYPOINT /workdir/main.py
