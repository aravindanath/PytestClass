import pytest



def test_case_001():
    print("Test one")

def test_case_002():
    print("Test two")

@pytest.mark.Accounts
@pytest.mark.Regression
def test_case_05():
    print("Hello my fith test on accounts in reg")
