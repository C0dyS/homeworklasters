class City:
    def __init__(self,city_name,region,country,amount_of_people_living,post_index,telephone_code):
        self.city_name = city_name
        self.region = region
        self.country = country
        self.amount_of_people_living = amount_of_people_living
        self.post_index = post_index
        self.telephone_code = telephone_code
    def get_info(self):
        return self.city_name,self.region,self.post_index,self.amount_of_people_living,self.telephone_code
    def example_change_method(self,new_value):
        self.city_name = new_value
