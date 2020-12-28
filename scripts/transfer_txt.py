import os
import re
import sys
import json

FILE_DIR = os.path.dirname(os.path.realpath(__file__))

def to_text(dir_path):
    file_list = os.listdir(dir_path)
    new_dir_path = dir_path + '.NEW'
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)

    all_contents = ''
    for fn in range(len(file_list)):
        file = 'comments{}-{}.json'.format(fn*100+1, (fn+1)*100)
        file_path = os.path.join(dir_path, file)
        contents = json.loads(open(file_path, 'rb').read().decode(errors='ignore'))['results']

        out_contents = ''
        for i in range(len(contents)):
            id = contents[i]["id"]
            author_avatar = contents[i]["author_avatar"]
            author_url = contents[i]["author_url"]
            author_alias = contents[i]["author_alias"]
            author_signature = contents[i]["author_signature"]
            author_nickname = contents[i]["author_nickname"]
            topic_author = contents[i]["topic_author"]
            created_at = contents[i]["created_at"]
            reply_to_url = contents[i]["reply_to_url"]
            reply_to = contents[i]["reply_to"]
            reply_quote_content = contents[i]["reply_quote_content"]
            content = contents[i]["content"]
            img = contents[i]["img"]
            out_content = ''
            out_content += '-' * 20 + '\n'
            out_content += author_nickname + ('    ' + topic_author if topic_author else '') + '    ' + created_at + '\n\n'
            if reply_to:
                out_content += '    |  ' + reply_quote_content.replace('\n', '\n    |  ') + '\n'
                out_content += '    |\n'
                out_content += '    |  -- ' + reply_to + '\n'
                out_content += '\n'
            if img:
                out_content += '  ' + img + '\n'
            out_content += ' ' + content.replace('\n', '\n  ') + '\n'
            out_content += '-' * 20 + '\n'
            out_content += '\n'
            out_content += '\n'
            out_contents += out_content 

        all_contents += out_contents
        f = open(os.path.join(new_dir_path, file.replace('.json', '.txt')), 'wb+')
        f.write(out_contents.encode())
        f.close()
    f = open(os.path.join(new_dir_path, 'all_comments.txt'), 'wb+')
    f.write(all_contents.encode())
    f.close()

def main():
    to_text(sys.argv[1])

if __name__ == '__main__':
    main()
    
