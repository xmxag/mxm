class Date:
    def __init__(self, day, mouth, year):
        self.day =day
        self.mouth = mouth
        self.year = year

    def get_day(self):
        return self.__day

    def get_mouth(self):
        return self.__mouth

    def get_year(self):
        return self.__year
    def set_day(self,day):
        self.day=day

    def set_mouth(self,mouth):
        self.mouth=mouth

    def set_year(self,year):
        self.year=year


day= int(input("день:"))
mouth= int(input("месяц:"))
year= int(input("год:"))

date1=Date (day,mouth,year)
print("пациент родился {}.{}.{}".format(date1.day,date1.mouth,date1.year))