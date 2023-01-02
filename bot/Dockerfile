FROM python:3.11-alpine

WORKDIR /app

ENV APP_NAME="theatreBot"

COPY requirements.txt requirements.txt
RUN set -e \
&& pip install --no-cache-dir -r requirements.txt \
&& rm -rf ..?* .[!.]* * \
&& set +e \

ENV PYTHONPATH="/app/"
ENV APP_DIR="/app/"
ENV APP_BIN="${APP_DIR}main.py"

COPY .. ./

CMD [ "/bin/sh", "-c", "python ${APP_BIN}" ]

