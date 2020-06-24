# Tracking http requests

This repository is small web application to get information from host server or container itself.
You can track the http accesses to each container or each host Server by this service.

## Who use it

If you want to test the communications through Load Balancer or Ingress,
maybe this application fit that.

## How it works

This application consist of Django Rest Framework which doesn't have models.
This application have several APIs to get information from each resources like EC2 meta-data or 
Container Network Interface Information and so on.
Each APIs return information is formatted by JSON and just display it.

If you want addtional information from different resources,
you can add APIs by `python3 manage.py startapp <resource name>`.

## How to deploy

There are three ways to deploy this application.

First, `git clone` like below
(Example)
```
$ git clone https://github.com/tuimac/httptracker.git
$ cd httptracker/httptracker
$ python3 manage.py runserver 0.0.0.0:8000
```

Second, you can use the docker image I created.
(Example)
```
$ docker pull tuimac/httptracker:latest
$ docker run -itd --name httptracker -p 8000:8000 tuimac/httptracker:latest
```

Third, use pip3 to install package to your python3 module directory and
create execution command.
(Example)
```
$ pip3 install git+https://github.com/tuimac/httptracker.git
$ httptracker -m start
```
Help of httptracker below:

usage: httptracker [-h] -m MODE [-p PORT] [-i IPADDRESS]

Track HTTP request to the end of the host. ex) httptracker --mode start -p 80

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  [Required]Select modes which are 'start', 'restart', 'stop' to execute httptracker.
  -p PORT, --port PORT  [Optional]Direct port which httptracker process use. Default is 8000/tcp.
  -i IPADDRESS, --ipaddress IPADDRESS
                        [Optional]Direct listen ip address which httptracker process use. Default is 0.0.0.0 .

## Authors

* **Kento Kashiwagi** - [tuimac](https://github.com/tuimac)

If you have some opinion and find bugs, please post [here](https://github.com/tuimac/httptracker/issues).

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/tuimac/httptracker/LICENSE.md) file for details.
