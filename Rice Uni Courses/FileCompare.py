"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if(len(line1) < len(line2)):
        min_len = len(line1)
    else:
        min_len = len(line2)

    for index in range(min_len):
        if(line1[index] != line2[index]):
            return index

    if(len(line1) == len(line2)):
        return IDENTICAL
    elif(len(line1) > len(line2)):
        return len(line2)
    else:
        return len(line1)


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if(len(line1) < len(line2)):
        min_len = len(line1)
    else:
        min_len = len(line2)

    if(idx < 0 or idx > min_len):
        return ""
    elif("\n" in line1 or "\r" in line1):
        return ""
    elif("\n" in line2 or "\r" in line2):
        return ""
    else:
        string = []
        string.append(line1)
        string.append("\n")
        string.append("="*idx)
        string.append("^")
        string.append("\n")
        string.append(line2)
        string.append("\n")
        return "".join(string)


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if(len(lines1) < len(lines2)):
        min_len = len(lines1)
    else:
        min_len = len(lines2)

    for line_no in range(min_len):
        check = singleline_diff(lines1[line_no], lines2[line_no])
        if(check > -1):
            return(line_no, check)
    if(len(lines1) > len(lines2)):
        return len(lines2), 0
    elif(len(lines2) > len(lines1)):
        return len(lines1), 0
    else:
        return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    para = []
    datafile = open(filename, "rt")
    for line in datafile:
        if(line[-1] == "\n" or line[-1] == "\r"):
            para.append(line[:-1])
        else:
            para.append(line)
    return para


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    datafile1 = open(filename1, "rt")
    datafile2 = open(filename2, "rt")
    line_no = -1
    for line1, line2 in zip(datafile1, datafile2):
        line_no += 1
        idx = singleline_diff(line1, line2)
        if idx > -1:
            string1 = "".join(["Line ", str(line_no), ":\n"])
            string = []
            string.append(line1)
            string.append("="*idx)
            string.append("^")
            string.append("\n")
            string.append(line2)
            string2 = "".join(string)
            return string1 + string2
    return "No differences\n"
