import grequests
import os


def get_tree_size(path):
    for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as error:
            continue
        if is_dir:
            get_tree_size(entry.path)
        else:
            try:
                name, file_extension = os.path.splitext(entry.path)
                if file_extension == ".swift" and "Localization+Constants" not in name:
                    print(entry.path)
                    input_file = open(entry.path, "r")
                    for line in input_file:
                        matches = re.finditer(regex, line, re.IGNORECASE)
                        for matchNum, match in enumerate(matches):
                            group = match.groups()[0]
                            output_file.write("/// \"{group}\"\r\n".format(group = group))
                            key = group.lower().replace(" ", "_")
                            output_file.write("static let {key} = {matches}\r\n".format(key = key, matches = match.group()))
                            output_file.write("\r\n")                            
                    entry.stat(follow_symlinks=False).st_size
            except UnicodeDecodeError as error:
                output_file.write(entry.path)
                print('Error calling stat():', error, file=sys.stderr)
            except OSError as error:
                print('Error calling stat():', error, file=sys.stderr)


urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]

rs = (grequests.get(u) for u in urls)

print(grequests.map(rs))

import multiprocessing
print(multiprocessing.cpu_count())                
