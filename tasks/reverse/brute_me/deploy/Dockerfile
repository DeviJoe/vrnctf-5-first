FROM dellabetta/tcpserver:latest
WORKDIR /tmp
COPY ./pppp .
RUN chmod +x ./pppp
ENTRYPOINT ["tcpserver", "0", "5678", "./pppp"]