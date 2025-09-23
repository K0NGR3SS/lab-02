import time
import re
from collections import defaultdict

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

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

counts = defaultdict(int)
start = time.time()
with open("gavno.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1

with open("attackerips.log", "w") as g:
    g.write("count  |   ip\n")
    for ip, count in counts.items():
        g.write(f"{count}   |   {ip}\n")

fiveattackers = top_n(counts, 5)

end = time.time()

print("Top 5 attackers: ")
i = 1
for ip, count in fiveattackers:
    print(f"{i}. {ip} -- {count}")
    i += 1
print("Time taken: ", end - start, "seconds")
print("Elapsed:", end-start, "seconds")