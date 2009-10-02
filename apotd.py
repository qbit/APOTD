#!/usr/bin/env python

import urllib2
import re
from appscript import app, mactypes

#####################config###########################

img_dir = "/Users/abieber/Pictures/"

######################################################

url = "http://antwrp.gsfc.nasa.gov/apod/astropix.html"
short_url = "http://antwrp.gsfc.nasa.gov/apod/"

html =  urllib2.urlopen( url )

tmp = re.search( '(?<=SRC=[\"\'])([^\"\']+)', html.read() )
image_path = tmp.group(0)

tmp = re.search( '(\w+\.jpg|png|gif+)', image_path )
image_name = tmp.group(0)

new_url = short_url + image_path

FILE = open( img_dir + image_name, "w" )
FILE.writelines( urllib2.urlopen( new_url ) )
FILE.close()

app('Finder').desktop_picture.set(mactypes.File( img_dir + image_name ))
