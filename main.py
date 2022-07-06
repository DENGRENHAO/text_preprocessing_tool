import argparse
from text_preprocessing_tool import text_preprocessing

def parse_argument():
    parser = argparse.ArgumentParser(description='Text Preprocessing Tool')
    parser.add_argument('-i', '--input', type=str, required=True,
                        help='Complete path and filename for the csv file.')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_argument()
    if args.input:
        new_file = text_preprocessing(args.input)
        print(f"Completed output {new_file}")