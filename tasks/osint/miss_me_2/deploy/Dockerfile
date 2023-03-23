FROM dellabetta/tcpserver:latest
WORKDIR /tmp
COPY ./veryprod .
RUN chmod a+x ./veryprod
ENTRYPOINT ["tcpserver", "0", "5679", "./veryprod"]