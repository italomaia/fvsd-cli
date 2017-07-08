#!/home/italomaia/.virtualenvs/fv/bin/python
import re
import sys
import shutil
import zipfile
import os.path
import tempfile
import urllib.request

c_prj_name = re.compile(r'^[a-z\-]+$')


def cmd_exists(cmd):
    return shutil.which(cmd) != ''


def call_new(name):
    assert c_prj_name.match(name), '' \
        'Invalid project name. Accepted characters are [a-z],-'
    assert cmd_exists('git'), 'Please, install git. It is required.'

    print('downloading remote resources')
    filename, headers = urllib.request.urlretrieve('https://codeload.github.com/italomaia/flask-vue-semantic-docker/zip/master')

    print('unzipping')
    zfile = zipfile.ZipFile(filename)
    namelist = zfile.namelist()
    commonprefix = os.path.commonprefix(namelist)
    tmp_dir = tempfile.mkdtemp()
    zfile.extractall(tmp_dir)
    zfile.close()
    print('copying')
    source = os.path.join(tmp_dir, commonprefix)
    shutil.move(source, name)
    shutil.rmtree(tmp_dir)
    print('Enjoy your project! \nps: run setup.sh ;)')


def main(args):
    if len(args) == 2:
        if args[0] == 'new':
            call_new(args[1])
        else:
            print('command not found')
    else:
        print('command not found')


if __name__ == '__main__':
    main(sys.argv[1:])