# Project Name: Web Server Redundancy and Load Balancer Configuration

## Background Context

This project aims to enhance the web stack by introducing redundancy for web servers, enabling the infrastructure to handle more traffic and improve reliability. Two additional servers, `gc-[STUDENT_ID]-web-02` and `gc-[STUDENT_ID]-lb-01`, have been provided for this purpose. Bash scripts will be utilized to automate the configuration of a new Ubuntu server to meet the project requirements.

## Requirements

- Allowed editors: vi, vim, emacs
- Interpreted on Ubuntu 16.04 LTS
- Files end with a new line
- A README.md file, at the root of the folder, is mandatory
- Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

### Your Servers

| Name                | Username | IP              | State   |
| ------------------- | -------- | --------------- | ------- |
| 224933 web-01       | ubuntu   | *************   | running |
| 224933-web-02       | ubuntu   | *************   | running |
| 224933-lb-01        | ubuntu   | *************   | running |

## Tasks

### Task 0: Double the number of webservers

In this task, web-02 needs to be configured identically to web-01. The Nginx on both servers should contain a custom header (`X-Served-By`) 
to track which web server is handling HTTP requests.

**Requirements:**

- Configure Nginx on web-01 and web-02 with a custom header
- Write `0-custom_http_response_header` to configure a new Ubuntu machine to the specified requirements

### Task 1: Install your load balancer

Install and configure HAProxy on lb-01 to send traffic to web-01 and web-02 using a round-robin algorithm.

**Requirements:**

- Configure HAProxy for load balancing
- Ensure HAProxy can be managed via an init script
- Servers should be configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02
- Write a Bash script to configure a new Ubuntu machine to meet the above requirements

### Task 2: Add a custom HTTP header with Puppet

*Advanced Task*

Automate the creation of a custom HTTP header response using Puppet.

**Requirements:**

- Puppet script (`2-puppet_custom_http_response_header.pp`) to configure a new Ubuntu machine as specified in the task
