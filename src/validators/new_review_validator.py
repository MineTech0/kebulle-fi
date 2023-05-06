from src.validators.base_validator import BaseValidator


class NewReviewValidator(BaseValidator):
    def validate(self, form):
        self.errors = []
        if not self.notEmpty(form['comment']):
            self.errors.append('Kommentti ei saa olla tyhjä')
        if not self.notEmpty(form['user_name']):
            self.errors.append('Nimi ei saa olla tyhjä')
        if not self.inRange(form['sauce_rating'], 1, 10):
            self.errors.append('Kastikearvosana ei ole sallitulla välillä')
        if not self.inRange(form['meat_rating'], 1, 10):
            self.errors.append('Liha-arvosana ei ole sallitulla välillä')
        if not self.inRange(form['service_rating'], 1, 10):
            self.errors.append('Palvelu-arvosana ei ole sallitulla välillä')
        if not self.inRange(form['price_rating'], 1, 10):
            self.errors.append('Hinta-arvosana ei ole sallitulla välillä')
        if not self.inRange(form['cleanliness_rating'], 1, 10):
            self.errors.append('Siisteys-arvosana ei ole sallitulla välillä')
        if not self.inRange(form['sides_rating'], 1, 10):
            self.errors.append('Lisuke-arvosana ei ole sallitulla välillä')
        if not self.inRange(form['fries_rating'], 1, 10):
            self.errors.append(
                'Ranskalaisten arvosana ei ole sallitulla välillä')
        if not self.isBoolean(form['vegan_options']):
            self.errors.append('Vegaanivaihtoehtoja ei ole valittu')

        return len(self.errors) == 0


new_review_validator = NewReviewValidator()
