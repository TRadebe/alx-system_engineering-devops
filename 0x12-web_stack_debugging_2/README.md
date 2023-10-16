# Project: 0x12-web_stack_debugging_2

## Introduction

This project focuses on debugging and configuring web servers. It includes tasks related to running software as another user, 
running Nginx as a specific user, and implementing fixes in a concise manner.

## General Requirements

- All files are interpreted on Ubuntu 20.04 LTS.
- Files end with a new line.
- A README.md file at the root of the folder is mandatory.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck without any errors.
- Bash scripts must run without error.
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining the script's purpose.

## Task 0: Run software as another user

### Description

Write a Bash script that accepts one argument and runs the `whoami` command under the user passed as an argument.

### Requirements

- Accept one argument.
- Run the `whoami` command under the user passed as an argument.

## Task 1: Run Nginx as Nginx

### Description

Fix the container so that Nginx is running as the `nginx` user, listening on all active IPs on port 8080.

### Requirements

- Nginx must be running as the `nginx` user.
- Nginx must be listening on all active IPs on port 8080.
- Do not use `apt-get remove`.
- Write a Bash script that configures the container to meet the above requirements.

## Task 2: 7 lines or less

### Description

Using the solution from Task 1, create a Bash script that is 7 lines or less.

### Requirements

- Bash script must be 7 lines or less.
- There must be a new line at the end of the file.
- Respect Bash script requirements.
- Do not use `;`, `&&`, `wget`, or execute the previous answer file.
