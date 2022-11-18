# Add version number to the name, for easily installation of multiple versions
# addVersionToNames.py /path/to/Font1.otf /path/to/Font2.otf

from fontTools.ttLib import TTFont
import sys
import os

def getFiles(path, extensions):
    return [os.sep.join((dir, file)) for (dir, dirs, files)
            in os.walk(path) for file in files if
            file.split(".")[-1] in extensions]


def get_name_record(ttFont, nameID, fallbackID=None, platform=(3, 1, 0x409)):
    name = ttFont["name"]
    record = name.getName(nameID, 3, 1, 0x409)
    if not record and fallbackID:
        record = name.getName(fallbackID, 3, 1, 0x409)
    if not record:
        raise ValueError(f"Cannot find record with nameID {nameID}")
    return record.toUnicode()

paths = getFiles(sys.argv[1], ['ttf'])

for path in paths:
    path = path.strip('\"')
    print(path)
    f = TTFont(path)


    familyName = get_name_record(f, 16, fallbackID=1)
    psFamilyName = familyName.replace(" ", "")
    print('find', familyName)
    versionName = get_name_record(f, 3, fallbackID=1)
    versionNumber = versionName.split(';')[0]

    new_familyName = f'{familyName} Beta {versionNumber}'
    new_psFamilyName = new_familyName.replace(" ", "")
    
    oldNames = [familyName, psFamilyName]
    newNames = [new_familyName, new_psFamilyName]

    for record in f['name'].names:
        record_text = record.toUnicode()

        isMatch = False
        for string in oldNames:
            if string in record_text:
                isMatch = string
                break
        
        if isMatch != False:

            if record.nameID not in [1, 4, 7, 16]:
                record_newtext = record_text.replace(isMatch, newNames[1])
            else:
                record_newtext = record_text.replace(isMatch, newNames[0])

            f['name'].setName(
                record_newtext,
                record.nameID,
                record.platformID,
                record.platEncID,
                record.langID
            )
            
    
    #os.remove(path)
    basePath, fileName = os.path.split(path)

    newFilename = fileName.replace(psFamilyName, new_psFamilyName)
    
    newPath = os.path.join(basePath, newFilename)

    f.save(newPath)