from src.validators.base_validator import BaseValidator


class NewRestaurantValidator(BaseValidator):
    def validate(self, form):
        self.errors = []
        if not self.notEmpty(form['name']):
            self.errors.append('Nimi ei saa olla tyhjä')
        if not self.notEmpty(form['address']):
            self.errors.append('Osoite ei saa olla tyhjä')
        if not self.notEmpty(form['city_id']):
            self.errors.append('Kaupunki ei saa olla tyhjä')

        return len(self.errors) == 0
new_restaurant_validator = NewRestaurantValidator()