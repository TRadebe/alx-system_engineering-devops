### Configuration Management Project

## Requirements

### General

- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- The first line of all your Puppet manifests should be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp

### Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

#### Install puppet

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

This project is simply a set of tasks to familiarize you with the basic level syntax, which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](puppet_docs_link)

#### Install puppet-lint

```bash
$ gem install puppet-lint
```

## Tasks

### Task 0: Create a file

Using Puppet, create a file in `/tmp`.

#### Requirements:

- File path is `/tmp/school`
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains `I love Puppet`

#### Example:

```bash
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
```

#### Repository Information:

- GitHub repository: [alx-system_engineering-devops](repository_link)
- Directory: 0x0A-configuration_management
- File: 0-create_a_file.pp

### Task 1: Install a package

Using Puppet, install Flask from pip3.

#### Requirements:

- Install Flask
- Version must be 2.1.0

#### Example:

```bash
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
```

#### Repository Information:

- GitHub repository: [alx-system_engineering-devops](repository_link)
- Directory: 0x0A-configuration_management
- File: 1-install_a_package.pp

### Task 2: Execute a command

Using Puppet, create a manifest that kills a process named `killmenow`.

#### Requirements:

- Must use the `exec` Puppet resource
- Must use `pkill`

#### Example:

```bash
Terminal #0 - starting my process

root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```

```bash
Terminal #1 - executing my manifest

root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/#
```

```bash
Terminal #0 - process has been terminated

root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```

#### Repository Information:

- GitHub repository: [alx-system_engineering-devops](repository_link)
- Directory: 0x0A-configuration_management
- File: 2-execute_a_command.pp
