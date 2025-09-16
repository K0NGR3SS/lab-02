import re

ips = []
pattern = r"\d+\.\d+\.\d+\.\d+"
with open('auth.log', 'r') as f:
    ip = re.findall(pattern, str(f.readlines()))

found_ips = set(ip)

with open('unique_ips.txt', 'w') as g:
    for ip in found_ips:
        g.write(ip)
        g.write("\n")