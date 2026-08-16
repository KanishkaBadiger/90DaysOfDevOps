# Linux Commands Cheatsheet

A quick reference for commonly used Linux commands in DevOps and troubleshooting.

## 1. File & Directory Management

| Command                     | Usage                                                  |
| --------------------------- | ------------------------------------------------------ |
| `pwd`                       | Shows the current working directory.                   |
| `ls`                        | Lists files and directories.                           |
| `ls -la`                    | Lists all files, including hidden files, with details. |
| `cd <directory>`            | Changes the current directory.                         |
| `mkdir <directory>`         | Creates a new directory.                               |
| `touch <file>`              | Creates an empty file or updates its timestamp.        |
| `cp <source> <destination>` | Copies files or directories.                           |
| `mv <source> <destination>` | Moves or renames a file or directory.                  |
| `rm <file>`                 | Deletes a file.                                        |
| `cat <file>`                | Displays the contents of a file.                       |

## 2. Process Management

| Command         | Usage                                                          |
| --------------- | -------------------------------------------------------------- |
| `ps aux`        | Displays currently running processes.                          |
| `top`           | Monitors processes and CPU/memory usage in real time.          |
| `pgrep <name>`  | Finds the PID of processes matching a name.                    |
| `kill <PID>`    | Sends a termination signal to a process.                       |
| `kill -9 <PID>` | Forcefully terminates a process when normal termination fails. |

## 3. System Information

| Command    | Usage                                                         |
| ---------- | ------------------------------------------------------------- |
| `uname -a` | Displays Linux kernel and system information.                 |
| `df -h`    | Shows available and used disk space in human-readable format. |
| `free -h`  | Displays RAM and swap memory usage.                           |
| `uptime`   | Shows how long the system has been running and system load.   |
| `whoami`   | Shows the currently logged-in user.                           |

## 4. Networking & Troubleshooting

| Command        | Usage                                                           |
| -------------- | --------------------------------------------------------------- |
| `ip addr`      | Displays network interfaces and IP addresses.                   |
| `ping <host>`  | Checks network connectivity to a host.                          |
| `curl <URL>`   | Sends requests to a URL and is useful for testing web services. |
| `dig <domain>` | Queries DNS information for a domain.                           |
| `ss -tuln`     | Shows listening TCP/UDP network ports.                          |

## 5. Services & Logs

| Command                      | Usage                                         |
| ---------------------------- | --------------------------------------------- |
| `systemctl status <service>` | Checks the status of a systemd service.       |
| `systemctl start <service>`  | Starts a service.                             |
| `systemctl stop <service>`   | Stops a service.                              |
| `journalctl -u <service>`    | Displays logs for a specific systemd service. |
| `journalctl -f`              | Continuously follows new system logs.         |

## Quick Troubleshooting Flow

When a Linux server has an issue:

1. Check the system:
   `uptime`, `free -h`, `df -h`

2. Check processes:
   `ps aux`, `top`

3. Check network:
   `ip addr`, `ping`, `ss -tuln`

4. Check services:
   `systemctl status <service>`

5. Check logs:
   `journalctl -u <service>`

## Key Takeaways

* `ps` and `top` help investigate processes and resource usage.
* `df` and `free` help identify disk and memory problems.
* `ip`, `ping`, `dig`, `curl`, and `ss` are useful for network troubleshooting.
* `systemctl` manages services.
* `journalctl` helps investigate service and system problems.
