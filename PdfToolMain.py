import argparse

import DeletePage
import GetPage

parser = argparse.ArgumentParser(description="A Simple PDF Tool")

parser.add_argument(
        "source_file",
        help="path of source file"
)

subparsers = parser.add_subparsers(
        title="operation",
        required=True,
        help="target pages list, formated as [p1],[p2],...,[pn]",
        metavar="get-page"
)

get_page_parser = subparsers.add_parser(
        "get-page",
        help="extract selected pages from source pdf and merge to a new pdf in same order"
)

get_page_parser.add_argument(
        "get_page_index",
        type=lambda x: x.split(","),
        help="page index in format [p1],[p2],...,[pn] or [p1],[p2]-[p3],[pn], p1<p2<...<pn"
)

get_page_parser.set_defaults(func=GetPage.get_page)

delete_page_parser = subparsers.add_parser(
        "delete-page",
        help="delete selected pages from source pdf"
)

delete_page_parser.add_argument(
        "delete_page_index",
        type=lambda x: x.split(","),
        help="page index in format [p1],[p2],...,[pn] or [p1],[p2]-[p3],[pn], p1<p2<...<pn"
)

delete_page_parser.set_defaults(func=DeletePage.delete_page)

parser.add_argument(
        "--new-file",
        nargs=1,
        help="path of dest file",
)

args = parser.parse_args()

args.func(args)
