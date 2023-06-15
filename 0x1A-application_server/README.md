# 0x1A. Application server

![c7d1ed0a2e10d1b4e9b3](https://user-images.githubusercontent.com/35099243/155179732-c464c3e1-7eae-4193-b711-f4504ad00035.jpg)

## Concepts

For this project, students are expected to look at these concepts:

* [Web Server](https://alx-intranet.hbtn.io/concepts/17)
* [Server](https://alx-intranet.hbtn.io/concepts/67)
* [Web stack debugging](https://alx-intranet.hbtn.io/concepts/68)

## Background Context

While a web server can also serve dynamic content, this task is usually given to an application server. In this project I added this piece to my infrastructure, plug it to my Nginx and make is serve my Airbnb clone project.

### Resources

* [Application server vs web server](https://alx-intranet.hbtn.io/rltoken/B9fOBzIxX_t1289WAuRzJw)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 ](https://alx-intranet.hbtn.io/rltoken/kpG6RwmwRJHzRmGUM_ERcA)
* [Running Gunicorn](https://alx-intranet.hbtn.io/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
* [Be careful with the way Flask manages slash in route - strict_slashes](https://alx-intranet.hbtn.io/rltoken/lEg0zpkkDcLtdl3VD4ACRQ)
* [Upstart documentation](https://alx-intranet.hbtn.io/rltoken/mcEsKqFsjJA3tHAjiMknaw)

## Requirements

### General

* A README.md file, at the root of the folder of the project, is mandatory
* Everything Python-related must be done using python3
* All config files must have comments

## Bash Scripts

* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing


# Application server

This was the application deployment project for our AirBnB clone. In this
project, I configured Nginx on the web servers provided me by Holberton School
to serve a WSGI Flask app running through Gunicorn. Additionally, I set up an
Upstart script to keep the application running on server reboots.

## Tasks :page_with_curl:

* **0. Set up development with Python**
  * In this task, I configured the file `web_flask/0-hello_route.py` from my
  [AirBnB_clone_v2](https://github.com/bdbaraban/AirBnB_clone_v2) to serve content
  on the route `/airbnb-onepage/`, running on port `5000`.

* **1. Set up production with Gunicorn**
  * This task involved setting up a production environment, installing and configuring
  Gunicorn to serve the same file from task 0.

* **2. Serve a page with Nginx**
  * [2-app_server-nginx_config](./2-app_server-nginx_config): Nginx configuration file
  proxying requests on the route `/airbnb-onepage/` to the Gunicorn app running on
  port `5000`.

* **3. Add a route with query parameters**
  * [3-app_server-nginx_config](./3-app_server-nginx_config): Nginx configuration file
  proxying requests on the route `/airbnb-dynamic/number_odd_or_even/<int: num>` to the
  Gunicorn app running on port `5000`.

* **4. Let's do this for your API**
  * In this task, I configured the API from my [AirBnB_clone_v3](./https://github.com/Ostoyae/AirBnB_clone_v3) to run on Gunicorn.
  * [4-app_server-nginx_config](./4-app_server-nginx_config): Nginx configuration file
  that proxies requests on the AirBnB API to the corresponding Gunicorn app.

* **5. Serve your AirBnB clone**
  * In this task, I configured the complete AirBnB app from [AirBnB_clone_v4](https://github.com/bdbaraban/AirBnB_clone_v4) to run on Gunicorn and be served through Nginx.
  * [5-app_server-nginx_config](./5-app_server-nginx_config): Nginx configuration file
  configured to serve the static assets from `web_dynamic/static/` on the Gunicorn AirBnB
  app.

* **6. Deploy it**
  * [gunicorn.conf](./gunicorn.conf): Configuration file for an Upstart script that starts a
  Gunicorn process bounded to port 5003 that serves the content from task 5.
  * The Gunicorn process spawns three worker processes and logs errors to `/tmp/airbnb-error.log`,
  access to `/tmp/airbnb-access.log`.

* **7. No service interruption**
  * [4-reload_gunicorn_no_downtime](./4-reload_gunicorn_no_downtime): Bash script that gracefully
  reloads Gunicorn.
