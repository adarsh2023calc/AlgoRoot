


import os

import webbrowser

import psutil

import subprocess



def open_chrome():
    webbrowser.open("https://www.google.com")





# Windows only

def open_calculator():
    
    os.system("calc" if os.name == "nt" else "gnome-calculator")


#Linux On;ly
def open_terminal():
    
    os.system("gnome-terminal" if os.name == "posix" else "cmd")


def get_cpu_usage():
    
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    """Returns the current RAM usage percentage."""
    return psutil.virtual_memory().percent

def get_disk_usage():
    """Returns disk usage details."""
    disk_usage = psutil.disk_usage("/")
    return {"total": disk_usage.total, "used": disk_usage.used, "free": disk_usage.free, "percent": disk_usage.percent}

# Command Execution
def run_shell_command(command):
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
    except Exception as e:
        return f"Error executing command: {e}"

# Process Management
def list_processes():
    """Lists all running processes."""
    return [proc.info for proc in psutil.process_iter(attrs=['pid', 'name'])]

def kill_process(pid):
    """Terminates a process by its PID."""
    try:
        os.kill(pid, 9)
        return f"Process {pid} terminated."
    except Exception as e:
        return f"Error: {e}"

# Network Operations
def get_public_ip():
    """Returns the public IP address of the machine."""
    try:
        return run_shell_command("curl -s ifconfig.me")
    except Exception as e:
        return f"Error fetching IP: {e}"

def ping_host(host):
    """Pings a host and returns the response."""
    command = f"ping -c 4 {host}" if os.name != "nt" else f"ping -n 4 {host}"
    return run_shell_command(command)

# File Operations
def create_file(filename, content=""):
    """Creates a new file with optional content."""
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"File '{filename}' created successfully."
    except Exception as e:
        return f"Error: {e}"

def delete_file(filename):
    """Deletes a specified file."""
    try:
        os.remove(filename)
        return f"File '{filename}' deleted successfully."
    except Exception as e:
        return f"Error: {e}"

# Example function registry dictionary
FUNCTION_REGISTRY = {
    "open_chrome": open_chrome,
    "open_calculator": open_calculator,
    "get_cpu_usage": get_cpu_usage,
    "get_ram_usage": get_ram_usage,
    "get_disk_usage": get_disk_usage,
    "run_shell_command": run_shell_command,
    "list_processes": list_processes,
    "kill_process": kill_process,
    "get_public_ip": get_public_ip,
    "ping_host": ping_host,
    "create_file": create_file,
    "delete_file": delete_file,
}


