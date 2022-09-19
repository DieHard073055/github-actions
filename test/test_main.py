from main import add, sub

def test_add():
    result = add(10, 10)
    assert result.unwrap() == 20

def test_sub():
    result = sub(20, 10)
    assert result.unwrap() == 10
