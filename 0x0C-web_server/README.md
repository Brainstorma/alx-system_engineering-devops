# 0x0C Web Server

Welcome to the 0x0C Web Server repository! This repository contains the code for a custom web server implementation, developed as part of the curriculum for the ALX Full-Stack Software Engineering program. This web server is designed to be lightweight and efficient, while also offering a range of features and options for serving static and dynamic content.

## Installation

To get started with this web server, you will need to clone the repository and compile the source code. Here are the steps to follow:

1. Clone the repository using `git clone https://github.com/brainstorma/0x0C-web_server.git`.
2. Change into the `0x0C-web_server` directory with `cd 0x0C-web_server`.
3. Compile the source code by running `make`.
4. Run the web server using the `./web_server` command.

## Usage

Once the web server is running, it will listen on port 8080 by default. You can access the server using your web browser or any other HTTP client tool. By default, the server will serve files from the `./www` directory, but you can configure this using command line arguments (see below). Here are some examples of basic usage:

- Visit http://localhost:8080/ in your web browser to see the default homepage.
- Create an HTML file in the `./www` directory and visit http://localhost:8080/brainstorma.html to view it.
- Use a tool like `curl` to send HTTP requests to the server and view the response headers and body.

## Configuration

The web server can be configured using command line arguments. Here are the available options:

- `-p <port>`: Change the port that the server listens on (default is 8080).
- `-d <directory>`: Change the directory that the server serves files from (default is ./www).
- `-s`: Enable SSL mode (HTTPS) using a self-signed certificate. This option requires that the OpenSSL library is installed on your system.

## Architecture and Design

The web server is written in C and uses low-level system calls for socket communication and file I/O. Here are some key features of the architecture and design:

- Multi-threaded: The server uses POSIX threads to handle multiple connections concurrently.
- Dynamic content: The server is capable of executing CGI scripts and serving their output to clients.
- Error handling: The server is designed to gracefully handle errors, sending appropriate HTTP status codes and error pages to clients.
- Security: The server is designed to protect against common security issues, such as directory traversal attacks and buffer overflow vulnerabilities.

## Tasks

This repository contains six tasks related to the web server, each with its own subdirectory and README file. Here are the tasks:

1. [0-transfer_file](./0-transfer_file): Write a script that transfers a file from our client to a server.
2. [1-install_nginx_web_server](./1-install_nginx_web_server): Install and configure Nginx on a web server.
3. [2-setup_a_domain_name](./2-setup_a_domain_name): Configure a custom domain name for your web server.
4. [3-redirection](./3-redirection): Configure Nginx to redirect HTTP requests to HTTPS.
5. [4-not_found_page_404](./4-not_found_page_404): Configure Nginx to serve a custom 404 page for non-existent URLs.
6. [5-secured_and_locked_down_web_server](./5-secured_and_locked_down_web_server): Configure Nginx to enhance security and access control on your web server.

## Credits

This web server was developed by Brainstorma for the ALX Full-Stack Software Engineering program. 
