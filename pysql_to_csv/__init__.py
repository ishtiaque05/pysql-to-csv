import argparse
from pysql_to_csv.converter import Converter

def cli():
    parser = argparse.ArgumentParser(description="Find the commit statistic in particular file")
    parser.add_argument(
        'host',
        type=str,
        help="Input filename or directory to find the commit stats"
    )
    parser.add_argument(
        'user',
        type=str,
        help="Username of the host sql"
    )

    parser.add_argument(
        'passwd',
        type=str,
        help="Password for sql"
    )

    parser.add_argument(
        'db',
        type=str,
        help="Database name to connect to"
    )

    parser.add_argument(
        'tblname',
        type=str,
        help="Table name to convert to csv"
    )

    return parser.parse_args()

def runner():
    args = cli()
    converter = Converter(args)
    converter.execute_query()