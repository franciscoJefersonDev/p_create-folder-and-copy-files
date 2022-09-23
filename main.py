import os
from os import path
import shutil
# ==========
# print(path.abspath('')
fromDir = 'my-folder'
toDir = 'teste'
entries = os.listdir(path.abspath(fromDir))
# ==========
for entry in entries:
    directoryDir = entry.split('.')[0]
    directoryFile = entry
    folder = os.path.join(path.abspath(toDir), directoryDir)
    os.mkdir(folder)
    file = os.path.join(path.abspath(fromDir), directoryFile)
    fileCopy = '{folder}/{entry}'.format(folder=folder, entry=entry)
    shutil.copyfile(file, fileCopy, follow_symlinks=True)
# ===========
