import read_csv
import utils
import charts

def run():
  data = read_csv.read_csv('final_project/data.csv')
  occupations_summary = utils.get_occupation_count(data)
  occupations = occupations_summary.keys()
  count = occupations_summary.values()

  charts.generate_pie_chart(occupations, count)
  

if __name__ == '__main__':
  run()