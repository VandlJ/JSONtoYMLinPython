import json

# Define file paths
load_balancer_ip_file = 'load_balancer_ip.json'
inventory_file = 'inventory.yml'

# Read load balancer IP
try:
    with open(load_balancer_ip_file, 'r') as f:
        load_balancer_ip = json.load(f)
except FileNotFoundError:
    print(f"Error: {load_balancer_ip_file} not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON from {load_balancer_ip_file}: {e}")
    exit(1)

# Validate the load balancer IP
if not isinstance(load_balancer_ip, str):
    print(f"Error: {load_balancer_ip_file} does not contain a valid string IP.")
    exit(1)

# Generate the inventory file
try:
    with open(inventory_file, 'w') as f:
        
        # Write load balancer
        f.write("\nload_balancer:\n  hosts:\n")
        f.write(f"    {load_balancer_ip}:\n")
except Exception as e:
    print(f"Error while writing to {inventory_file}: {e}")
    exit(1)

print(f"Ansible inventory file has been successfully generated at {inventory_file}.")