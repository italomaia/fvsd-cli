#!/usr/bin/python3

'''
CLI boilerplate for the Flask+VueJS+SemanticUI+Nginx+Docker project
'''

import argparse
import os
import re
import shutil
import tempfile
import zipfile
from subprocess import run
from urllib.request import urlretrieve  # py3

c_prj_name = re.compile(r'^[a-z][a-z0-9\-]*$')


def cmd_exists(cmd):
    return shutil.which(cmd) != ''


def call_new(name, branch):
    assert c_prj_name.match(name), '' \
        'Invalid project name. Accepted characters are [a-z],-'
    assert cmd_exists('git'), 'Please, install git. It is required.'

    print('Creating a vue+flask+semantic-ui+docker project ...')
    print('Downloading remote resources')
    remote_source = f'https://codeload.github.com/italomaia/flask-vue-semantic-docker/zip/{branch}'
    filename, headers = urlretrieve(remote_source)

    print('UnZipping')
    zfile = zipfile.ZipFile(filename)
    namelist = zfile.namelist()
    commonprefix = os.path.commonprefix(namelist)
    tmp_dir = tempfile.mkdtemp()
    zfile.extractall(tmp_dir)
    zfile.close()

    # clean up after ourselves
    os.remove(filename)

    print('Moving files')
    source = os.path.join(tmp_dir, commonprefix)
    shutil.move(source, name)
    shutil.rmtree(tmp_dir)
    os.chdir(name)
    print('Finished.')

    if cmd_exists('fab'):
        print(
            "Fabric was found in your path. Continuing setup ... "
            "please, wait")
        run(['fab', 'setup'])
    else:
        print("Fabric could not be found in your PATH.")
        print("Please, run \"fab setup\" manually after installing it.")


def get_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-n', '--new', dest='name', type=str, action='store',
        help='creates a FVSD project with given name')
    parser.add_argument(
        '-b', '--branch', dest='branch', type=str, action='store',
        default='master', help='clone from a non-default branch')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.name:
        call_new(args.name, args.branch)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()