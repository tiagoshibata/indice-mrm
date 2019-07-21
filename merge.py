import sys

with open(sys.argv[1]) as f, open('out.md', 'w') as output:
    lines = [x.rstrip().split('](https://') for x in f.readlines()]
    last_title = None
    content = []
    for x in lines:
        # print(x)
        title, link = x
        if title == last_title:
            content.append(' [[{}]](https://{}'.format(len(content), link))
        else:
            last_title = title
            output.write('{}\n'.format(''.join(content)))
            content = ['{}](https://{}'.format(title, link)]
