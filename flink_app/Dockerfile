FROM flink:1.18

USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl && \
    ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /flink_app

COPY . /flink_app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

RUN sed -i 's/\r$//' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
