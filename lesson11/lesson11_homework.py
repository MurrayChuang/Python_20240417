from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str
    website: str
    state: str = Field(alias="from")


class PeopleData(BaseModel):
    people: list[Person]


with open('data.json', encoding='utf-8') as file:
    people_data: PeopleData = PeopleData.model_validate_json(file.read())

for person in people_data.people:
    print(person)
