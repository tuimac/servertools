FROM alpine:latest

WORKDIR /root

EXPOSE 8000

ADD requirements.txt /root/requirements.txt

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash git icu-dev ncurse icu-libs vim python3 py3-pip curl jq tree && \
    git clone https://github.com/tuimac/httptracker && \
    mkdir /etc/vim/backup && \
    mkdir /etc/vim/undo && \
    pip3 install -r requirements.txt && \
 	rm /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/vim/vimrc -o /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/linux/bashrc/.bashrc_node_docker -o /root/.bashrc

CMD ["python3", "/root/httptracker/manage.py", "runserver", "0.0.0.0:8000"]
