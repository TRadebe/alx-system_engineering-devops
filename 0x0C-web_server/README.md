# ALX System Engineering DevOps - Web Server Configuration

This comprehensive guide provides instructions and information on setting up a web server environment on an Ubuntu 16.04 LTS machine 
as part of the ALX System Engineering DevOps curriculum. 
The following sections outline the requirements, tasks, and example commands to complete each task. Make sure to follow the guidelines 
and best practices to ensure a successful configuration.

## Table of Contents

1. [Transfer a File to Your Server](#task-0-transfer-a-file-to-your-server)
2. [Install Nginx Web Server](#task-1-install-nginx-web-server)
3. [Setup a Domain Name](#task-2-setup-a-domain-name)
4. [Redirection](#task-3-redirection)
5. [Custom 404 Page](#task-4-not-found-page-404)
6. [Install Nginx Web Server (w/ Puppet)](#task-5-install-nginx-web-server-with-puppet)

### Task 0: Transfer a File to Your Server

#### Requirements:
- Write a Bash script that transfers a file from your client to a server.
- Accepts 4 parameters: 
  1. The path to the file to be transferred.
  2. The IP of the server.
  3. The username scp connects with.
  4. The path to the SSH private key that scp uses.
- Display usage: `0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if fewer than 3 parameters are passed.
- Use scp to transfer the file to the user's home directory `~/`.
- Disable strict host key checking when using scp.

**Example:**
```shell
$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
```

### Task 1: Install Nginx Web Server

#### Requirements:
- Install Nginx on your web-01 server.
- Nginx should be listening on port 80.
- When querying Nginx at its root `/` with a GET request using `curl`, it must return a page that contains the string "Hello World!".
- Configure the server to meet the requirements using a Bash script.

**Example:**
```shell
$ curl 34.198.248.145/
Hello World!
```

### Task 2: Setup a Domain Name

#### Requirements:
- Provide the domain name only (e.g., `myschool.tech`), no subdomain.
- Configure your DNS records with an A entry so that your root domain points to your web-01 IP address.
- Update your project website URL with the domain name.

**Example:**
```shell
$ cat 2-setup_a_domain_name
myschool.tech
$ dig myschool.tech
```

### Task 3: Redirection

#### Requirements:
- Configure Nginx to perform a "301 Moved Permanently" redirection when accessing `/redirect_me`.
- Update the server using a Bash script.

**Example:**
```shell
$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4
```

### Task 4: Custom 404 Page

#### Requirements:
- Configure Nginx to have a custom 404 page that contains the string "Ceci n'est pas une page".
- Update the server using a Bash script.

**Example:**
```shell
$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found

$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page
```

### Task 5: Install Nginx Web Server (w/ Puppet)

#### Requirements:
- Install and configure Nginx using Puppet.
- Ensure Nginx listens on port 80 and returns "Hello World!" when querying the root `/`.
- Implement a "301 Moved Permanently" redirection when accessing `/redi
