FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
RUN pip install django ptvsd
ENV PYTHONUNBUFFERED 1
RUN mkdir /code/
WORKDIR /code/
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code/
ADD ./demo_site.conf /etc/apache2/sites-available/demo_site.conf
RUN a2ensite demo_site.conf
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod proxy_balancer
RUN a2enmod lbmethod_byrequests
RUN service apache2 start
RUN service apache2 reload
EXPOSE 80 3500
CMD ["apache2ctl", "-D", "FOREGROUND"]