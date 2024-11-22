import json

# Define file paths
backend_ips_file = 'backend_ips.json'

# Read backend IPs
try:
    with open(backend_ips_file, 'r') as f:
        backend_ips = json.load(f)
except FileNotFoundError:
    print(f"Error: {backend_ips_file} not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON from {backend_ips_file}: {e}")
    exit(1)

# Validate the content of backend_ips
if not isinstance(backend_ips, list) or not all(isinstance(ip, str) for ip in backend_ips):
    print(f"Error: {backend_ips_file} does not contain a valid list of IPs.")
    exit(1)
