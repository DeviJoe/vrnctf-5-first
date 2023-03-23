FROM dellabetta/tcpserver:latest
WORKDIR /tmp
COPY --chmod=777 ./veryprod .
ENTRYPOINT ["tcpserver", "0", "5678", "./veryprod"]