from calculations import numbers_sum

def test_numbers_sum():
    assert numbers_sum(2, 3) == 5
    return "Testing numbers_sum successful"

print test_numbers_sum()

from geogame import check_guess


def test_check_guess():
    assert check_guess("Ljubljana", "Slovenia", {"Slovenia": "Ljubljana"}) == True
    return "test_check_guess() passed successfully."

print test_check_guess()