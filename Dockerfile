
FROM python:3.7-alpine AS final
COPY docker/requirements.txt .
RUN pip3 install -r requirements.txt
RUN apk update && apk add gettext nginx
WORKDIR /opt
RUN mkdir -p /run/nginx
COPY docker/nginx.conf /opt/
COPY app/ .
COPY docker/entrypoint.sh .

ENTRYPOINT [ "sh", "entrypoint.sh" ] 