class DiscountCalculator:
    """Калькулятор скидок"""

    def apply_discount(self, price, discount):
        """Применяет скидку к цене"""
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if not (0 <= discount <= 100):
            raise ValueError("Скидка должна быть от 0 до 100")

        return price * (1 - discount / 100)