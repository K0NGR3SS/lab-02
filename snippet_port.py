import re

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
    with open(logs_file, 'r') as f:
        for line in f:
            print(ip_parse(line.strip()))      