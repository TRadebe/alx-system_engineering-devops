# HTTPS SSL Configuration Project

## Overview

This project focuses on configuring and securing your web infrastructure using HAproxy for SSL termination. 
Follow the tasks below to ensure proper configuration and HTTPS enforcement.

## Tasks

### Task 0: World Wide Web

#### Objective
Configure your domain zone and create a Bash script to display information about specified subdomains.

#### Requirements
- Add subdomains www, lb-01, web-01, and web-02 to your domain.
- Bash script accepts two arguments: domain (mandatory) and subdomain (optional).
- Output format: "The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]".

#### Example
```bash
./0-world_wide_web holberton.online
# Output:
# The subdomain www is a A record and points to 54.210.47.110
# The subdomain lb-01 is a A record and points to 54.210.47.110
# The subdomain web-01 is a A record and points to 34.198.248.145
# The subdomain web-02 is a A record and points to 54.89.38.100

./0-world_wide_web holberton.online web-02
# Output:
# The subdomain web-02 is a A record and points to 54.89.38.100
```

### Task 1: HAproxy SSL Termination

#### Objective
Configure HAproxy to handle encrypted traffic (SSL termination).

#### Requirements
- HAproxy listens on port TCP 443.
- HAproxy accepts SSL traffic.
- Encrypted traffic returns the / of your web server.
- Page returned must contain "Holberton School".
- Share HAproxy config in the file `1-haproxy_ssl_termination` located at `/etc/haproxy/haproxy.cfg`.

#### Example
```bash
curl -sI https://www.holberton.online
# Output:
# HTTP/1.1 200 OK
# Server: nginx/1.4.6 (Ubuntu)
# ...

curl https://www.holberton.online
# Output:
# Holberton School for the win!
```

### Task 2: HTTPS Traffic Enforcement

#### Objective
Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

#### Requirements
- Transparent to the user.
- HAproxy returns a 301 for HTTP.
- Redirects HTTP traffic to HTTPS.
- Share HAproxy config in the file `100-redirect_http_to_https` located at `/etc/haproxy/haproxy.cfg`.

#### Example
```bash
curl -sIL http://www.holberton.online
# Output:
# HTTP/1.1 301 Moved Permanently
# ...

curl -sI https://www.holberton.online
# Output:
# HTTP/1.1 200 OK
# ...
```

## Repository

### GitHub Repository
[alx-system_engineering-devops](link-to-repository)

### Directory
`0x10-https_ssl`

## Files
- `0-world_wide_web`
- `1-haproxy_ssl_termination`
- `100-redirect_http_to_https`
