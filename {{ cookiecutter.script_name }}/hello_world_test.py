from hello_world import greet


def test_greet():
    result = greet("world")
    assert result == "Hello, world!"
