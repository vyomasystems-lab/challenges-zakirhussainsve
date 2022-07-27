# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    for i in range(5):

        dut.inp0.value=random.randint(0, 4)
        dut.inp1.value=random.randint(0, 4)
        dut.inp2.value=random.randint(0, 4)
        dut.inp3.value=random.randint(0, 4)
        dut.inp4.value=random.randint(0, 4)
        dut.inp5.value=random.randint(0, 4)
        dut.inp6.value=random.randint(0, 4)
        dut.inp7.value=random.randint(0, 4)
        dut.inp8.value=random.randint(0, 4)
        dut.inp9.value=random.randint(0, 4)
        dut.inp10.value=random.randint(0, 4)
        dut.inp11.value=random.randint(0, 4)
        dut.inp12.value=random.randint(0, 4)
        dut.inp13.value=random.randint(0, 4)
        dut.inp14.value=random.randint(0, 4)
        dut.inp15.value=random.randint(0, 4)
        dut.inp16.value=random.randint(0, 4)
        dut.inp17.value=random.randint(0, 4)
        dut.inp18.value=random.randint(0, 4)
        dut.inp19.value=random.randint(0, 4)
        dut.inp20.value=random.randint(0, 4)
        dut.inp21.value=random.randint(0, 4)
        dut.inp22.value=random.randint(0, 4)
        dut.inp23.value=random.randint(0, 4)
        dut.inp24.value=random.randint(0, 4)
        dut.inp25.value=random.randint(0, 4)
        dut.inp26.value=random.randint(0, 4)
        dut.inp27.value=random.randint(0, 4)
        dut.inp28.value=random.randint(0, 4)
        dut.inp29.value=random.randint(0, 4)
        dut.inp30.value=random.randint(0, 4)

        dut.sel.value=random.randint(0, 40)
       

        await Timer(2, units="ns")

        assert dut.out.value == mux_model(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,
           inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,inp27, inp28, inp29, inp30
        ), "Randomised test failed with:"
