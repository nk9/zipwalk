# zipwalk

A very simple walker that recursively walks through nested zipfiles

## About

This project was created because I needed a way to iterate over nested zipfiles
without unzipping them.

## Install

```sh
pip install zipwalk
```

## Usage

It has a similar interface to `os.walk`:

```py
from zipwalk import zipwalk

for root, zips, files in zipwalk('tests/1.zip'):
    print('root:', root.filename)
    print('zips:', zips)
    print('files:', files)

# output:
# root: tests/1.zip
# zips: {'2.zip'}
# files: {'1c.txt', 'dir/d1.txt', '1b.txt', '1a.txt'}
# root: 2.zip
# zips: set()
# files: {'2c.txt', '2b.txt', '2a.txt'}
```

`root` is an instance of `ZipWalkFile`. This is just a subclass of [ZipFile][1] with an additional `zpath` attribute. The ZipFile is opened in read mode, `r`. All zip files are
opened using a `with` context manager and will be closed once the generator is
exhausted.

You can use the zip walker like the following:

```py
from pathlib import Path
from zipfile import ZipFile

from zipwalk import zipwalk

zipwalk(ZipFile('tests/1.zip'))
zipwalk(Path('tests/1.zip'))
zipwalk('tests/1.zip')
```

To get the absolute path of nested files or directories, you can use the `zpath` attribute:

```py
from zipwalk import zipwalk

for root, zips, files in zipwalk('tests/1.zip'):
    print(' path:', root.zpath)
    print('rpath:', root.zpath.resolve())

# output:
#  path: PosixPath('tests/1.zip')
# rpath: PosixPath('/home/neo/zipwalk/tests/1.zip')
#  path: PosixPath('tests/1.zip/2.zip')
# rpath: PosixPath('/home/neo/zipwalk/tests/1.zip/2.zip')
```

[1]: https://docs.python.org/3/library/zipfile.html
