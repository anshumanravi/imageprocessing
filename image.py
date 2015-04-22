#!/usr/bin/env python

import sys
from PIL import Image
import webcolors


class imageProcesser:
    def __init__(self,imgurl):
        
        self.imgurl = imgurl
        


    def getColor(self):

        im = Image.open(self.imgurl)
        n, color =  max(im.getcolors(im.size[0]*im.size[1]));
        try:
            actual_name = webcolors.rgb_to_name(color)
        except ValueError:
            actual_name = None

        return actual_name



if __name__ == "__main__":
    if len(sys.argv) > 1:
           imgp = imageProcesser(sys.argv[1])
           print imgp.getColor()
