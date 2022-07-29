# See LICENSE.vyoma for details
import random


#from mux_model import mux_model
import cocotb
from cocotb.triggers import Timer

def mux_model(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17, inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,inp27, inp28, inp29, inp30):
  if sel == 0:
    y = inp0
  elif sel == 1:
      y = inp1
  elif sel == 2:
    y = inp2
  elif sel == 3:
    y = inp3
  elif sel == 4:
    y = inp4
  elif sel == 5:
    y = inp5
  elif sel == 6:
    y = inp6
  elif sel == 7:
    y = inp7
  elif sel == 8:
    y = inp8
  elif sel == 9:
    y= inp9
  elif sel == 10:
    y = inp10
  elif sel == 11:
    y = inp11
  elif sel == 12:
    y = inp12
  elif sel == 13:
    y = inp13
  elif sel == 14:
    y = inp14
  elif sel == 15:
    y = inp15
  elif sel == 16:
    y = inp16
  elif sel == 17:
    y = inp17
  elif sel == 18:
    y = inp18
  elif sel == 19:
    y = inp19
  elif sel == 20:
    y = inp20
  elif sel == 21:
    y = inp21
  elif sel == 22:
    y = inp22
  elif sel == 23:
    y = inp23
  elif sel == 24:
    y = inp24
  elif sel == 25:
    y = inp25
  elif sel == 26:
    y = inp26
  elif sel == 27:
    y = inp27
  elif sel == 28:
    y = inp28
  elif sel == 29:
    y = inp29
  else:
    y = 0
  return y

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    for i in range(32):

        
        inp0=random.randint(0, 3)
        inp1=random.randint(0, 3)
        inp2=random.randint(0, 3)
        inp3=random.randint(0, 3)
        inp4=random.randint(0, 3)
        inp5=random.randint(0, 3)
        inp6=random.randint(0, 3)
        inp7=random.randint(0, 3)
        inp8=random.randint(0, 3)
        inp9=random.randint(0, 3)
        inp10=random.randint(0, 3)
        inp11=random.randint(0, 3)
        inp12=random.randint(0, 3)
        inp13=random.randint(0, 3)
        inp14=random.randint(0, 3)
        inp15=random.randint(0, 3)
        inp16=random.randint(0, 3)
        inp17=random.randint(0, 3)
        inp18=random.randint(0, 3)
        inp19=random.randint(0, 3)
        inp20=random.randint(0, 3)
        inp21=random.randint(0, 3)
        inp22=random.randint(0, 3)
        inp23=random.randint(0, 3)
        inp24=random.randint(0, 3)
        inp25=random.randint(0, 3)
        inp26=random.randint(0, 3)
        inp27=random.randint(0, 3)
        inp28=random.randint(0, 3)
        inp29=random.randint(0, 3)
        inp30=random.randint(0, 3)
        sel=random.randint(0, 31)
        
        dut.inp0.value=inp0
        dut.inp1.value=inp1
        dut.inp2.value=inp2
        dut.inp3.value=inp3
        dut.inp4.value=inp4
        dut.inp5.value=inp5
        dut.inp6.value=inp6
        dut.inp7.value=inp7
        dut.inp8.value=inp8
        dut.inp9.value=inp9
        dut.inp10.value=inp10
        dut.inp11.value=inp11
        dut.inp12.value=inp12
        dut.inp13.value=inp13
        dut.inp14.value=inp14
        dut.inp15.value=inp15
        dut.inp16.value=inp16
        dut.inp17.value=inp17
        dut.inp18.value=inp18
        dut.inp19.value=inp19
        dut.inp20.value=inp20
        dut.inp21.value=inp21
        dut.inp22.value=inp22
        dut.inp23.value=inp23
        dut.inp24.value=inp24
        dut.inp25.value=inp25
        dut.inp26.value=inp26
        dut.inp27.value=inp27
        dut.inp28.value=inp28
        dut.inp29.value=inp29
        dut.inp30.value=inp30

        dut.sel.value=sel
       
        await Timer(2, units="ns")

        
        
        #if(dut.out.value == mux_model(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,inp27, inp28, inp29, inp30)):
        #    print("success")
        #else:
        #    print("Fail")
        #"Randomised test failed with:"

        assert (dut.out.value == mux_model(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,inp27, inp28, inp29, inp30)), "Randomised test failed"
