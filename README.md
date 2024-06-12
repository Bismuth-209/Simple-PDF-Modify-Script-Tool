# Simple-PDF-Modify-Script-Tool
A simple python script for modifying PDF files based on PyPDF2.

## format
source_file_path   options   subcommand

## options
1. --new-path destination_file_path
the result of modification will be saved into the new file

## subcommand

### get page
select pages of indices in source PDF and merge into a new PDF in same order
#### format
get-page page_indices
#### page indicies
indices of target pages
formated as [p1],[p2],[p3],...,[pn] or [p1]-[p2],[p3],...,[pn]
for example, if you need page 1, 2, 5, 6, 7, 8, 9, 16
you can type 1,2,5-9,16

### delete page
delete pages of the indices
#### format
delete-page page_indices
#### page indices
indices of target pages
formated as [p1],[p2],[p3],...,[pn] or [p1]-[p2],[p3],...,[pn]
for example, if you don't need page 1, 2, 5, 6, 7, 8, 9, 16
you can type 1,2,5-9,16
