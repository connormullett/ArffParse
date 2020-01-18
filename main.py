
import argparse

parser = argparse.ArgumentParser(description='ARFF parsing tool')
parser.add_argument('input', help='path for input ARFF file')
parser.add_argument('-o', '--out', help='name of output file')
parser.add_argument('-v', '--verbose', help='display more info',
    action='store_true')

args = parser.parse_args()


input_path = args.input
output_path = args.out if args.out else None

if not output_path:
  output_path = input_path.split('.')[0] + '.csv'

if args.verbose:
  print('using input file %s' % input_path)
  print('using output file %s' % output_path)


def read_file(file_path):
  with open(file_path, 'r') as f:
    return f.read()


def main():
  data = read_file(input_path)

  # build attributes
  attributes = [line for line in data.split('\n') if line.startswith('@attribute')]
  attributes = [attr.replace('\t', ' ') for attr in attributes]
  attributes = [attr.split(' ')[1] for attr in attributes]

  # build data

if __name__ == '__main__':
  main()

