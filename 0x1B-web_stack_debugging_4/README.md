# 0x1B-web_stack_debugging_4

## Description
0x1B-web_stack_debugging_4 is a repository that contains solutions to various web stack debugging challenges. The repository focuses on debugging and troubleshooting complex issues with web applications. Each challenge requires a different set of debugging techniques and skills. This project contains tasks for learning how to debug web stacks using Puppet.

This repository contains solutions to two tasks, both of which are focused on debugging Nginx server configuration files. The first task is "0-the_sky_is_the_limit_not.pp". This task involves a server configuration issue that limits the number of file descriptors that a process can open, causing the web application to crash. The second task, "1-user_limit.pp", is also focused on a server configuration issue. In this task, the maximum number of concurrent connections to the web server is limited, causing the application to become unresponsive.

## Tasks

### 0. The sky is the limit, let's bring that limit higher

[0-the_sky_is_the_limit_not.pp](0-the_sky_is_the_limit_not.pp) is a Puppet manifest that changes the OS configuration so that it is possible to login with the `ALX` user and open a file without any error message.
In this task, the server configuration file needs to be modified to increase the maximum number of file descriptors that a process can open. The web application is crashing because it is reaching the limit of the number of file descriptors it can open. The solution to this task involves editing the Nginx configuration file to increase the file descriptor limit, which will allow the web application to function correctly.


### 1. User limit

[1-user_limit.pp](1-user_limit.pp) is a Puppet manifest that changes the OS configuration so that it is possible to login with the `ALX` user and run the command `curl 0:8080` without any error message.
The second task involves a server configuration issue that limits the maximum number of concurrent connections to the web server. This limit causes the web application to become unresponsive during periods of high traffic. The solution to this task involves editing the Nginx configuration file to increase the maximum number of concurrent connections allowed, which will improve the performance of the web application during periods of high traffic.
