import pytest

from elections import elections

print("HEEEEEEEEERE")

@pytest.fixture
def client():
    elections.app.config['TESTING'] = True
    client = elections.app.test_client()

    yield client
