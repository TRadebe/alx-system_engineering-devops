# Project: 0x13-firewall

## Introduction

This project focuses on configuring and managing firewalls on web servers using the UFW (Uncomplicated Firewall) tool. 
It includes tasks related to blocking incoming traffic and port forwarding.

## Task 0: Block all incoming traffic

### Description

Install the UFW firewall and configure it on web-01 to block all incoming traffic except for specific TCP ports.

### Requirements

- Configure UFW to allow incoming traffic on the following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)

## Task 1: Port forwarding

### Description

Configure the firewall on web-01 to redirect traffic from port 8080/TCP to port 80/TCP.e that was modified to enable port forwarding. 

## Additional Information

- **Telnet Usage:** Telnet can be used to check if sockets are open. For example, to check if port 22 is open on web-02:

  ```bash
  telnet web-02.holberton.online 22
  ```
