# Add version number to the name, for easily installation of multiple versions
# addVersionToNames.py /path/to/Font1.otf /path/to/Font2.otf

from fontTools.ttLib import TTFont
import sys
import os

paths = sys.argv[1:]

for path in paths:
    path = path.strip('\"')
    f = TTFont(path)


    findName = f['name'].getName(25, 1, 0, 0).toUnicode()
    #print('find', findName)
    versionName = f['name'].getName(3, 3, 1, 0x409).toUnicode()
    versionNumber = versionName.split(';')[0]
    varNoSpace = 'Beta'+versionNumber
    varSpace = ' ' + varNoSpace


    for namerecord in f['name'].names:
        new = namerecord.toUnicode().replace(findName, findName+varNoSpace)
        if new:
            #print('Changing name', namerecord.toUnicode(), 'to', new )
            f['name'].setName(new, namerecord.nameID, namerecord.platformID, namerecord.platEncID, namerecord.langID)
    
    #os.remove(path)
    basePath, fileName = os.path.split(path)
    newPath = os.path.join(basePath, fileName.replace(findName, findName+varNoSpace))
    f.save(newPath)