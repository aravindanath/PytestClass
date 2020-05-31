
import pytest

@pytest.mark.run(order=1)
def test_three():
    assert True
    
@pytest.mark.run(order=4)
@pytest.mark.dependency(depends=["test_two"])    
def test_four():
    assert True
    
@pytest.mark.run(order=3)      
def test_two():
    assert False
    
@pytest.mark.run(order=2)      
def test_one():
    assert True