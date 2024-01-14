FROM alpine:3.18.5 as alpine

RUN apk add -U --no-cache ca-certificates

FROM scratch
COPY --from=alpine /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
ENTRYPOINT ["/app"]
USER 65535
# COPY --chown=65535:65535 tmp /
RUN MKDIR /tmp
COPY --chown=65535:65535 app /