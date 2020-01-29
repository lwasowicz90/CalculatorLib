import calculator


class TestCalculator:
    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 2 == calculator.substract(4, 2)

    def test_multi(self):
        100 == calculator.multi(10, 10)
