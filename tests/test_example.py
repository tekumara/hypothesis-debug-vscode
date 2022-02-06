from hypothesis import given
from hypothesis import strategies as st

from statistics import mean


@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean(xs):
    print("test_mean")
    assert min(xs) <= mean(xs) <= max(xs)
