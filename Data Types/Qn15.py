# function that inserts a string into middle of a string
def insert_string_middle(cover,string):
    half=len(cover)//2
    print(f"{cover[:half]}{string}{cover[half:]}")
insert_string_middle('{{}}','PHP')
insert_string_middle('[]','hello')
insert_string_middle('[[[]]]','Konichiwa')
