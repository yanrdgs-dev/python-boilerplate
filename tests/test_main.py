from template_package.main import sum

def test_sum_positive_numbers():
    """Tests the sum of two positive integers."""
    assert sum(2, 3) == 5