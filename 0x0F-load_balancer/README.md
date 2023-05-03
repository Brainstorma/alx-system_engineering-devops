# 0x0F-load_balancer

This repository contains my solution to the Holberton School project `0x0F-load_balancer`. In this project, I had to set up a load balancer using HAProxy and configure it to balance HTTP requests between multiple web servers. Additionally, I also added a custom HTTP response header to the servers using Puppet.

## Custom HTTP Response Header

The task `0-custom_http_response_header` involved adding a custom HTTP response header to the web servers. This was achieved by setting the `proxy_set_header` directive in the HAProxy configuration file to include the desired header.

For more details, please refer to the [README.md](./README.md) file in the `0-custom_http_response_header` directory.

## Install Load Balancer

The task `1-install_load_balancer` required me to install and configure HAProxy on a dedicated server. This involved installing HAProxy from the package manager (`apt-get`) and setting the appropriate configuration options.

For more details, please refer to the [Install Load Balancer](./1-install_load_balancer) file in the `1-install_load_balancer` directory.

## Puppet Custom HTTP Response Header

The task `2-puppet_custom_http_response_header.pp` involved automating the configuration of the custom HTTP response header using Puppet. This was achieved using a Puppet manifest file that defined the necessary resources and dependencies.

For more details, please refer to the [2-puppet_custom_http_response_header](./2-puppet_custom_http_response_header.pp) file in the `2-puppet_custom_http_response_header.pp` directory.

## Conclusion

I thoroughly enjoyed working on this project and learned a lot about load balancing and HAProxy. Feel free to browse through the code and documentation to get a better understanding of the implementation details.
