import PyPDF2

import GetPage


def delete_page(args):
    src_file = open(args.source_file, "rb")
    pdf_src = PyPDF2.PdfReader(src_file)
    index_list = list(range(1, len(pdf_src.pages)+1))
    for i in GetPage.page_index_unzip(args.delete_page_index):
        index_list.remove(i)

    src_file.close()
    GetPage.get_pages_of_index_list(args, index_list)
