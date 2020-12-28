import os
import re
import ssl
import sys
import time
import random
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = os.path.join(os.path.dirname(FILE_DIR), 'image')

def download_from_url(url, target_path):
    if not os.path.exists(os.path.dirname(target_path)):
        os.makedirs(os.path.dirname(target_path))
    if not os.path.exists(target_path):
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh,zh-CN;q=0.8,zh-TW;q=0.6,en;q=0.4,en-US;q=0.2',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/538.36 (KHTML, like Gecko) '
            'Chrome/57.0.3029.110 Safari/538.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'https://www.douban.com/people/junbaoyang/',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }
        request = urllib.request.Request(url, headers=headers)
        fin = urllib.request.urlopen(request)
        fout = open(target_path, 'wb')
        fout.write(fin.read())
        fout.close()
        time.sleep(2*random.uniform(0.5, 1.5))

def file_parser(file_path):
    f = open(file_path, 'rb')
    content = f.read().decode(errors='ignore')
    f.close()
    pattern = re.compile(r'https://img.*jpg')
    result = pattern.findall(content)
    print(result)
    return list(set(result))

def main():
    dir_path = sys.argv[1]
    file_list = os.listdir(dir_path)
    for file in file_list:
        file_path = os.path.join(dir_path, file)
        print('='*20)
        print('Parsing file: {}'.format(file_path))
        links = file_parser(file_path)
        print("total: {}".format(len(links)))
        count = 0
        for l in links:
            count += 1
            print('downloading {} ...'.format(count))
            img_category = 'group_topic' if 'group_topic' in l else ('richtext' if 'richtext' in l else 'icon')
            download_from_url(l, os.path.join(IMG_DIR, img_category, os.path.basename(l)))
            print('done.')
            print('----------')
        print('='*20)
        print()

if __name__ == '__main__':
    main()
    
