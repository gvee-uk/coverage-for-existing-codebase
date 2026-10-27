from app import utils


def test_foo():
    expected = 1
    actual = utils.foo()
    assert expected == actual
