from main import add

def test_add():
    result = add(10, 10)
    assert result.unwrap() == 20
