import pytest
def sum(a,b):
    return a+b

def return_param():
    return 7, 8, 15

@pytest.mark.parametrize("input1,input2,output",           
                        [(6,4,10),
                          (4,6,10),
                          (3,2,5),
                          return_param()])
def test_calc_1(input1,input2,output):
    result =sum(input1,input2)
    assert result == output