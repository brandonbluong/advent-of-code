"""Test file for Day 1: Sonar Sweep"""
import pathlib
import pytest
import aoc202101 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture(name="example_1")
def example1():
    """Parses example1"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture(name="example_2")
def example2():
    """Parses a sliding window function of example1"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_window_fn(aoc.parse(puzzle_input))


def test_parse_example1(example_1):
    """Test that input is parsed properly"""
    assert example_1 == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1_example1(example_1):
    """Test part 1 on example input"""
    assert aoc.part1(example_1) == 7


def test_parse_example2(example_2):
    """Test that input is parsed properly using window function"""
    assert example_2 == [607, 618, 618, 617, 647, 716, 769, 792]


def test_part2_example2(example_2):
    """Test part 2 on example input"""
    assert aoc.part2(example_2) == 5
