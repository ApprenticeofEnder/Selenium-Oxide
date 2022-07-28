from faker import Faker

class SeO2User:
    def __init__(self, gen: Faker = None, locale: str = "en_US", **data) -> None:
        self.gen = gen if gen else Faker(locale)
        base_profile = self.gen.simple_profile()
        self.sex = data.get("sex", base_profile["sex"])
        if self.sex == "M":
            name = self.gen.name_male()
        elif self.sex == "F":
            name = self.gen.name_female()
        else:
            name = self.gen.name_nonbinary()
        self.name = data.get("name", name)
        self.first_name = self.name.split(' ')[0]
        self.last_name = self.name.split(' ')[1]
        self.username = data.get("username", base_profile["username"])
        self.email = data.get("email", base_profile["mail"])
        self.address = data.get("address", base_profile["address"])
        self.birthdate = data.get("birthdate", base_profile["birthdate"])
    
    def __str__(self) -> str:
        return f"{self.name} ({self.sex}), username {self.username}, email {self.email}, DOB {str(self.birthdate)}"

    def get_generator(self) -> Faker:
        return self.gen