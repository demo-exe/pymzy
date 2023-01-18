import logging, argparse


def init_argparse(parser):
    group = parser.add_argument_group('logging')
    group.add_argument(
        '--logfile',
        help='File for writing logs',
        type=argparse.FileType('w', encoding="utf-8"))

    vgroup = group.add_mutually_exclusive_group()
    vgroup.add_argument('-v', action='count', default=0, dest='verbosity',
        help="Increase verbosity")
    vgroup.add_argument('-q', action='count', default=0, dest='quietness',
        help="Decrease verbosity")


def init_logging(args):
    print("Verbosity =", args.verbosity - args.quietness)

def simple_logging_init():
    parser = argparse.ArgumentParser(prog='PROG')
    init_argparse(parser)
    init_logging(parser.parse_args())
