from main import greet, greet_many


def test_greet_returns_personalized_greeting():
    assert greet("Python") == "Hello, Python!"


def test_greet_many_returns_greetings_in_input_order():
    assert greet_many(["Git", "Python", "Codex"]) == [
        "Hello, Git!",
        "Hello, Python!",
        "Hello, Codex!",
    ]
