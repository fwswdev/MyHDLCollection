'''
Author: SevenString
Description:
    This is a MyHDL program that contains mux and demux. They both share
    a group of select pins. User can change the number of mux and demux
    by just simply changing the BIT_WIDTH constant.

    This is tested working with XC2C128.
'''

from myhdl import *
import operator


##-#######-------------------------#-----#---------------
##-#-------#------######-#----#----##---##-#----#-#----#-
##-#-------#------#-------#--#-----#-#-#-#-#----#--#--#--
##-#####---#------#####----##------#--#--#-#----#---##---
##-#-------#------#--------##------#-----#-#----#---##---
##-#-------#------#-------#--#-----#-----#-#----#--#--#--
##-#-------######-######-#----#----#-----#--####--#----#-
##-------------------------------------------------------


def systemMuxDemux(outpn,sel,inp,bitwidth,indemux,outdemux):

    # mux
    @always_comb
    def logicmux():

        for x in range(0,2**bitwidth):
            if(sel==x):
                outpn.next = inp[x]

    @always_comb
    def logicdemux():

        for x in range(0,2**bitwidth):
            if(sel==x):
                outdemux[x].next = indemux
            else:
                outdemux[x].next = True


    return logicmux,logicdemux



def convert():


    BIT_WIDTH = 3 # just change this (3 is  2^3 = 8, then this is a 1 to 8 mux/8 to 1 demux)

    outpn = Signal(False)
    sel = Signal(intbv(0)[BIT_WIDTH:])
    inp = Signal(intbv(0)[ int(2**BIT_WIDTH):])

    indemux=Signal(False)
    outdemux=Signal(intbv(0)[ int(2**BIT_WIDTH):])

    toVHDL(systemMuxDemux,outpn,sel,inp,BIT_WIDTH,indemux,outdemux)





if __name__ == '__main__':
    convert()
    print "OK!"