FROM alpine:latest

WORKDIR /root

EXPOSE 80

ADD requirements.txt /root/requirements.txt

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash git icu-dev ncurses icu-libs vim python3 py3-pip curl jq tree && \
    mkdir /etc/vim/backup && \
    mkdir /etc/vim/undo && \
    pip3 install -r requirements.txt && \
 	rm /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/vim/vimrc -o /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/linux/bashrc/.bashrc_node_docker -o /root/.bashrc && \
    git clone https://github.com/tuimac/servertools && \
    git config --global user.email "tuimac.devadm01@gmail.com" && \
    git config --global user.name "tuimac" && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/git/hook/servertools/pre-commit -o .git/hooks/pre-commit && \
    chmod +x .git/hooks/pre-commit && \

CMD ["python3", "/root/servertools/src/backend/manage.py", "runserver", "0.0.0.0:80"]
