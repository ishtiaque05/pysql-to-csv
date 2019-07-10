import argparse
from mysqldump_to_csv.parser import Parser

def cli():
    parser = argparse.ArgumentParser(description="Convert a mysql dump file to csv")
    parser.add_argument(
        'filename',
        type=str,
        help="dump mysql filename source"
    )
    
    return parser.parse_args()

def runner():
    args = cli()
    parser = Parser(args)
    parser.parse()