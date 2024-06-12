# Simple-PDF-Modify-Script-Tool
A simple python script for modifying PDF files based on PyPDF2.

command format:
[source file path] (-options) (subcommand)

options:
  --new-path [destination file path]
    the result of modification will be saved into the new file

subcommand:
  get-page [page indices]
    select pages of indices in source PDF and merge into a new PDF in same order

    page indicies:
      indices of target pages
      formated as [p1],[p2],[p3],...,[pn] or [p1]-[p2],[p3],...,[pn]
      for example, if you need page 1, 2, 5, 6, 7, 8, 9, 16
      you can type 1,2,5-9,16

  delete-page [page indices]
    delete pages of the indices

    page indices:
      indices of target pages
      formated as [p1],[p2],[p3],...,[pn] or [p1]-[p2],[p3],...,[pn]
      for example, if you don't need page 1, 2, 5, 6, 7, 8, 9, 16
      you can type 1,2,5-9,16
