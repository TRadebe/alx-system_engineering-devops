# Web Infrastructure Design Project

In this project, you will be tasked with designing and explaining the architecture of various web infrastructures. 
The goal is to deepen your understanding of web systems and their components. You will need to whiteboard your designs, 
take screenshots, and provide explanations for each task. Please ensure that you do not copy or plagiarize any content, 
as this is strictly prohibited.

## Resources

Before you begin, it's recommended to familiarize yourself with the following resources:

- Network basics concept page
- Server concept page
- Web server concept page
- DNS concept page
- Load balancer concept page
- Monitoring concept page
- What is a database
- What's the difference between a web server and an app server?
- DNS record types
- Single point of failure
- How to avoid downtime when deploying new code
- High availability cluster (active-active/active-passive)
- What is HTTPS
- What is a firewall

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without needing to consult external sources:

### General

- Understand how to create a diagram of a web stack.
- Explain the roles and functions of each component in a web infrastructure.
- Describe system redundancy and its importance.
- Define key acronyms such as LAMP, SPOF, and QPS.

### Copyright - Plagiarism

- Understand the importance of original work and avoiding plagiarism.

## Requirements

To successfully complete this project, you must meet the following requirements:

### General
- Create a `README.md` file at the root of your project folder.
- For each task, whiteboard your design and take a screenshot of your diagram.
- Manually review the project, ensuring that each task is completed.
- Upload your screenshots to an image hosting service and insert the links into your answer file.
- Push your answer file to GitHub and insert the GitHub file link into the URL box.
- Whiteboard each task in front of a mentor, staff, or student without using a computer or notes.

## Tasks

### Task 0: Simple Web Stack
Design a one-server web infrastructure that hosts the website reachable via `www.foobar.com`. Your design should include the following components:

- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

You must be able to explain the following aspects of your infrastructure:
- The role of a server
- The purpose of the domain name
- The type of DNS record used for `www.foobar.com`
- The roles of the web server, application server, and database
- How the server communicates with the user's computer
- Issues with this infrastructure, including SPOF, downtime during maintenance, and scalability challenges.

### Task 1: Distributed Web Infrastructure

Design a three-server web infrastructure that hosts the website `www.foobar.com`. Your design should include the following components:

- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

You must explain the reasons for adding each component and answer questions about distribution algorithms, load balancing setups, 
and database clustering. Additionally, discuss issues such as SPOF, security, and monitoring.

### Task 2: Secured and Monitored Web Infrastructure

Design a three-server web infrastructure for `www.foobar.com` that is secure, serves encrypted traffic over HTTPS, and is monitored. 
Your design should include the following components:

- 3 firewalls
- 1 SSL certificate for HTTPS
- 3 monitoring clients (data collectors for monitoring services)

Explain the purpose of each added element, including firewalls, HTTPS, and monitoring. Address issues related to SSL termination, 
database write capabilities, and component redundancy.

Please ensure that all documentation and explanations are in English to enhance your technical communication skills.

For detailed instructions and to submit your completed tasks, refer to the provided GitHub repository and project directory. 
Good luck with your web infrastructure design project!
