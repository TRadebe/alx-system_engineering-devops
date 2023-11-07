# Web Stack Debugging 3

## Background Context

When debugging, logs may not be enough. Whether the software is breaking unexpectedly or logs are not providing sufficient information, 
sometimes you need to go deeper into the stack. In this project, you'll delve into debugging a WordPress website running on a LAMP stack, 
which is a common technology stack used for web development.

WordPress powers 26% of the web, making it highly likely that you'll encounter it in your career. 
The LAMP stack, consisting of Linux, Apache, MySQL, and PHP, is widely used to run WordPress and many other websites.

## Requirements

- All files interpreted on Ubuntu 14.04 LTS.
- Files should end with a new line.
- A mandatory `README.md` file at the root.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
- Puppet manifests must run without error.
- Puppet manifests should start with a comment explaining their purpose.
- Puppet manifests files must end with the extension `.pp`.

## Tasks

### 0. Strace is your friend (mandatory)

Using `strace`, find out why Apache is returning a 500 error. Once you identify the issue, fix it, and automate the fix using Puppet instead of Bash.

#### Hint:

- `strace` can attach to a currently running process.
- Use `tmux` to run `strace` in one window and `curl` in another.

#### Requirements:

- Your `0-strace_is_your_friend.pp` file must contain Puppet code.
- Use any Puppet resource type for your fix.

#### Example:

```bash
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
<div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>
<h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
<p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#
```
