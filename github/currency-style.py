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
    m = re.split("(, | |\.$|\n)", text)
    print(m)
    for index, item in enumerate(m):
        if item and item[0] == "$":
            if (not re.search(r"\.\d{0,2}$",item)) and item[-1].isdigit():
                print("to check: "+ str(item))
                if not re.search(r'\,\d{3}$',item):
                    m[index] = convert(item)
                    print("converted: "+str(m[index]))
        text = "".join(m)
    print("text="+text)
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
    assert checkio("$222,100,455") == "$222,100,455"

