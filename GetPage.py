import PyPDF2


def get_page(args):
    page_list = page_index_unzip(args.get_page_index)
    get_pages_of_index_list(args, page_list)


def get_pages_of_index_list(args, index_list):
    src_file = open(args.source_file, "rb")
    pdf_src = PyPDF2.PdfReader(src_file)
    pdf_dest = PyPDF2.PdfWriter()
    for page in index_list:
        pdf_dest.add_page(pdf_src.pages[page-1])

    src_file.close()
    if args.new_file is None:
        dest_file = open(args.source_file, "wb")
    else:
        dest_file = open(args.new_file[0], "wb")

    pdf_dest.write(dest_file)
    dest_file.close()


def page_index_unzip(s_list):
    index_list = []
    for i in s_list:
        if i.find("-") != -1:
            a, b = list(map(lambda x: int(x), i.split("-")))
            for j in range(a, b+1):
                index_list.append(j)

        else:
            index_list.append(int(i))

    return index_list
