FROM python:3.7-alpine as builder
RUN apk update && apk add jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    postgresql-libs \ 
    gcc \
    musl-dev \
    postgresql-dev

COPY docker/requirements.txt .
RUN pip3 install -r requirements.txt

FROM python:3.7-alpine AS final
COPY --from=builder /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
RUN apk update && apk add gettext nginx libpq
WORKDIR /opt
RUN mkdir -p /run/nginx
COPY docker/nginx.conf /opt/
COPY app/ .
COPY docker/entrypoint.sh .

ENTRYPOINT [ "sh", "entrypoint.sh" ] 