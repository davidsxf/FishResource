FROM coding-public-docker.pkg.coding.net/public/docker/python:3.8

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]

RUN chmod +x /app/start.sh

CMD ["sh", "start.sh"]

