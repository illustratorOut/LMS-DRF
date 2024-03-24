from rest_framework.exceptions import ValidationError


class LinkVideoValidator:
    """ Проверка поля linl_course на вхождения данных link """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = 'https://www.youtube.com/'
        tmp_val = dict(value).get(self.field).lower()

        if link in tmp_val:
            return
        else:
            raise ValidationError('Cсылки на сторонний ресурс запрещены!')
