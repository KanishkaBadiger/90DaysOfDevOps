"""
# Linux Architecture, Processes & systemd

## Linux Architecture
- **Kernel:** Core of Linux that manages CPU, memory, devices, file systems, networking, and processes.
- **User Space:** Where user applications such as Chrome, Python, Docker, and VS Code run.
- **systemd (Init System):** The first userspace process (PID 1) that starts and manages system services during boot.

## Process Management
A process is a running instance of a program. Every process has a unique Process ID (PID).

### Process States
- **Running (R):** Currently executing on the CPU.
- **Sleeping (S):** Waiting for an event or resource.
- **Stopped (T):** Paused manually or by a signal.
- **Zombie (Z):** Finished execution but waiting for the parent process to collect its exit status.
- **Dead (X):** Completely terminated.

## Why systemd Matters
- Starts services during system boot.
- Manages background services.
- Automatically restarts failed services.
- Provides logs through `journalctl`.
- Simplifies service management with `systemctl`.

## Five Daily Linux Commands
| Command | Purpose |
|---------|---------|
| `ps aux` | View running processes |
| `top` | Monitor system resources |
| `systemctl status <service>` | Check service status |
| `journalctl -u <service>` | View service logs |
| `kill <PID>` | Terminate a process |

## Key Takeaways
- The kernel is the heart of Linux.
- Applications run in User Space and communicate with the kernel.
- Every running program is a process with a unique PID.
- systemd manages services and is essential for production Linux systems.


"""