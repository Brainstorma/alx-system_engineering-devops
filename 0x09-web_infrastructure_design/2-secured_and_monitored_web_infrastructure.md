# Design of Three Server Web Infrastructure for www.foobar.com

This document specifies the design of a three server web infrastructure to host www.foobar.com. The infrastructure must be secured, serve encrypted traffic and must be monitored. The infrastructure is broken down into the following components:

1. Load Balancer:
    * The load balancer will distribute incoming traffic across the webservers.
    * It will terminate SSL at the load balancer level.
    * The load balancer will also perform health checks on the webservers, and should one server become unresponsive, it will redirect traffic to healthy servers.
    * The load balancer will handle all client requests so that the servers can focus only on serving content.

2. Web Servers:
    * There will be three web servers, each with Apache installed.
    * The web servers will host content and serve http requests received from the Load Balancer.
    * Apache will be configured with Virtual Host to serve `www.foobar.com`.
    * The web servers will not have direct access to the database.
  
3. Firewall:
    * Three firewalls will be added to the infrastructure for added security.
    * Firewalls will be responsible for creating a barrier between the internet and our infrastructure.
    * The firewalls will be configured to allow only incoming traffic on specific ports that are required to provide website functionality.
  
4. SSL Certificate:
    * An SSL certificate will be used to encrypt the traffic served over HTTPS.
    * The SSL certificate will be installed at the load balancer level, which will terminate SSL requests on behalf of the web servers. 
    * The SSL certificate will help keep the website secure by encrypting sensitive information in transit.

5. Database:
    * We will use MySQL to store website data.
    * One MySQL master server and two slave servers will be used in this infrastructure. 
    * The master server will handle write requests, while the slave servers will replicate data from the master server to eventually provide read access as well.

6. Monitoring:
    * Three monitoring clients will be used to monitor the webservers and database performance. 
    * Data will be collected by the Sumologic monitoring service and the monitoring clients.
    * The monitoring clients will collect data such as server resource usage (CPU, Memory, Disk) and network usage. 
    * Sumologic will collect and analyze data to monitor the performance of the infrastructure.
   
## Explanation of Design Decisions

### Why add firewalls?

Firewalls are used as a security measure to protect our infrastructure from unauthorized access. By setting up firewalls, we ensure that traffic is directed only to the ports required to provide website functionality. Firewalls are also useful in preventing traffic spikes and DDoS attacks, ensuring website availability.

### Why serve traffic over HTTPS?

Serving traffic over HTTPS is essential for website security. HTTPS encrypts sensitive information so that it cannot be intercepted or modified by hackers. SSL certificates help to verify the identity of the website server, and protect against Man-In-The-Middle attacks.

### Why use monitoring?

Monitoring helps us keep an eye on the infrastructure's performance, track the root cause of problems, and make informed decisions about when to take action. Monitoring data helps us fine-tune our configuration and adjust resource allocations to avoid any performance issues. Monitoring is used to identify anomalies and trends over time, which help in predicting future issues and improve overall infrastructure security.

### How is data collected by the monitoring tool?

The monitoring clients will collect data on the performance of the servers, such as CPU usage, Memory usage, Network usage, and Disk usage. Data is transferred within the infrastructure and stored in Sumologic, which is also responsible for analyzing the logs.

### What If I want to monitor your web server QPS?

To monitor the web server QPS, we need to install additional tools. Web server logs provide us with the necessary data to monitor QPS. The logs can be forwarded to Sumologic, and we can use Sumologic to analyze them in real-time, which helps in monitoring QPS.

## Issues with this Infrastructure

### Why terminating SSL at the load balancer level is an issue?

Terminating SSL at the load balancer level creates a potential security vulnerability. Sensitive data is decrypted before reaching the server, which means the server is not aware of whether the connection is secure or not. Also, if the SSL certificate at the load balancer level is compromised, this could allow attackers to view or modify sensitive information in transit.

### Why having only one MySQL server capable of accepting writes is an issue?

Having only one MySQL server capable of accepting write requests creates a single point of failure. If the server goes down, the website's functionality would be severely affected, and we could lose the data stored on the server.

### Why having servers with all the same components (database, web server, and application server) might be a problem?

Having servers with all the same components creates a 'monolithic' infrastructure that makes scaling difficult. Scaling a monolithic application often requires scaling the entire stack: webserver, application server, and database. This could result in costly infrastructure changes to the entire infrastructure to support increased traffic. It is preferable to design for modularity and loose coupling, a system where different components can be added or removed according to the needs of the system.
