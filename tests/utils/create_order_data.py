from faker import Faker


faker_obj = Faker(locale='ru_RU')


def create_order_data():
    """создание данных для заказа"""
    return {
        'firstName': faker_obj.first_name(),
        'lastName': faker_obj.last_name(),
        'address': faker_obj.address(),
        'metroStation': faker_obj.random_choices(elements=range(1, 60), length=1)[0],
        'phone': faker_obj.unique.numerify('+7 9## ### ## ##'),
        'rentTime': faker_obj.random_choices(elements=range(1, 8), length=1)[0],
        'deliveryDate': faker_obj.future_date().strftime('%Y-%m-%d'),
        'comment': faker_obj.text(),
        'color': [
            'BLACK'
        ],
    }
