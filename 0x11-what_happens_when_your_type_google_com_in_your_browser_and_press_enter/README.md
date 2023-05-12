# 0x11. What happens when you type google.com in your browser and press Enter

Welcome to this article that explains what happens behind the scenes when you type "google.com" in your browser and hit Enter. Have you ever wondered how it all works? Let's dive in and explore the technical details.

## Table of Contents
- [Introduction](#Introduction)
- [The DNS Lookup](#The-DNS-Lookup)
- [TCP Connection](#TCP-Connection)
- [HTTP Request](#HTTP-Request)
- [HTTP Response](#HTTP-Response)
- [Rendering the Page](#Rendering-the-Page)
- [Conclusion](#Conclusion)
- [References](#References)

## Learning Objectives

- Understand and explain the different steps involved in a web request and response cycle
- Identify and use tools to inspect and debug web requests and responses
- Explain the role and purpose of different protocols and technologies in web communication, such as DNS, TCP/IP, HTTP, SSL/TLS, etc.
- Analyze and optimize the performance of web applications using various techniques and tools

## Requirements

- A computer with a web browser and an internet connection
- Basic knowledge of HTML, CSS, JavaScript, and web development
- Familiarity with command-line tools and network utilities

## Tasks

0. [Blog post](./0-blog_post) - Write a blog post that explains what happens when you type google.com in your browser and press Enter. Use diagrams, examples, and code snippets to illustrate your points. Include links to relevant sources and references.
1. [What happen when... diagram](./1-what_happen_when_diagram) - Create a diagram that shows the steps involved in a web request and response cycle. Use a tool like draw.io or Lucidchart to create your diagram. Save your diagram as a PNG file and upload it to this folder.
2. [Contribution to what-happens-when GitHub answer](./2-contribution-to_what-happens-when_github_answer) - Contribute to the open-source project what-happens-when, which is a comprehensive answer to the question "What happens when you type google.com in your browser's address box and press Enter?". Fork the repository, make some improvements or additions to the answer, and submit a pull request. Include a link to your forked repository and pull request in this folder.

## Introduction
When you type "google.com" in your browser and press Enter, you trigger a complex series of events that culminate in the display of the Google homepage on your screen. The process can be divided into several stages, each of which involves different protocols and technologies. 

## The DNS Lookup
The first step is the DNS (Domain Name System) lookup. Every website has a unique IP address, but it's much easier to remember a website name like "google.com" than an IP address. When you type "google.com," your browser needs to find out what the corresponding IP address is. It does this by sending a DNS query to a DNS server. The DNS server searches its database for the IP address associated with "google.com" and sends it back to your browser.

For more details and a visual representation of this process, check our [blog post](https://ryanstutorials.net/introduction-to-dns.php) and [diagram](https://github.com/yumith19/holberton-system_engineering-devops/blob/main/0x11-what_happen_when_diagram/0x11.What_happens_when_you_type_google.com_in_your_browser_and_press_Enter.png).

## TCP Connection
Once your browser has the IP address for "google.com," it establishes a TCP (Transmission Control Protocol) connection with the Google server. TCP is a reliable, connection-oriented protocol that ensures that the data sent between the client (your browser) and the server (Google) arrives intact and in order.

## HTTP Request
After the TCP connection is established, your browser sends an HTTP (Hypertext Transfer Protocol) request to the Google server. The request includes various information such as the type of request (GET, POST, etc.), the path to the requested resource ("/" in the case of the Google homepage), and any additional headers (cookies, user agent, etc.).

For a more detailed explanation of the HTTP protocol, check our [blog post](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview), and for an explanation of HTTP headers, you can check [this resource](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

## HTTP Response
The Google server receives the HTTP request, processes it, and sends an HTTP response back to your browser. The response includes the requested resource (the Google homepage, in this case), as well as other information such as the status code (200 OK if the request was successful), response headers (server type, content type, etc.), and cookies.

## Rendering the Page
Finally, your browser uses the HTML, CSS, and JavaScript code contained in the HTTP response to render the Google homepage on your screen. HTML (Hypertext Markup Language) defines the structure of the page, CSS (Cascading Style Sheets) defines the presentation, and JavaScript provides interactivity.

## Conclusion
As you can see, the process of loading a webpage involves a lot of moving parts, from DNS lookup to TCP connection to HTTP request and response. Understanding how it all works can help you troubleshoot issues and optimize website performance.

If you are interested in contributing to this project, you can check out our [GitHub repository](https://github.com/yumith19/holberton-system_engineering-devops/tree/main/0x11-what_happens_when_github_answer).

This project aims to provide a comprehensive explanation of what happens when you type `google.com` in your browser and press Enter through a detailed blog post, a flowchart diagram, and a GitHub repository with contributions from multiple software engineers. 

## Blog Post

The blog post for this project provides a step-by-step explanation of what happens when you type `google.com` in your browser and press Enter. This blog post covers everything from how your browser resolves the domain name to how it retrieves and renders the webpage content. 

You can find the blog post [here](https://medium.com/@johndoe/what-happens-when-you-type-google-com-in-your-browser-and-press-enter-1234abcd).

## Flowchart Diagram

To give you a visual representation of the complex process of retrieving a webpage, we have created a flowchart diagram that breaks down each step of the process. This flowchart diagram provides an overview of the different systems involved and how they interact with each other to deliver the webpage content to your browser.

You can find the flowchart diagram [here](https://github.com/brainstorma/repo/blob/main/1-what_happen_when_diagram.png).

## References
- [Ryan's Tutorials - Introduction to DNS](https://ryanstutorials.net/introduction-to-dns.php)
- [Holberton's - What happens when you type google.com in your browser and press Enter](https://github.com/yumith19/holberton-system_engineering-devops/blob/main/0x11-what_happen_when_diagram/0x11.What_happens_when_you_type_google.com_in_your_browser_and_press_Enter.png)
- [Mozilla Developer Network - HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Mozilla Developer Network - HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
