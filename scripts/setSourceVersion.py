manual = """
Sets version number in Ubuntu font sources and redraws uniEFFD accordingly.

USAGE:
- Set version explicitly (expects 0.000 format):
    $ python setSourceVersion.py 0.000
- Find existing version number of Ubuntu-Light.ufo, bump by 1
    $ python setSourceVersion.py bump
- Find existing version number of Ubuntu-Light.ufo, bump by a certain amount
    $ python setSourceVersion.py bump 10
"""

import sys
import os
from fontParts.world import OpenFont

basePath = os.path.split(os.path.split(__file__)[0])[0]
sourcesPath = os.path.join(basePath, 'sources')

# this is the glyph we will overwrite with the version number
versionGlyphName = 'uniEFFD'

# get glyph names we will use to compose the version glyph
glyphMap = {
'.': 'period',
'0': 'zeroinferior',
'1': 'oneinferior',
'2': 'twoinferior',
'3': 'threeinferior',
'4': 'fourinferior',
'5': 'fiveinferior',
'6': 'sixinferior',
'7': 'seveninferior',
'8': 'eightinferior',
'9': 'nineinferior',
}

if len(sys.argv) < 2 or sys.argv[1] in ['help', '-h']:
    # if nothing, print the manual
    print(manual)

elif sys.argv[1] == 'bump':
    # bump an existing version number
    # get the version number from Ubuntu-Light and use it for all fonts
    try:
        bumpAmount = sys.argv[2]
    except:
        bumpAmount = 1
    f = OpenFont(os.path.join(basePath,'sources/Ubuntu-Light.ufo'))
    print('Version from Ubuntu-Light.ufo: ', f.info.versionMajor, f.info.versionMinor)
    versionString = str(f.info.versionMajor) + '.' + str(f.info.versionMinor + bumpAmount)
    print(versionString)
    f.close()

else:
    # set version number explicitly
    versionString = sys.argv[1]

# parse version number into versionMajor and versionMinor
versionMajor, versionMinor = versionString.split('.')
versionMajor = int(versionMajor)
versionMinor = int(versionMinor)

# replace version info in all UFOs
# NOTE: will only replace versionMajor and versionMinor
# assumes other fontInfo fields are empty

for fileName in os.listdir(sourcesPath):
    filePath = os.path.join(sourcesPath, fileName)
    if filePath.endswith('.ufo'):
        f = OpenFont(filePath)
        print('Updating version number and', versionGlyphName, 'in', fileName)
        # reset font info
        f.info.versionMajor = versionMajor
        f.info.versionMinor = versionMinor
        
        versionGlyph = f[versionGlyphName]
        # clear version glyph
        versionGlyph.clearComponents()
        versionGlyph.clearContours()
        # add new version as components
        xOffset = 0
        for versionChar in versionString:
            versionCharGlyphName = glyphMap[versionChar]
            versionCharGlyphWidth = f[versionCharGlyphName].width
            versionGlyph.appendComponent(versionCharGlyphName, offset=(xOffset, 0))
            xOffset += versionCharGlyphWidth
        # set version glyph width
        versionGlyph.width = xOffset
        # save
        f.save()
        f.close()
print('done')