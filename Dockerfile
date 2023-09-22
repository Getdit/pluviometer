FROM ubuntu
RUN apt-get update
RUN apt-get install -y apt-utils vim curl openssh-server

RUN echo 'root:{your password here}' | chpasswd
#Allow Root login
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' \
    /etc/ssh/sshd_config

#SSH login fix
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional \
    pam_loginuid.so@g' -i /etc/pam.d/sshd
EXPOSE 22 8004
EXPOSE 80 8005
EXPOSE 443 8006

CMD ["/usr/sbin/sshd","-D"]



