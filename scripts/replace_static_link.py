import os
import re
import sys
import time

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = os.path.join(os.path.dirname(FILE_DIR), 'image')

def link_replacement(dir_path):
    file_list = os.listdir(dir_path)
    new_dir_path = dir_path + '.NEW'
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)

    for file in file_list:
        file_path = os.path.join(dir_path, file)
        f = open(file_path, 'rb')
        content = f.read().decode(errors='ignore')
        f.close()

        pattern = re.compile(r'https://img.*jpg')
        result = pattern.findall(content)
        for r in result:
            if 'group_topic' in  r and os.path.exists(os.path.join(IMG_DIR, 'group_topic', os.path.basename(r))):
                content = content.replace(r, '../../image/group_topic/'+ os.path.basename(r))
            elif 'richtext' in  r and os.path.exists(os.path.join(IMG_DIR, 'richtext', os.path.basename(r))):
                content = content.replace(r, '../../image/richtext/'+ os.path.basename(r))
            elif 'icon' in  r and os.path.exists(os.path.join(IMG_DIR, 'icon', os.path.basename(r))):
                content = content.replace(r, '../../image/icon/' + os.path.basename(r))

        f = open(os.path.join(new_dir_path, file), 'wb+')
        f.write(content.encode())
        f.close()

def main():
    link_replacement(sys.argv[1])

if __name__ == '__main__':
    main()
    
