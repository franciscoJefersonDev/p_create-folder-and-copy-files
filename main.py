import os
import shutil

entries = os.listdir('my-folder')
dir = '/home/francisco/Área de Trabalho/workspace/python/automization/create-folder-and-copy-file/'
dirFiles = '/home/francisco/Área de Trabalho/workspace/python/automization/create-folder-and-copy-file/my-folder/'
for entry in entries:
    directoryDir = entry.split('.')[0]
    directoryFile = entry
    file = os.path.join(dirFiles, directoryFile)
    folder = os.path.join(dir, directoryDir)
    os.mkdir(folder)
    shutil.copyfile(file, folder + '/' + entry, follow_symlinks=True)
    # print(file)
    # print(folder)
    # shutil.copyfile(file, folder+entry, follow_symlinks=True)
    # os.mkdir(path)
    # print(path)
    # shutil.copyfile(file, folder)

# shutil.copyfile(dirFiles+'L100_F001_A001.pdf', '/')

