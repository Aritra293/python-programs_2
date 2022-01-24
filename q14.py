def swap_case_string(string1):
    result_str = ""  
    for item in string1:
       if item.isupper():
           result_str += item.lower()
       else:
           result_str += item.upper()           
    return result_str
print(swap_case_string("Python Exercises"))
print(swap_case_string("Java"))
print(swap_case_string("NumPy"))


    