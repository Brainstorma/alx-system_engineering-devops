# 0x0A Configuration Management

## Overview

This repository contains three tasks related to configuration management with Puppet. Each task involves writing Puppet code that configures a specific component of a server.

## Tasks

The tasks include:

1. [Install Puppet](./0-create_a_file.pp): write a Puppet manifest that creates a file in the `/tmp` directory.
2. [Execute a command](./1-install_a_package.pp): write a Puppet manifest that installs the `puppet-lint` package.
3. [Create a manifest](./2-execute_a_command.pp): write a Puppet manifest that creates a new user, installs the `nginx` package and starts the `nginx` service.

Each task is contained in a separate directory, and includes a README file with specific instructions on how to execute the Puppet code.

## Requirements

To run the Puppet code in this repository, you will need to have Puppet installed on your system. The code has been tested with Puppet version 6.24.0.

## Usage

To execute the Puppet code for any of the tasks, navigate to the appropriate directory and run the command:

```
sudo puppet apply <FILENAME>.pp
```

Where `<FILENAME>` is the name of the Puppet manifest file for the task.

For example, to execute the Puppet code for Task 1:

1. Navigate to the `0-create_a_file` directory.
2. Run the command:

```
sudo puppet apply 0-create_a_file.pp
```

This will create a file called `/tmp/ALX` on the server.

## Conclusion

The Puppet code in this repository demonstrates basic configuration management practices, including installing packages and executing commands, and can be used as a starting point for more complex configuration management tasks.
