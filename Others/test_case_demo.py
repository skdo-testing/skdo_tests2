import pytest

@pytest.fixture()
def setUp():
    print("I will run one before every test")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")
