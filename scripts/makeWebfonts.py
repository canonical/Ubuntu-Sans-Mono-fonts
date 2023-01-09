import os
from fontTools import subset
from fontTools.ttLib import TTFont, woff2
from fontTools.ttx import makeOutputFileName


def getFiles(path, extensions):
    return [os.sep.join((dir, file)) for (dir, dirs, files)
            in os.walk(path) for file in files if
            file.split(".")[-1] in extensions]


def makeWOFF(fontPath, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    WOFF2_outputfile = makeOutputFileName(fontPath, outputDir=outputDir, extension='.woff2')
    woff2.compress(fontPath, WOFF2_outputfile)
    print(f"Saved WOFF2: {WOFF2_outputfile} ")
    # Woff 1 
    WOFF_outputfile = makeOutputFileName(fontPath, outputDir=outputDir, extension='.woff')
    ttFont = TTFont(fontPath)
    ttFont.save(WOFF_outputfile)
    print(f"Saved WOFF: {WOFF_outputfile}")

def unicodeRangeToList(unicodeRangeString):
    # remove "U+"" from ranges
    unicodeRangeString = unicodeRangeString.replace("U+", "").replace(" ", "")
    # create set
    unicodesSet = set()
    # split up separate ranges by commas
    for unicodeChunk in unicodeRangeString.split(","):
        # if it's a range...
        if "-" in unicodeChunk:
            # get start and end of range
            start, end = unicodeChunk.split("-")
            # go through range and add each value to the set
            for unicodeInteger in range(int(start,16), int(end,16)+1):
                unicodesSet.add(unicodeInteger)
        # if it's a single unicode...
        else:
            unicodesSet.add(int(unicodeChunk,16))
    return unicodesSet

def subsetFont(fontPath, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    UNICODERANGE_DATA = {
        "latin": "U+0000-00FF, U+0131, U+0152-0153, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2212, U+2215",
        "latin-extended": "U+0100-024F, U+1E00-1EFF, U+20A0-20AB, U+20AD-20CF, U+2C60-2C7F, U+A720-A7FF",
        "latin-minimal": "U+0000-00FF, U+0131, U+0152, U+0153, U+02BB, U+02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD",

        "cyrillic": "U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116",
        "cyrillic-extended": "U+0460-052F, U+20B4, U+2DE0-2DFF, U+A640-A69F",
        "greek": "U+0370-03FF",
        "greek-extended": "U+1F00-1FFF",
    }

    for charset in UNICODERANGE_DATA:
        # Create a list of chars to keep
        unicodesToKeep = [intUnicode for intUnicode in unicodeRangeToList(UNICODERANGE_DATA[charset])]
        # Get hex value from integer characters
        unicodesToKeep = [hex(n) for n in unicodesToKeep]
        # Join in a string for subsetter
        unicodesToKeep = ",".join(unicodesToKeep)
    
        # Subset
        outputPath = makeOutputFileName(fontPath, outputDir=outputDir, extension='.ttf', suffix="-"+charset)
        subset.main([fontPath, f'--unicodes={unicodesToKeep}',
                    "--name-IDs=*",
                    "--layout-features=*",
                    "--glyph-names",
                    '--notdef-outline',
                    f'--output-file={outputPath}'])
    
        makeWOFF(outputPath, outputDir)
        os.remove(outputPath)

fontsPath = 'fonts'
if __name__ == '__main__':
    ttfFonts = getFiles(fontsPath, ['ttf'])
    for fontPath in ttfFonts:
        # Make webfont for base font
        makeWOFF(fontPath, "fonts/webfont")
        
        # Make subsetted webfont 
        subsetFont(fontPath, "fonts/webfont-subsets")
        
