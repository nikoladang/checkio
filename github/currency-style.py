__author__ = 'nikoladang'
# http://stackoverflow.com/questions/1540049/replace-values-in-list-using-python
# http://stackoverflow.com/questions/3519487/python-regex-re-sub-replacing-multiple-parts-of-pattern/3519536#3519536
# Python: How can I include the delimiter(s) in a string split? --> http://stackoverflow.com/a/21208564/2493265
# http://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters
    # Python - Split Strings with Multiple Delimiters --> http://stackoverflow.com/a/1059596/2493265
import re

def convert(string):
    string = re.sub(r'(\d)\,(\d)', r"\1temp\2", string)
    string = re.sub(r'(\d)\.(\d)', r"\1,\2", string)
    string = re.sub(r'(\d)temp(\d)', r"\1.\2", string)
    return string

def checkio(text):

    "Convert Euro style currency in dollars to US/UK style"
    # if not re.search("Euro", text):
    #     text = convert(text)
    # else:
    #     m = re.split(", ", text)
    #     for index, item in enumerate(m):
    #         # if "Euro" in item:
    #         if not re.search(r"\.\d\d$",item): # unchange if already US Style
    #             m[index] = convert(item)
    #         text = ", ".join(m)
    # print(text)

    # m = re.split(", ", text)
    # for index, item in enumerate(m):
    #     if (not re.search(r"\.\d\d$",item)) and (not re.search(r"\,\d\d\d", item)): # unchange if already US Style
    #         m[index] = convert(item)
    #     text = ", ".join(m)

    m = re.split("(, | )", text)
    for index, item in enumerate(m):
        if (not re.search(r"\.\d\d$",item)) and (not re.search(r"\,\d\d\d", item)): # unchange if already US Style
            m[index] = convert(item)
        text = "".join(m)
    print(m)
    print(text)
    return text

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
    assert checkio("$5.34") == "$5.34" , "1st Example"
    assert checkio("$4.545,45 is less than $5,454.54.") == "$4,545.45 is less than $5,454.54." , "1st Example"
