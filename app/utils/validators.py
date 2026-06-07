from datetime import datetime


def validate_amount(amount):

    try:
        amount = float(amount)

        if amount <= 0:
            return None

        return amount

    except ValueError:
        return None


def validate_date(date_string):

    try:
        datetime.strptime(
            date_string,
            "%Y-%m-%d"
        )
        return True

    except ValueError:
        return False