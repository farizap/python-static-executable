FROM python:3.8-slim as alpine

RUN apt-get update \
  && apt-get install -y ca-certificates \
  && apt-get clean

RUN pip install pyinstaller --no-cache
RUN pip install staticx --no-cache
RUN pyinstaller main.spec
RUN staticx ./dist/main/main ./app

FROM scratch
COPY --from=alpine /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
ENTRYPOINT ["/app"]
USER 65535
RUN ls
COPY --from=alpine --chown=65535:65535 tmp /tmp
COPY --from=alpine --chown=65535:65535 app /