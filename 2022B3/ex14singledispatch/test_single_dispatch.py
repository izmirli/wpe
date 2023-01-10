import pytest
from solution import mysum


@pytest.mark.parametrize('nums, output', [
    ([], 0),
    ([10, 20, 30], 60),
    ((10, 20, 30), 60),
    ({10, 20, 30, 40}, 100)
])
def test_list(nums, output):
    assert mysum(nums) == output


@pytest.mark.parametrize('nums, output', [
    ({}, 0),
    ({'a': 1, 'b': 2, 'c': 3}, 6)
])
def test_dict(nums, output):
    assert mysum(nums) == output


@pytest.mark.parametrize('nums, output', [
    ('', 0),
    ('abcd', 0),
    ('a1b2c3', 6)
])
def test_string(nums, output):
    assert mysum(nums) == output
