"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self,repeat=5):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Repeat First Byte',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        self.sync=0
        self.repeat=repeat
        self.repeated=0
        self.first=0
#        self.loose=[]
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def work(self, input_items, output_items):
 #       for i in range(0,len(input_items[0])):
 #           output_items[0][i] = input_items[0][i]
 #           if input_items[0][i] == 255 and output_items[0][i-1] == 255 and output_items[0][i-2] == 255:
 #               output_items[0][i] = 1
 #           if input_items[0][i] == 0 and output_items[0][i-1] == 0 and output_items[0][i-2] == 0:
 #               output_items[0][i] = 254
        self.sync=output_items[0][0]=input_items[0][0]
        for i in range(0,len(input_items[0])):
            if self.repeated<self.repeat:
                output_items[0][i]=self.sync
                self.repeated+=1
            else:
                output_items[0][i]=input_items[0][i-self.repeated*self.first]
#        Si algun dia quiero que no se pierdan esos bits
#        if self.first == 1:
#            for j in range(i+1,i+1+self.repeated):
#                self.loose.append(input_items[0][j-self.repeated])
        self.first=0
        return len(output_items[0])
