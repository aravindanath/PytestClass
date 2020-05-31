import pytest

@pytest.mark.Regression
def test_demo01():
    print("Demo pytest Regression")

@pytest.mark.Smoke
def test_demo01():
    print("Demo pytest smoke")