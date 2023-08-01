# Processes and Signals - Bash Scripts

## Table of Contents

- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Project Description](#project-description)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a collection of Bash scripts related to processes and signals in Linux. 
The scripts are part of the DevOps learning curriculum and are designed to teach process management, 
signal handling, and process identification using shell scripting.

## Learning Objectives

By completing this project, you will be able to:
- Understand what a PID (Process ID) is and how to find your own PID.
- Identify running processes and their hierarchy on Linux.
- Demonstrate knowledge of signals and their significance in process management.
- Write Bash scripts to manage processes and handle signals.

## Project Description

The project consists of several Bash scripts, each targeting specific learning objectives related to processes and signals. 
The tasks include finding your own PID, listing running processes, stopping infinite processes, and handling signals.

## Requirements

- Operating System: Ubuntu 20.04 LTS
- Text Editors: vi, vim, emacs
- Bash Version: /usr/bin/env bash
- Shellcheck: version 0.7.0

## Project Tasks

1. **What is my PID**
   - Filename: 0-what-is-my-pid
   - Description: Displays the PID of the current running Bash script.

2. **List your processes**
   - Filename: 1-list_your_processes
   - Description: Displays a list of currently running processes, including process hierarchy, for all users.

3. **Show your Bash PID**
   - Filename: 2-show_your_bash_pid
   - Description: Displays lines containing the word "bash," allowing you to find your Bash process PID.

4. **Show your Bash PID made easy**
   - Filename: 3-show_your_bash_pid_made_easy
   - Description: Displays the PID and process name of processes containing the word "bash."

5. **To infinity and beyond**
   - Filename: 4-to_infinity_and_beyond
   - Description: Displays "To infinity and beyond" indefinitely with a sleep 2 between each iteration.

6. **Don't stop me now!**
   - Filename: 5-dont_stop_me_now
   - Description: Stops the process started by the 4-to_infinity_and_beyond script.

7. **Stop me if you can**
   - Filename: 6-stop_me_if_you_can
   - Description: Stops the process started by the 4-to_infinity_and_beyond script without using kill or killall.

8. **Highlander**
   - Filename: 7-highlander
   - Description: Displays "To infinity and beyond" indefinitely with a sleep 2 between each iteration and responds to SIGTERM with 
     "I am invincible!!!"

9. **Beheaded process**
   - Filename: 8-beheaded_process
   - Description: Kills the process started by the 7-highlander script.

## Usage

To execute any of the scripts, follow these steps:
1. Clone this repository to your local machine.
2. Navigate to the project directory: `cd alx-system_engineering-devops/0x05-processes_and_signals`
3. Make the script executable: `chmod +x <script_name>`
4. Run the script: `./<script_name>`

## Contributing

Contributions to this project are welcome. If you find any issues or have improvements to suggest, please open an issue or submit a pull request.
