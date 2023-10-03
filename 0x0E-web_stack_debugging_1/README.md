### Task 0: Nginx likes port 80

#### README.md

```markdown
# Web Stack Debugging 1

## Task 0: Nginx likes port 80

### Requirements:

- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root is mandatory
- Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all Bash scripts should be a comment explaining the script's purpose
- You cannot use wget

### Task Description:

Using debugging skills, find out why the Ubuntu container's Nginx installation is not listening on port 80. 
Write a Bash script with the minimum number of commands to automate the fix.

#### Example:

```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```

#### Repository Information:

- GitHub repository: [alx-system_engineering-devops](repository_link)
- Directory: 0x0E-web_stack_debugging_1
- File: 0-nginx_likes_port_80

### Task 1: Make it sweet and short

#### README.md

```markdown
# Web Stack Debugging 1

## Task 1: Make it sweet and short

### Requirements:

- Bash script must be 5 lines long or less
- There must be a new line at the end of the file
- Usual Bash script requirements must be respected
- You cannot use ;
- You cannot use &&
- You cannot use wget
- You cannot execute the previous answer file (Do not include the name of the previous script in this one)
- `service` (init) must say that nginx is not running for real

#### Example:

```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```

#### Repository Information:

- GitHub repository: [alx-system_engineering-devops](repository_link)
- Directory: 0x0E-web_stack_debugging_1
- File: 1-debugging_made_short
```
