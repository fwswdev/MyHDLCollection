'''
Author: SevenString
Description:
    This is a MyHDL program that has two counter (fast and slow) that outputs
    square waves. The counter are being controlled by rising edge clock signal provided
    by a clock source (on my experiment, it is a 555 timer on astable mode).
    It is then fed into a 2 to 1 mux.

    This is tested working with XC2C128.
'''

from myhdl import *


##-#------------------------######----------------------------#-----#---------------
##-#-------######-#####-----#-----#-#------#-#----#-#----#----##---##-#----#-#----#-
##-#-------#------#----#----#-----#-#------#-##---#-#---#-----#-#-#-#-#----#--#--#--
##-#-------#####--#----#----######--#------#-#-#--#-####------#--#--#-#----#---##---
##-#-------#------#----#----#-----#-#------#-#--#-#-#--#------#-----#-#----#---##---
##-#-------#------#----#----#-----#-#------#-#---##-#---#-----#-----#-#----#--#--#--
##-#######-######-#####-----######--######-#-#----#-#----#----#-----#--####--#----#-
##----------------------------------------------------------------------------------



def LedBlink(intMaxCount,clk,ledPin):
    @instance
    def logicled():
        count = 0
        ledStatus = False

        while True:
            yield clk.posedge
            count += 1
            if(count>intMaxCount):
                count = 0
                if(ledStatus):
                    ledPin.next = True
                else:
                    ledPin.next= False
                ledStatus = not ledStatus

    return logicled

def Mux2To1(sel,outpn,muxslow,muxfast):
    @always_comb
    def logic_mux():
        if(sel):
            outpn.next = muxslow
        else:
            outpn.next = muxfast
    return logic_mux



def muxclkdesign(clk,sel,outpn):

    # define the Signals inside
    muxslow = Signal(False)
    muxfast = Signal(False)

    instMux = Mux2To1(sel,outpn,muxslow,muxfast)
    instledBlinkFast = LedBlink(50,clk,muxfast)
    instledBlinkSlow = LedBlink(500,clk,muxslow)

    return instMux,instledBlinkFast,instledBlinkSlow



def convert():
    clk,sel,outpn = [Signal(False) for i in range(3)]
    toVHDL(muxclkdesign, clk,sel,outpn)



if __name__ == '__main__':
    convert()
    print "OK!"