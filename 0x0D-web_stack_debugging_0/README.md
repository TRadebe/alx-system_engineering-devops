# ALX System Engineering DevOps - Web Stack Debugging

Welcome to the first debugging project in the ALX System Engineering DevOps curriculum. In this project, 
your goal is to get Apache running inside a Docker container and have it return a page containing "Hello Holberton" 
when querying the root of the container.

## Table of Contents

1. [Debugging Task](#debugging-task)

### Debugging Task

#### Task 0: Give Me a Page!

**Requirements:**
- Debug the Docker container to make Apache run properly.
- Ensure that querying the root of the container returns a page containing "Hello Holberton."

**Example:**
```shell
$ docker run -p 8080:80 -d -it holbertonschool/265-0
$ docker ps
$ curl 0:8080
Hello Holberton
```

**Solution:**
To solve this issue, you can follow these steps:

1. Start the Docker container with the correct image and port mapping:
   ```shell
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

2. Verify the container is running:
   ```shell
   docker ps
   ```

3. Use `curl` to query the root of the container:
   ```shell
   curl 0:8080
   ```

This should return "Hello Holberton" if Apache is properly configured and running inside the container.

## Repository Information

- GitHub Repository: [alx-system_engineering-devops](https://github.com/your-github-username/alx-system_engineering-devops)
- Directory: 0x0D-web_stack_debugging_0
- File: 0-give_me_a_page

Please document your debugging steps in the provided repository and submit your solution. Good luck with debugging the web stack!
