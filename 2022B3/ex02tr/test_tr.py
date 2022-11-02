import pytest
from solution import tr


def test_empty_source():
    with pytest.raises(TypeError):
        noop_tr = tr('', 'abcd')


def test_empty_result():
    with pytest.raises(TypeError):
        noop_tr = tr('abcd', '')


def test_simple():
    a_to_b_tr = tr('a', 'b')
    assert callable(a_to_b_tr)
    assert a_to_b_tr('abcdabcd') == 'bbcdbbcd'


def test_2_to_1():
    ab_to_c_tr = tr('ab', 'c')
    assert ab_to_c_tr('abcdabcd') == 'cccdcccd'


def test_remove():
    ab_to_c_tr = tr('ab', 'x')
    assert ab_to_c_tr('abcdabcd') == 'xxcdxxcd'


def test_5_to_3():
    aeiou_to_xyz_tr = tr('aeiou', 'xyz')
    assert aeiou_to_xyz_tr('the quick brown fox jumps over the lazy dog') \
           == 'thy qzzck brzwn fzx jzmps zvyr thy lxzy dzg'
