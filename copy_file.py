with open('sample.txt', 'r') as f:
    for line in f:
        with open('copy.txt', 'a') as g:
            g.write(line)