from collections import defaultdict
import re

def ip_parse(line):
    if " from " in line:
        parts = line.split()
        try:
            anchor = parts.index("from")
            ip = parts[anchor+1]
            pattern = r"\d+\.\d+\.\d+\.\d+"
            if re.match(pattern, ip):
                return ip.strip()
                
        except (ValueError, IndexError):
            return None
    return None

counts = defaultdict(int)           # Create a dictionary to keep track of IPs


with open("gavno.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
print(counts)