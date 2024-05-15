import pyinputplus as pyip

name = input('請輸入姓名:')
height = pyip.inputFloat('請輸入身高(cm):', min=1, max=300)
weight = pyip.inputFloat('請輸入體重(kg):', min=1, max=500)


class BMI():

    def __init__(self, n: str, h: float, w: float):
        super().__init__()
        self.name = n  #attribute
        self.height = h  #attribute
        self.weight = w  #attribute

    def __repr__(self):
        message = f"{self.name}您好:\n"
        message += f"您的bmi值是{self.bmi:.2f}\n"
        message += f"您的體重:{self.status()}\n"
        return message

    #建立property的語言

    @property
    def bmi(self):
        return weight / (height / 100)**2

    #建立實體方法

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


user_bmi = BMI(name, height, weight)
print(user_bmi)
