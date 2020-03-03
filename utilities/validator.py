import re
def SpecialChars(stringpassed):
    out=re.findall('[^A-Za-z0-9]',stringpassed)
    if(len(out)==0):
        return False
    else:
        return True
