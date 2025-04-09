import pytest


@pytest.fixture()
def set_up():
    print("Start Test")
    yield
    print("Finish Test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter scope tests")
    yield
    print("Exit scope tests")
