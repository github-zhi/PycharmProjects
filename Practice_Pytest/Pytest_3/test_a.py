import pytest

@pytest.fixture()

def login():
    username = 'Tom'
    return username

class TestDemo:

    def test_a(self, login):
        print(f"AA   username = {login}")

    def test_b(self, login):
        print(f"BB   username = {login}")

    def test_c(self):
        print(f"cc   username = {login}")