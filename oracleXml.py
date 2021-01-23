#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Parse xml STIG-SCAP Format
# xml file is user input
# Modular:
# Editable by user config files
# Program creates reference files for security script check

import xml.etree.ElementTree as ET
import sys,re,os,codecs
from xcVariables import *
#from mVariables import *
from FUNCTIONS import *
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    print "\nThis program parses xml pages. Disable program with CTRL-C. Lets begin.\n"
    PATH=getPath()
    ROOT=getRoot(PATH)
    groupIDList = removeDelimiters(displayElementsWithAttrib(ROOT,groupIdTAG),rID)
    groupTitleList = groupTitles(displayElementsWithText(ROOT, allTitles))
    ruleIdLst = removeDelimiters(ruleIDList(displayElementsWithAttrib(ROOT,allRules),rID),rID)
    severityLst = convertCAT(removeDelimiters(severityList(displayElementsWithAttrib(ROOT, allRules)),severe))
    ruleVersionList = displayElementsWithText(ROOT, version)
    ruleVersionList.pop(0)
    ruleTitlesList = ruleTitles(displayElementsWithText(ROOT, allTitles))
    ruleTitlesList.pop(0)
    ### vulnDisc contains \u201c---\u201d encoding
    vulnDisc = removeDelimiters(tagSelection(displayElementsWithText(ROOT,description),vuld),tags)
    ## iaControls NEEDS TUNING
    iaControls = iaControl(splitItem(removeDelimiters(tagSelection(displayElementsWithText(ROOT,description),vuld),tags)))
    chkContent = displayElementsWithText(ROOT, checkContent)
    ### chkContent contains \u201c---\u201d encoding
    fxTxt = displayElementsWithText(ROOT, fixText)
    ### fxTt contains \u201c---\u201d formatting
    cci = displayElementsWithText(ROOT, CCI)

    new_directory = raw_input("\nName the new folder to contain new files: ")
    os.makedirs(new_directory)

    for gi, gt, ri, s, rv, rt, vd, cc, ft, cci in zip(groupIDList,
            groupTitleList, ruleIdLst, severityLst, ruleVersionList,
            ruleTitlesList, vulnDisc, chkContent, fxTxt, cci):
        file_O = open(os.path.join(new_directory,gi), "w")
        file_O.write('vulid='+'"'+gi+'"')
        file_O.write('\nGROUP_TITLE='+'"'+gt+'"')
        file_O.write('\nRULE_ID='+'"'+ri+'"')
        file_O.write('\nSEVERITY='+'"'+s+'"')
        file_O.write('\nRULE_VERSION='+'"'+rv+'"')
        file_O.write('\nRULE_TITLE='+'"'+rt+'"')
        file_O.write('\n\n\nVULNERABILITY_DISCUSSION='+'"'+vd+'"')
        file_O.write('\n\n\nCHECK_CONTENT='+'"'+cc+'"')
        file_O.write('\n\n\nFIX_TEXT='+'"'+ft+'"')
        file_O.write('\n\nCCI='+'"'+cci+'"')
        file_O.close()

            
    print "\nProgram Complete. Check your new directory and files for accuracy.\n"
if __name__ == "__main__":
    sys.exit(main())
# main() end


