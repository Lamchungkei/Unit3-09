# Created by: Kay Lin
# Created on: 24th-Oct-2017
# Created for: ICS3U
# this is a unicode program that prints lower case and upper case letters.

for outerCounter in range(65,91):
    for interCounter in range(97, 123):
        unicode = unichr(interCounter)
        upper_unicode = unichr(outerCounter)
        print (str(upper_unicode) + '->' + str(unicode))
    

