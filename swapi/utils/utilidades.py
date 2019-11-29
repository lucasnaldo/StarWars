from unicodedata import normalize
from datetime import datetime

def cores_olhos(text):
    if text == 'red':
        text = 'vermelho'
    elif text == 'white':
        text = 'branco'
    elif text == 'black':
        text = 'preto'
    elif text == 'gray' or text == 'grey':
        text = 'cinza'
    elif text == 'blue':
        text = 'azul'
    elif text == 'green':
        text = 'verde'
    elif text == 'brown':
        text = 'castanho'
    elif text == 'amber':
        text = 'ambar'
    else:
        text = text

    return text

def sexo(text):
    if text == 'male':
        text = 'Masculino'
    elif text == 'female':
        text = 'Feminino'
    else:
        text = text

    return text

def to_date_swagger(txt):
    n_date = datetime.strptime(txt, "%Y-%m-%d").date()
    day, month, year = n_date.day, n_date.month, n_date.year
    if day < 10: day = "0"+str(n_date.day)
    if month < 10: month = "0"+str(n_date.month)
    return f"{day}/{month}/{year}"
