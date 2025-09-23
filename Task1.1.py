import re

ip_list = []

logs_file = "gavno.log"
"""
def simple_parser(line):

    if " port " in line:
        parts = line.split() # splits the line into tokens, separates by spaces by default
        try:
            anchor = parts.index("port")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            return port.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None
    return None
"""
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

if __name__ == "__main__":
    scanned_lines = 0
    with open(logs_file) as f:
        for line in f:
            i = ip_parse(line.strip())
            if i != None:
                if ":" in i:
                    i = i[:-1]
                    ip_list.append(i)
                else:
                    ip_list.append(i)
            scanned_lines += 1
    unique_ips = set(ip_list)
    unique_number = len(unique_ips)
    sorted_ips = sorted(unique_ips)
    print("Lines read: ", scanned_lines)
    print("Unique IPs: ", unique_number)
    print("First 10 IPs: ", sorted_ips[:10])

