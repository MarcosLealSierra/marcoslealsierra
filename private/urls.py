urls = {}
with open('urls', 'r') as f:
    for line in f:
        line = line.replace(' ','').replace('\n', '')
        (key, value) = line.split(':')
        urls[key] = value

urls.update(B='Shalala', C='Lararara')
print(urls)
