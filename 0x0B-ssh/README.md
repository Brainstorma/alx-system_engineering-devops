# 0x0B-ssh

The purpose of this project is to learn how to use SSH (Secure Shell) and how to connect to a remote server using SSH. SSH is a cryptographic network protocol that allows secure communication between two computers. It provides secure access to a remote computer over an unsecured network, like the internet.

## Background Context

In the world of web development, developers often work on remote servers that are hosted by a third-party company. These servers are managed by system administrators who give developers the necessary access rights to the servers. To gain access to a remote server, developers must use SSH, which secures the connection between the two computers and allows them to communicate securely.

## Learning Objectives

At the end of this project, we should be able to answer the following questions:

- What is a server?
- Where server usually live?
- What is SSH?
- How to create an SSH RSA key pair?
- How to connect to a remote host using an SSH RSA key pair?
- The advantage of using SSH over other protocols?

## Repository Tasks

The following tasks were completed as part of this project:

#### [0. Use a private key](./0-use_a_private_key)
Learn how to connect to a server using SSH with a private key. We will be using [DigitalOcean](https://www.digitalocean.com/) to host the server.

#### [1. Create an SSH key pair](./1-create_ssh_key_pair)
Create an SSH key pair using `ssh-keygen`. We will be using this key pair to connect to our server.

#### [2. Client configuration file](./2-ssh_config)
Create a client configuration file to simplify the SSH connection process.

#### [3. Let me in!](./3-ssh_into_your_server)
Connect to the server using the SSH key pair that we created in task 1.

#### [4. Puppet manifests](./4-puppet_ssh_config.pp)
Use Puppet to automate the creation of the SSH client configuration file that we created in task 2.

## How to Use

- Clone the repository to your local machine using `git clone`.
- Navigate to the directory of the desired task.
- Follow the instructions in the README.md file of the task folder.
