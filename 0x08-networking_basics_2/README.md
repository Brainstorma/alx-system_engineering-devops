# 0x08-networking_basics_2
This repository contains code, work, and materials related to 0x08-networking_basics_2. These topics cover the basics of computer networking and the various protocols used to connect computers in a network. This repository contains a variety of tasks to build understanding in multiple areas of networking basics.

### Table of Contents

- [What is Networking Basics?](#what-is-networking-basics)
- [Network Topologies](#network-topologies)
- [Internet Protocols](#internet-protocols)
- [Internet Protocol Version 4 (IPv4)](#internet-protocol-version-4-ipv4)
- [Internet Protocol Version 6 (IPv6)](#internet-protocol-version-6-ipv6)
- [Network Address Translation (NAT)](#network-address-translation-nat)
- [Dynamic Host Configuration Protocol (DHCP)](#dynamic-host-configuration-protocol-dhcp)
- [Domain Name System (DNS)](#domain-name-system-dns)
- [Network File System (NFS)](#network-file-system-nfs)
- [Wireless Networking Basics](#wireless-networking-basics)
- [Secure Shell (SSH)](#secure-shell-ssh)
- [Tasks](#tasks)

### What is Networking Basics? 
Networking basics is the fundamental understanding of communication systems used to link computers and devices into a network. Different computer networks can use different topologies, protocols, and technologies to transfer data between devices. Understanding the basics of networking is essential for managing, configuring, and troubleshooting computer networks.

### Network Topologies
Network topologies are the physical and logical layout of a network. Different types of network topologies include the bus, star, mesh, and ring topologies. 

#### Bus Topology
A bus topology is a type of network where all computers and devices are connected to a single cable or backbone. All data being sent travels along the same cable and is received by each device connected. 

#### Star Topology
A star topology is a type of network where all computers and devices are connected to a central device, such as a switch or hub. The central device receives and sends data to all the connected devices.

#### Mesh Topology
A mesh topology is a type of network where each computer and device is connected to multiple other devices. Each device sends and receives data from multiple other devices, allowing for multiple paths of data to travel.

#### Ring Topology
A ring topology is a type of network where each computer and device is connected to two other devices. All devices pass along data in one direction, creating a loop or ring.

### Internet Protocols
Internet protocols are the set of rules used to send data over the internet. Protocols define how data is formatted, transmitted, and received. 

#### Internet Protocol Version 4 (IPv4)
Internet Protocol Version 4 (IPv4) is the fourth version of the Internet Protocol. IPv4 is one of the core protocols used on the Internet and is used to send and receive data between computers. IPv4 provides connectionless data delivery, meaning data is sent without requiring a connection first.

#### Internet Protocol Version 6 (IPv6)
Internet Protocol Version 6 (IPv6) is the sixth version of the Internet Protocol. IPv6 is the latest version of the Internet Protocol and is used to send and receive data between computers. IPv6 provides connectionless data delivery, meaning data is sent without requiring a connection first. 

### Network Address Translation (NAT)
Network Address Translation (NAT) is a way of connecting a private IP-based network to the Internet. NAT translates the internal IP addresses of the private network to publicly accessible IP addresses. NAT allows multiple devices on the private network to share the same public IP address, which saves IP addresses and is more secure.

### Dynamic Host Configuration Protocol (DHCP)
Dynamic Host Configuration Protocol (DHCP) is a network protocol used to dynamically assign IP addresses to network devices. DHCP is used to automatically assign IP addresses to devices as they are added to the network and to manage network settings such as the subnet mask and default gateway. 

### Domain Name System (DNS)
The Domain Name System (DNS) is a distributed directory service used to convert domain names to IP addresses. DNS is used to match domain names to the IP addresses of the server hosting the website.

### Network File System (NFS)
Network File System (NFS) is a distributed file system that allows multiple computers to access shared files and directories over a network. NFS enables multiple computers to access the same files and directories without having to copy them over the network.

### Wireless Networking Basics
Wireless networking is the use of wireless technology to connect computers and devices to a network. Wireless networking uses radio frequency (RF) signals to transfer data over the air, eliminating the need for physical cables. 

### Secure Shell (SSH)
Secure Shell (SSH) is a secure protocol used to remotely connect to a computer. SSH provides a secure connection between two computers over an insecure network, allowing for remote command line access and secure file transfer.

### Tasks
This repository contains the following tasks:
- 0x08-networking_basics_2
    - [0-localhost](./0-localhost)
    - [1-wildcard](./1-wildcard)
    - [2-change_your_home_IP](./2-change_your_home_IP)
    - [3-show_attached_IPs](./3-show_attached_IPs)
    - [4-port_listening_on_localhost](./4-port_listening_on_localhost)
    - [5-port_listening_on_ipv4](./5-port_listening_on_ipv4)
    - [6-port_listening_on_ipv6](./6-port_listening_on_ipv6)

## 0x08-networking_basics_2

This project focuses on teaching the principles and fundamentals of networking. It covers topics such as networking basics, networking concepts, networking applications, networking tools, networking protocols, and the OSI model.

#### What is the OSI Model?
The OSI Model (Open Systems Interconnection Model) is a layered model that provides a conceptual framework for describing and representing communications between two or more computer systems. This model defines seven layers of protocols for network communications, each layer responsible for a different aspect of network communications. The seven layers are:

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

#### What are the main benefits of using the OSI Model?

1. Aids in understanding the complexities of a computer network: By using the OSI Model, network communications can be broken down into smaller, manageable components. This makes it easier to troubleshoot and debug any issues that may arise in a computer network.

2. Helps to create standards: The OSI Model provides a framework that can be used to ensure that all computer systems on a network adhere to the same standards for communication. This ensures that data sent from one computer is formatted correctly and is received correctly by the recipient.

3. Can be used for troubleshooting: By using the OSI Model for troubleshooting, it is easier to identify which layer of the network is causing the problem. This allows for quicker and more effective troubleshooting and resolution.

#### What is IPv4?
IPv4 (Internet Protocol Version 4) is an Internet layer protocol that is used for sending and receiving packets between computers over the Internet. It defines the different datagram (or packet) formats, addressing schemes, and routing protocols used to link different networks together.

#### What is IPv6?

IPv6 (Internet Protocol Version 6) is the latest evolution of the Internet Protocol. It is designed to replace the current IPv4 protocol, which has been in use since the early days of the Internet. IPv6 is intended to provide a larger address space and improved security for Internet communications. IPv6 also offers better support for mobility, quality of service, and multicasting.
