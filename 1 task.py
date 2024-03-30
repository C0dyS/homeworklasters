class Country:
    def __init__(self,name_of_country,continent,people_living,telephone_code,main_city,list_of_cities):
        self.name_of_country = name_of_country
        self.continent = continent
        self.people_living = people_living
        self.telephone_code = telephone_code
        self.main_city = main_city
        self.list_of_cities = list_of_cities
    def add_city(self,new_city):
        self.list_of_cities.append(new_city)
    def change_capitol(self,new_capitol):
        self.main_city = new_capitol
    def get_info(self):
        return self.name_of_country,self.continent,self.people_living,self.telephone_code,self.main_city,self.list_of_cities