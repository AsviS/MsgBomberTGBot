FROM ubuntu:18.04
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN apt update
RUN apt -y upgrade
RUN apt install python3 python3-pip
COPY requirements.txt .
RUN pip3 install -r --no-cache-dir requirements.txt
COPY . .
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
CMD ["bash","start.sh"]