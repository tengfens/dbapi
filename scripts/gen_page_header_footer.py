import os
import re
import sys
import time

FILE_DIR = os.path.dirname(os.path.realpath(__file__))

def add_page_link(dir_path):
    comment_title = '''

## 留言
---
'''
    pre_nxt_template = '''
[主页](./%s "%s") | [首页](./%s "%s") | [前一页](./%s "%s") | [后一页](./%s "%s") | [末页](./%s "%s")  

---
'''
    current_page_template = '''
%s-%s

---
'''
    file_list = os.listdir(dir_path)
    cnt = len(file_list) - 1
    whole_pages = ''
    for i in range(cnt):
        page_link = '[{}-{}](./comments{}-{}.md \"{}-{}\")  '.format(i*100+1, i*100+100, i*100+1, i*100+100, i*100+1, i*100+100)
        whole_pages = whole_pages + page_link

    new_dir_path = dir_path + '.NEW'
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)

    f = open(os.path.join(dir_path, 'main.md'), 'rb')
    content = f.read().decode(errors="ignore")
    f.close()
    content = content + comment_title + whole_pages
    f = open(os.path.join(new_dir_path, 'main.md'), 'wb+')
    f.write(content.encode())
    f.close()

    main_page = 'main.md'
    first_page = 'comments1-100.md'
    last_page = 'comments{}-{}.md'.format((cnt-1)*100+1, cnt*100)
    for i in range(cnt):
        current_page = 'comments{}-{}.md'.format(i*100+1, (i+1)*100)
        prev_page = 'comments{}-{}.md'.format((i-1)*100+1, i*100) if i>=1 else first_page
        next_page = 'comments{}-{}.md'.format((i+1)*100+1, (i+2)*100) if i<=cnt-2 else last_page

        f = open(os.path.join(dir_path, current_page), 'rb')
        content = f.read().decode(errors="ignore")
        f.close()

        cur_page = current_page_template % (str(i*100+1), str((i+1)*100))
        pre_nxt_page = pre_nxt_template % (main_page, main_page, first_page, first_page, prev_page, prev_page, next_page, next_page, last_page, last_page)
        content = pre_nxt_page + content + cur_page + pre_nxt_page + whole_pages

        f = open(os.path.join(new_dir_path, current_page), 'wb+')
        f.write(content.encode())
        f.close()

def main():
    add_page_link(sys.argv[1])

if __name__ == '__main__':
    main()
    
