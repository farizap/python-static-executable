FROM python:3.8 as builder

WORKDIR /app
COPY . .
RUN apt-get update \
  && apt-get install -y ca-certificates \
  && apt-get clean

RUN pip install pyinstaller staticx patchelf==0.17.0 --no-cache 

RUN pyinstaller main.spec 
RUN ls 
RUN dist 
RUN staticx ./dist/main /app

FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

ENTRYPOINT ["/app"]
USER 65535
COPY --from=builder --chown=65535:65535 /tmp /tmp
COPY --from=builder --chown=65535:65535 /app /