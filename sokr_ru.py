import os
import argparse
from crawler import try_to_parse
import parser

def run_crawler(tries_per_proc, processes):
    os.makedirs("./data", exist_ok=True)
    try_to_parse(tries_per_proc=tries_per_proc, processes=processes)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        description="Trying to randomly find all abbreviation from sokr.ru"
    )
    argparser.add_argument(
        "unit",
        help="[crawler|parser]",
        action="store",
    )
    argparser.add_argument(
        "command",
        help="Command for unit [crawler run]|[parser parse]",
        action="store",
    )
    argparser.add_argument(
        "--processes", "-p", help="Change number of processes", action="store", type=int
    )
    argparser.add_argument(
        "--tries-per-process",
        "-tpp",
        help="Change amount of tries per process",
        action="store",
        type=int,
    )
    args = argparser.parse_args()

    processes = 64
    tries_per_proc = 10 ** 7


    if args.unit == "crawler":
        if args.command == "run":
            if args.processes:
                processes = args.processes
            if args.tries_per_process:
                tries_per_proc = args.tries_per_process
            run_crawler(tries_per_proc=tries_per_proc, processes=processes)
        else:
            parser.print_help()

    if args.unit == "parser":
        if args.command == "parse":
            parser.parse()
        else:
            argparser.print_help()
            

    if args.command == "":
        argparser.print_help()