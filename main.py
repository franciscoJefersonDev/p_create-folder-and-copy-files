import os
import shutil

entries = os.listdir('my-folder')
dir = '/home/francisco/Área de Trabalho/workspace/python/automization/create-folder-and-copy-file/teste'
dirFiles = '/home/francisco/Área de Trabalho/workspace/python/automization/create-folder-and-copy-file/my-folder/'
for entry in entries:
    directoryDir = entry.split('.')[0]
    directoryFile = entry
    file = os.path.join(dirFiles, directoryFile)
    folder = os.path.join(dir, directoryDir)
    os.mkdir(folder)
    shutil.copyfile(file, folder + '/' + entry, follow_symlinks=True)