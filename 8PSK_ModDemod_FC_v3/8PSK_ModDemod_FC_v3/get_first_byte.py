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

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Print First',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.float32]
        )
        self.first=0
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        

    def work(self, input_items,output_items):
        for i in range(0,len(input_items[0])):
            if self.first == 0:
                self.first=input_items[0][0]
            output_items[0][i]=float(self.first)
        return len(output_items[0])
        
