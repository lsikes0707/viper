#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Test elements of new xml
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is used to test out the functions of the viper program
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import xml.etree.ElementTree as ET
import subprocess as sp
import sys,re,os,codecs
from xcVariables import *
from FUNCTIONS import *
from test import *
reload(sys)
sys.setdefaultencoding('utf8')

def main():
#    print "This program supplies all of the tag elements to be able to parse the xml.\n"
    PATH = getPath()
#    print PATH
#    print "\nThis is from the getRoot(PATH) function\n"
    ROOT = getRoot(PATH)
#    print ROOT
#    print "\nHere are the \n"
#    viewTags(PATH)
  #  print 'Group Ids: '
#    vulids = removeDelimiters(displayElementsWithAttrib(ROOT, groupIdTAG),rID)
#    print vulids
#    print "Group Titles: "
#    print len(groupTitles(displayElementsWithText(ROOT, allTitles)))
#    print "Rule Ids: "
#    print len(removeDelimiters(ruleIDList(displayElementsWithAttrib(ROOT,allRules),rID),    rID))
#    print "CAT Severities: "
#    print severityList(displayElementsWithAttrib(ROOT, allRules))
#    print len(convertCAT(removeDelimiters(severityList(displayElementsWithAttrib(ROOT,     allRules)),severe)))
#    print "Rule Version: "
#    print len(displayElementsWithText(ROOT, version))
#    print "Rule Titles: "
#    print len(ruleTitles(displayElementsWithText(ROOT, allTitles)))
##    print ruleTitles(displayElementsWithText(ROOT, allTitles))
#    print "Vuln Disc: "
    vuldi = removeDelimiters(removeDelimiters(tagSelection(displayElementsWithText(ROOT, description), vuld),tags,mt),quo,quoa)
    print vuldi 
#    vuldi = ['ca"ts', 'dogs', 'birds']
#    for i in vuldi:
#        print sp.call(["sed", 's|\"||g', i])
#        for j in var:
#            sp.call(["/usr/bin/echo", j])
        
 
#    for disc in vuldi:
#        sp.call("sed 's|\"|\\\"|g' disc")
#        print "vuldiscussion"
#        print disc
        #newDisc = re.sub('"', '\\"',disc)
        #vuldi = newList.append(newDisc)
#    vuldi = displayElementsWithText(ROOT, description)
    #print vuldi
#    print len(removeDelimiter(splitItem(tagSelection(displayElementsWithText(ROOT,description),iaControl),tags),'false')
#    descriptions = splitItem(removeDelimiters(tagSelection(displayElementsWithText(ROOT,description),vuld),tags))
#    descriptions = removeDelimiters(displayElementsWithText(ROOT, description),tags)
#    print "IA Controls: "
#    print "NEED FUNCTION FOR DESCRIPTION TAG PARSE"
#    print "Check Content: "
#    print len(displayElementsWithText(ROOT, checkContent))
#    print "Fix Text: "
#    print len(displayElementsWithText(ROOT, fixText))
#    print "CCI: "i
#    print displayElementsWithText(ROOT, CCI)
#    print len(displayElementsWithText(ROOT, CCI))
#    print displayElementsWithText(ROOT, CCI)
#
## print all tag names, their attributes, and text
#    ELEMENT = description 
#    for e in ROOT.iter():
#        rATTRIB = str(e.attrib)
#        if e.tag == ELEMENT:
#            print "Element Tag Name: "
#            print e.tag
#            print "Element Attribute Data: "
#            print e.attrib
#            print "Element Text Data: "
#            print e.text
#    for ids, desc in zip(vulids, descriptions):
#        print "VULID="+'"'+str(ids)+'"'
#        print "DESCRIPTION"+'"'+str(desc)+'"'
##    new_directory = raw_input("\nName the new folder containing test files: ")
##    os.makedirs(new_directory)
### for loop options for zip:
#   gi  vulids
#   gt  group title
#   ri  rule id
#   s   severity
#   rv  rule version
#   rt  rule title
#   vd  vuln discussion
#   cc  check content
#   ft  fix text
#   cci as is
##    for vi, vd, cci in zip(vulids, vuldi, Cci):
##        file_O = open(os.path.join(new_directory,vi), "w")
##        file_O.write('vulid='+'"'+vi+'"')
#        file_O.write('\nGROUP_TITLE='+'"'+gt+'"')
#        file_O.write('\nRULE_ID='+'"'+ri+'"')
#        file_O.write('\nSEVERITY='+'"'+s+'"')
#        file_O.write('\nRULE_VERSION='+'"'+rv+'"')
#        file_O.write('\nRULE_TITLE='+'"'+rt+'"')
##        file_O.write('\n\n\nVULNERABILITY_DISCUSSION='+'"'+vd+'"')
#        file_O.write('\n\n\nCHECK_CONTENT='+'"'+cc+'"')
#        file_O.write('\n\n\nFIX_TEXT='+'"'+ft+'"')
#        file_O.write('\n\nCCI='+'"'+cci+'"')
##        file_O.close()



if __name__ == "__main__":
    sys.exit(main())
