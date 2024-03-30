class Human:
    def __init__(self,PiB,date_of_birth,phone_number,city,country,adress):
        self._PiB = PiB
        self._date_of_birth = date_of_birth
        self._phone_number = phone_number
        self._city = city
        self._country = country
        self._adress = adress
    def get_info(self):
        return self._PiB,self._city,self._adress,self._date_of_birth,self._phone_number
    def example_change_method(self,new_value):
        self._PiB = new_value
