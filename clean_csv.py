import io
import csv

def clean_csv(input_stream):
    """
    From my coding test with NextGate Tech
    Given an Input string, return string contain csv data without the header and also skip None items
    :param input_stream: (StringIO) An in-memory stream for text I/O containing CSV data
    :returns: (String) A string containing CSV data
    """
    all_lines = input_stream.read()
    lns = all_lines.split("\n")
    i = 0
    for item in lns:
        if i == 0:
            i+=1
            pass
        else:
            if ',' not in item:
                pass
            else:
                print(item)
    
    return 
                    

input_stream = io.StringIO("Name,Surname\nJohn,Doe\nAnn,Franklin\nMichael,Mbajwa\n\nTersoo,Mbajwa")
result_csv = clean_csv(input_stream)
input_stream.close()