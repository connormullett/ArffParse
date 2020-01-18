
import argparse

parser = argparse.ArgumentParser(description='ARFF parsing tool')
parser.add_argument('input', help='path for input ARFF file')
parser.add_argument('-o', '--out', help='name of output file')
parser.add_argument('-v', '--verbose', help='display more info',
    action='store_true')

args = parser.parse_args()
verbose = args.verbose


def read_file(file_path):
  with open(file_path, 'r') as f:
    return f.read()


def print_verbose(msg):
  if verbose:
    print(msg)


def main():

  input_path = args.input
  output_path = args.out if args.out else None

  if not output_path:
    output_path = input_path.split('.')[0] + '.csv'

  print_verbose('using input file %s' % input_path)
  print_verbose('using output file %s' % output_path)

  data = read_file(input_path)

  # build attributes
  print_verbose('parsing attributes')

  attributes = [line for line in data.split('\n') if line.startswith('@attribute')]
  attributes = [attr.replace('\t', ' ') for attr in attributes]
  attributes = [attr.split(' ')[1] + ',' for attr in attributes]

  # build data
  print_verbose('parsing data rows')

  data_rows = []
  found = False
  for line in data.split('\n'):

    if line.startswith('%'):
      continue

    if found:
      line += '\n'
      data_rows.append(line)

    if line.startswith('@data'):
      found = True

  print_verbose('writing to %s' % output_path)

  # output data
  with open(output_path, 'w+') as f:
    f.writelines(attributes)
    f.writelines(data_rows)
    
  print_verbose('finished writing .. cleaning up')
  print('done')


if __name__ == '__main__':
  main()

