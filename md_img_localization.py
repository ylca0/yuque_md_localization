# coding : utf-8
import re
import requests
import os

filename = 'xxxxxx' # without .md postfix.
os.makedirs(f'images/{filename}.assets')
f = open(f'{filename}.md', encoding='utf-8')
md_content = f.read()
f.close()


m = re.findall('\!\[image.png\]\((.*).*\)', md_content)

for i in m:
    striped_url = i.split('#')[0]
    print(striped_url)
    # print(content.find(rf'![image.png]({i})'))
    # continue
    r = requests.get(striped_url)
    png_path = f'images/{filename}.assets/' + striped_url.split('/')[-1]
    png_name = striped_url.split('/')[-1]
    f = open(png_path, 'wb')
    f.write(r.content)
    f.close()
    md_content = md_content.replace(rf'![image.png]({i})', f'![{png_name}]({png_path})')

f = open(f'{filename}.md', 'w')
f.write(md_content)
f.close()