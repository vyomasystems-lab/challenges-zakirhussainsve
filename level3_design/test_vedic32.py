# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

# Sample Test
@cocotb.test()
def run_test(dut):

    
    # input transaction
    for i in range(255):
        a = random.randint(0, 255)
        #0x5
        b = random.randint(0, 255)
        #0x0
        
    # driving the input transaction
        dut.a.value = a
        dut.b.value = b
        
  
        yield Timer(1) 

    # obtaining the output
        dut_output = dut.c.value

        
    # comparison
        error_message = f'does not match MODEL'
        assert dut_output == a*b, error_message

    #//0x101010B3

    
