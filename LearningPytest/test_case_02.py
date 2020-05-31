import pytest

@pytest.mark.Accounts
def test_case_01():
    print("Hello my first test on accounts")

@pytest.mark.Regression
def test_case_02():
    print("Hello my first test")

@pytest.mark.Smoke
def test_case_03():
    print("Hello my first test")
    assert 10==3

@pytest.mark.Regression
@pytest.mark.Smoke
@pytest.mark.Accounts
def test_case_04():
    print("Hello my fourth test on accounts")
