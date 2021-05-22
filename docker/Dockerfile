FROM alpine:latest

WORKDIR /root

EXPOSE 80

ADD requirements.txt /root/requirements.txt

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash git icu-dev ncurses icu-libs vim python3 py3-pip nodejs nodejs-npm curl jq tree && \
    mkdir /etc/vim/backup && \
    mkdir /etc/vim/undo && \
    pip3 install -r requirements.txt && \
 	rm /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/vim/vimrc -o /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/linux/bashrc/.bashrc_node_docker -o /root/.bashrc && \
    git clone https://github.com/tuimac/servertools && \
    git config --global user.email "tuimac.devadm01@gmail.com" && \
    git config --global user.name "tuimac" && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/git/hook/servertools/pre-commit -o servertools/.git/hooks/pre-commit && \
    chmod +x servertools/.git/hooks/pre-commit && \
    echo $'\n\
echo -en "\e[1m\e[34m" \n\
cat << "EOF" \n\
\n\
   ___________ _   _________     __________  ____  __   ____\n\
  / __/ __/ _ \ | / / __/ _ \___/_  __/ __ \/ __ \/ /  / __/\n\
 _\ \/ _// , _/ |/ / _// , _/___// / / /_/ / /_/ / /___\ \  \n\
/___/___/_/|_||___/___/_/|_|    /_/  \____/\____/____/___/  \n\
                                                            \n\
EOF' >> /root/.bashrc && \
    cd servertools/src/frontend && \
    npm install && \
    npm build && \
    cp -r build/* /root/servertools/src/backend/template/

CMD ["python3", "/root/servertools/src/backend/manage.py", "runserver", "0.0.0.0:80"]
