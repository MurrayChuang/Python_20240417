import pyinputplus as pyip

def bmi(weight: float, height: float) -> float:
    return weight / (height / 100) ** 2

def get_status(bmi: float) -> str:
    if bmi < 18.5:
        result = '過輕'
    elif bmi < 24:
        result = '正常'
    elif bmi < 27:
        result = '過重'
    elif bmi < 30:
        result = '輕度肥胖'
    elif bmi < 35:
        result = '中度肥胖'
    else:
        result = '重度肥胖'
    return result

name = input('請輸入姓名:')
height = pyip.inputFloat('請輸入身高(cm):', min = 1, max = 300) 
weight = pyip.inputFloat('請輸入體重(kg):', min = 1, max = 500) 
bmi_value = bmi(weight, height)
print(f'{name}, 您的BMI: {bmi_value:.2f}')
print(f'{name}, 您的體重: {get_status(bmi_value)}')