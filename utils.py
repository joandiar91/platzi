import read_csv
from collections import Counter

def get_occupation_count(data):
  bmi_condition = ('Overweight','Obese')
  result = list(filter(lambda item: item['BMI Category'] in bmi_condition, data))
  occupation = list(map(lambda item: item['Occupation'], result))
  counter = dict(Counter(occupation))
  return counter

if __name__ == '__main__':
  data = read_csv.read_csv('final_project/data.csv')
  get_occupation_count(data)