# Tracking http requests

This repository is small web application to get information from host server or container itself.
You can track the http accesses to each container or each host Server by this service.

## Who use it

If you want to test the communications through Load Balancer or Ingress,
maybe this application fit that.

## How it works

This application consist of Django Rest Framework.
This application have several APIs to get information from each resources like EC2 meta-data or 
Container Network Information.
Each APIs return information is formatted by JSON and just display it.

If you want addtional information from different resources,
you can add APIs by `python3 manage.py startapp <resource name>`.

## How to deploy

There are two ways to deploy this application.

First, `git clone` like below
(Example)
```
$ git clone https://github.com/tuimac/httptracker.git
$ cd httptracker/httptracker
$ python3 manage.py runserver localhost:8000
```

Second, you can use the docker image I created.
(Example)
```
$ docker pull tuimac/httptracker:latest
$ docker run -itd --name httptracker -p 8000:8000 tuimac/httptracker:latest
```

## Authors

* **Kento Kashiwagi** - [tuimac](https://github.com/tuimac)

If you have some opinion and find bugs, please post [here](https://github.com/tuimac/httptracker/issues).

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/tuimac/httptracker/LICENSE.md) file for details.
