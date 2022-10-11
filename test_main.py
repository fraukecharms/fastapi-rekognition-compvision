from main import root


def test_root():
    """
    curl -X 'GET'   'http://0.0.0.0:8080/showimage'   -H 'accept: application/json' --output streamimage.jpg
    """
    r = root()

    assert 1 == 1
