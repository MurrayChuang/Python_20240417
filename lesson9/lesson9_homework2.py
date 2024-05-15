from dataclasses import dataclass
import pyinputplus as pyip

name = input('請輸入姓名:')
height = pyip.inputFloat('請輸入身高(cm):', min=1, max=300)
weight = pyip.inputFloat('請輸入體重(kg):', min=1, max=500)

@dataclass
class BMI():
    name:str
    height:float
    weight:float

    @property
    def bmi(self):
        return weight / (height / 100)**2

    def status(self) -> str:
        bmi_value = self.bmi
        if bmi_value < 18.5:
            result = '過輕'
        elif bmi_value < 24:
            result = '正常'
        elif bmi_value < 27:
            result = '過重'
        elif bmi_value < 30:
            result = '輕度肥胖'
        elif bmi_value < 35:
            result = '中度肥胖'
        else:
            result = '重度肥胖'
        return result

user = BMI(name, height, weight)

print(f"{user.name}您好:")
print(f"您的bmi值是{user.bmi:.2f}")
print(f"您的體重:{user.status()}")