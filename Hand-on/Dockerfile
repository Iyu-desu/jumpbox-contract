FROM ubuntu:22.04
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y python3.11 python3.11-dev python3-pip
RUN pip install -r requirements.txt
RUN rm -rf /bin/cat
RUN rm -rf /bin/touch
RUN rm -rf /bin/ls
EXPOSE 5000
ENTRYPOINT ["flask", "run"]
CMD ["--host=0.0.0.0"]
