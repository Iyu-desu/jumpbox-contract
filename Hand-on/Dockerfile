FROM alpine:latest
WORKDIR /app
COPY . .
RUN apk add --no-cache python3 py3-pip
RUN python3 -m venv /app/venv
RUN . /app/venv/bin/activate && pip install -r requirements.txt
RUN rm -rf /bin/cat
RUN rm -rf /bin/touch
RUN rm -rf /bin/ls
EXPOSE 5000
ENTRYPOINT ["flask", "run"]
CMD ["--host=0.0.0.0"]
