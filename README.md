# Information of docker container through HTTP

[![CircleCI](https://circleci.com/gh/tuimac/servertools.svg?style=shield)](https://circleci.com/gh/tuimac/servertools)

This repository is small web application to get information from host server or container itself.
You can track the http accesses to each container or each host Server by this service.

## Who use it

If you want to test the communications through Load Balancer or Ingress, some container deployment services, this application will fit that demand.

## Functions
- Runcommand<br>
You can run command through web terminal. This function was implemented by [Xtermjs](https://xtermjs.org/).
The command send to servertool's container and run within that container.
(You can't use Vim now...)

- Server Information API<br>
Servertool's landing page provide some information of host server and contaner. This API gather information from EC2 instance so servertool works on only AWS services.

## Technology
- Frontend<br>
Framework is React with bootstrap UI.

- Backend
Using Django Rest Framework. Runcommand use Websocket so /runcommand use [Django Channels](https://channels.readthedocs.io/en/stable/).

## Authors

* **Kento Kashiwagi** - [tuimac](https://github.com/tuimac)

If you have some opinion and find bugs, please post [here](https://github.com/tuimac/servertools/issues).

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/tuimac/servertools/LICENSE.md) file for details.
