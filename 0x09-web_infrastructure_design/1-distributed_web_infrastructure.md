# Designing a Three Server Web Infrastructure for www.foobar.com

This document outlines the design of a three-server web infrastructure that can host the website www.foobar.com. This infrastructure comprises two servers on the application layer, a web server, a load balancer, a MySQL database, and a codebase. 

## Infrastructure Components

### Application Layer

The application layer is made up of two servers - one application server and one web server: 

#### Web Server (Nginx)

We are deploying Nginx as our web server. It is reliable, scalable, and can handle a high volume of traffic. Nginx serves static files such as HTML, CSS, and images. 

#### Application Server

Our application server will be running on a Python Flask framework. Flask is a lightweight and easy to use framework to build web applications. The application server will help manage authentication and access control, implement business logic and interact with the database. 

### Load Balancer

Our load balancer of choice is HAProxy. HAProxy is a fast and reliable solution to load balance incoming traffic to multiple application servers. 

Distribution Algorithm:

Our load balancer is configured to use the round-robin algorithm to distribute traffic to the application servers. This algorithm selects application servers in rotation to balance the workload. By using this algorithm, we can ensure that traffic is evenly distributed across all application servers. 

Active-Active vs Active-Passive setup:

Our load balancer is enabling an Active-Active setup. Active-Active setup refers to a configuration where all servers are actively serving requests at the same time. It means that the load balancer routes traffic to all servers simultaneously. This setup ensures better availability and fault tolerance. 

### Database Layer

Our database of choice is MySQL. MySQL is a widely used open-source database. It provides robustness, scalability, and reliability.

#### Primary-Replica Cluster

We are utilizing a Primary-Replica (Master-Slave) cluster to replicate our database. The primary node handles all writes (INSERT, UPDATE, DELETE), while the replica node replicates these changes and handles all read requests. 

Difference between Primary and Replica node:

The primary node is the node that receives write requests such as INSERT, UPDATE, and DELETE. It is the node that all other nodes replicate to. The replica node, on the other hand, receives updates from the primary node and handles read requests. 

## Issues with this Infrastructure

We have identified some issues with this infrastructure: 

### SPOF

Our infrastructure has a Single Point of Failure (SPOF) in the web server. If the web server fails, the entire application will be inaccessible. We can overcome this problem by introducing another web server and have HAProxy load balance between the two. 

### Security Issues

Our infrastructure has some potential security issues such as no firewall or HTTPS. We can address these issues by adding a firewall to restrict traffic to only certain ports and implementing HTTPS to encrypt traffic between servers and clients. 

### No Monitoring

We do not have any monitoring in place to track the performance and health of our servers. We need to implement monitoring to alert us when something goes wrong, measure server performance, and track trends over time. 

## Conclusion

This infrastructure design comprises two servers, a web server (Nginx), an application server, a load balancer (HAProxy), a MySQL database, and a codebase. It uses the round-robin algorithm for load balancing, has an Active-Active setup, and a Primary-Replica cluster for database replication. However, this infrastructure has some issues with SPOF, security, and lacks monitoring. These issues can be resolved by introducing additional web servers, implementing HTTPS, firewall, and adding monitoring. 
