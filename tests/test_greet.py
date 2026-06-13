"""Basic tests for the greet module."""

from greet import greet


def test_greets_a_name():
    assert greet("World") == "Hello, World!"


def test_strips_surrounding_whitespace():
    assert greet("  Ada  ") == "Hello, Ada!"


def test_empty_name_falls_back_to_friend():
    assert greet("") == "Hello, friend!"
    assert greet("   ") == "Hello, friend!"
