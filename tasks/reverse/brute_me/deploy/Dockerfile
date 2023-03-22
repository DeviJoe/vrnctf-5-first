FROM dellabetta/tcpserver:latest
WORKDIR /tmp
COPY ./pppp .
ENTRYPOINT ["tcpserver", "0", "5678", "./pppp"]