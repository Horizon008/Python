class RegistrationError(Exception): 
    pass
 # Используется для обозначения ошибок регистрации.
class ExcessOccupantsError(RegistrationError): 
    pass
    # Используется для обозначения ошибки регистрации из-за избыточного количества жильцов.

class SameGenderError(RegistrationError): 
    pass
    # Используется для обозначения ошибки регистрации из-за однообразия пола жильцов.

class DuplicateGenderError(SameGenderError): 
    pass
    # Используется для обозначения ошибки регистрации из-за дублирования пола жильцов.

class OccupantHasResidenceError(RegistrationError): 
    pass
    # Используется для обозначения ошибки регистрации из-за уже заселенного жильца.

class Inhabitant:
    def settle(self, residence):
        if not self._settled:
            residence.register(self)
            self._settled = True
        else:
            raise OccupantHasResidenceError()
                # Регистрирует жильца в жилище, если он не зарегистрирован ранее, иначе вызывает ошибку OccupantHasResidenceError.

    def __init__(self, given_name):
        self._given_name = given_name
        self._settled = False

    def compatible(self, others):
        if len(others) > 1:
            raise ExcessOccupantsError()

class Gentleman(Inhabitant):
    def __repr__(self):
        return "\u265A(%s)" % self._given_name

    def compatible(self, others):
        super().compatible(others)
        try:
            if isinstance(others[0], Gentleman):
                raise SameGenderError()
        except IndexError:
            pass
            # Проверяет совместимость мужчины с другими жильцами, вызывая ошибку SameGenderError при присутствии другого мужчины.

class Lady(Inhabitant):
    def __repr__(self):
        return "\u265B(%s)" % self._given_name

    def compatible(self, others):
        super().compatible(others)
        if others and isinstance(others[0], Lady):
            raise DuplicateGenderError()

            # Проверяет совместимость женщины с другими жильцами, вызывая ошибку DuplicateGenderError, если уже присутствует другая женщина.

class Dwelling:
    def __init__(self, designation):
        self._designation = designation
        self._occupants = []

    def register(self, inhabitant):
        try:
            inhabitant.compatible(self._occupants)
            self._occupants.append(inhabitant)
        except Exception as e:
            raise e
            # Регистрирует жильца в жилище, вызывая ошибку при возникающих проблемах совместимости или переполнении жилища.

    def is_full(self):
        return len(self._occupants) > 0
        # Проверяет, заполнено ли жилище.

    def residents(self):
        return self._occupants
        # возвращает список жильцов в жилище.

    def __repr__(self):
        return "\u26EA(%s, %s)" % (self._designation, self._occupants)

from itertools import product
from sys import stderr
import unittest

class TestDwellingRegistration(unittest.TestCase):
    def test_successful_registration(self):
        dwelling = Dwelling('1A')
        gentleman = Gentleman("Егор")
        dwelling.register(gentleman)
        self.assertIn(gentleman, dwelling.residents())

    def test_duplicate_gender_error(self):
        dwelling = Dwelling('2B')
        lady1 = Lady("Таисия")
        lady2 = Lady("Ксения")
        dwelling.register(lady1)
        with self.assertRaises(DuplicateGenderError):
            dwelling.register(lady2)

    def test_excess_occupants_error(self):
        dwelling = Dwelling('3C')
        gentleman1 = Gentleman("Андрей")
        gentleman2 = Gentleman("Иван")
        gentleman3 = Gentleman("Никита")
        with self.assertRaises(ExcessOccupantsError):
            dwelling.register(gentleman1)
            dwelling.register(gentleman2)
            dwelling.register(gentleman3)
            
# if __name__ == '__main__':
#     unittest.main()
    
if __name__ == '__main__':
    for locale, individual in product(
        (Dwelling('1A'), Dwelling('2B')),
        (Gentleman("Егор"), Gentleman("Андрей"), Lady("Таисия"), Lady("Ксения"))
    ):
        try:
            individual.settle(locale)
            print(individual, locale)
        except Exception as e:
            print(type(e), individual, locale, file=stderr)
