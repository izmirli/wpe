import pytest
from solution import ImmutableParent, ImmutableMeansImmutableError


@pytest.fixture
def immutable_value():
    class ImmutableMe(ImmutableParent):
        pass

    im = ImmutableMe(x=111, y=222, z=[10, 20, 30])
    return im


def test_attributes_are_set(immutable_value):
    assert vars(immutable_value) == {'x': 111, 'y': 222, 'z': [10, 20, 30]}


def test_cannot_change_existing_attribute(immutable_value):
    with pytest.raises(ImmutableMeansImmutableError) as e:
        immutable_value.x = 999
        assert 'Cannot set x' in e


def test_can_change_element_in_attribute(immutable_value):
    immutable_value.z.append(40)
    assert vars(immutable_value) == {'x': 111, 'y': 222, 'z': [10, 20, 30, 40]}


def test_cannot_add_new_attribute(immutable_value):
    with pytest.raises(ImmutableMeansImmutableError) as e:
        immutable_value.a = 'Hello'
        assert 'Cannot set a' in e

    assert vars(immutable_value) == {'x': 111, 'y': 222, 'z': [10, 20, 30]}
