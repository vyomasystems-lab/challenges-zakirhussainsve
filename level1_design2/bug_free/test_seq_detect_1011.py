# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await RisingEdge(dut.clk)   
    dut.reset.value = 0
    await RisingEdge(dut.clk) 

    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await RisingEdge(dut.clk) 
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk) 
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk) 
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk) 

    await RisingEdge(dut.clk) 

    #if(dut.current_state.value==dut.SEQ_1011.value):
    #   print("pass")
    #else:
    #    print("fail")

    assert dut.current_state.value==dut.SEQ_1011.value, "Randomised test failed"
    
