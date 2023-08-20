from seasons import minutes
import pytest

def test_minutes():
    assert minutes("2022-07-12")==525600
    assert minutes("2023-07-10")==2880
