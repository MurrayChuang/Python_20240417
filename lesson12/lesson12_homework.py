import requests
from requests import Response

aqi_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'

res: Response = requests.get(aqi_url)
if res.status_code == 200:
    print("下載成功")
else:
    print("下載失敗")

from pydantic import BaseModel, Field, field_validator


class Site(BaseModel):
    site_name: str = Field(alias='sitename')
    county: str
    aqi: int
    status: str
    pm25: float = Field(alias='pm2.5')
    so2: float
    co: float

    @field_validator('pm25', 'so2', 'co', mode='before')
    @classmethod
    def whitespace_to_zero(cls, value: str) -> str:
        if value == '':
            return '0.0'
        else:
            return value


class AQI(BaseModel):
    records: list[Site]


data1: AQI = AQI.model_validate_json(res.text)
for item in data1.records:
    print(item)
