#!/usr/bin/python

import sys
import tempfile
import re
import tarfile
import urllib.request
import os

# Extract
def extract(fname):
    d = tempfile.TemporaryDirectory()
    try:
        tar = tarfile.open(fname, "r:gz")
        tar.extractall(d.name)
        tar.close()
    except Exception as e:
        print('Error: could not extract files. Must be valid .tgz file')
        return None

    return d


def get_ids(fname):
    p = re.compile(r'project4\.([a-zA-Z]{4}[0-9]{4})(?:\.([a-zA-Z]{4}[0-9]{4}))?\.tgz')
    m = p.match(fname.split('/')[-1])
    if m is None:
        return False, []
    id1, id2 = m.groups()
    if id1 == 'erwu1234' or id1 is None:
        return False, []

    if id2 is None:
        return True, [id1]
    else:
        return True, [id1, id2]


def getcookie(ids):
    import hashlib
    return int(hashlib.sha1(b'|'.join(sorted([a.encode('utf-8') for a in ids]))).hexdigest(),16) % 0x8FFF

def check_files(temp_d, ids):
    ret = True
    for i in range(7):
        sol = 'sol%d.py' % i
        fname = os.path.join(temp_d.name, sol)
        if not(os.path.isfile(fname)):
            print('Error: could not find %s' % sol)
            ret = False
            continue
    if ret == False:
        return False

    # check that shellcode.py is NOT there
    fname = os.path.join(temp_d.name, 'shellcode.py')
    if os.path.isfile(fname):
        print('Error: please remove shellcode.py from your submission')
        return False

    # check cookie
    fname = os.path.join(temp_d.name, 'cookie')
    if not(os.path.isfile(fname)):
        print('Error: no cookie file!')
        return False

    expected_cookie = getcookie(ids)
    with open(fname, 'rb') as f:
        cookie = int(f.read())
        if cookie != expected_cookie:
            print('Error: wrong cookie value. Did you run `./setcookie %s` and `make clean && make`?' % ' '.join(ids))
            return False

    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Use:')
        print('   python3 %s project4.[identikey].tgz' % sys.argv[0])
        sys.exit(1)

    fname = sys.argv[1]

    valid, ids = get_ids(fname)
    if not(valid):
        print('Error: invalid filename format. Must be "project4.[identikey(s)].tgz"')
        print('   e.g. project4.erwu1234.tgz  or  project4.erwu1234.abcd5678.tgz')
        sys.exit(1)

    temp_d = extract(fname)
    if temp_d is None:
        sys.exit(1)


    if check_files(temp_d, ids):
        print('============================')
        print('Passed format check, hooray!')
        print('============================')
        print('Note: this does NOT mean solutions are correct or guarantee a grade,')
        print('only that the format is correct. Please test that your solutions have')
        print('the intended behavior')
    else:
        print('!!!!!!!!!!!!!!!!!!!')
        print('Did not pass format check, please fix!')
        print('!!!!!!!!!!!!!!!!!!!')


