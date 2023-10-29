"""
The application for working with seasons.

TODO No leap year
"""


def validate_init(func):
    def wrapper(self, name, months):
        if not isinstance(name, str):
            raise ValueError("Name should be a string")
        if not isinstance(months, list):
            raise ValueError("Months should be a list")
        for month in months:
            if not isinstance(month, str):
                raise ValueError("Each month should be a string")
        return func(self, name, months)
    
    return wrapper


class Season:
    @validate_init
    def __init__(self, name, months):
        self.__name = name
        self.months = months
    
    def __str__(self):
        return self.__name
    
    def __iter__(self):
        return iter(self.months)
    
    @staticmethod
    def _date_generator(month):
        day_to_text = lambda x: '\t%u' % x
        if month == 'February':
            for day in range(1, 29):
                yield day_to_text(day)
        elif month in ['April', 'June', 'September', 'November']:
            for day in range(1, 31):
                yield day_to_text(day)
        else:
            for day in range(1, 32):
                yield day_to_text(day)
    
    def print_months(self):
        for month in self:
            print(month)
            dates = list(self._date_generator(month))
            for i in range(0, len(dates), 28):
                week = dates[i:i + 28]
                for j in range(0, len(week), 7):
                    print(" ".join(week[j:j + 7]))


class Winter(Season):
    def __init__(self):
        super().__init__("Winter", ['December', 'January', 'February'])


class Spring(Season):
    def __init__(self):
        super().__init__("Spring", ['March', 'April', 'May'])


class Summer(Season):
    def __init__(self):
        super().__init__("Summer", ['June', 'July', 'August'])
    
    def __iter__(self):
        return iter(map(str.upper, self.months))


class Autumn(Season):
    def __init__(self):
        super().__init__("Autumn", ['September', 'October', 'November'])


try:
    season = input("Enter a season (winter, spring, summer, autumn): ")
    if not season.isalpha():
        raise ValueError("Season should be a string")
    
    if season.lower() == "winter":
        s = Winter()
    elif season.lower() == "spring":
        s = Spring()
    elif season.lower() == "summer":
        s = Summer()
    elif season.lower() == "autumn":
        s = Autumn()
    else:
        raise ValueError("Unknown season")
    
    print(f'{s}:')
    s.print_months()

except ValueError as e:
    print(e)
