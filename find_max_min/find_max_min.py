'''module for finding maximum and minimun elements of an array'''

def find_max_min(array_list):
    '''the find_max_min function'''
    array_list.sort() 
    if array_list[0] == array_list[-1]:
        return [len(array_list)]
    else:
        return [array_list[0], array_list[-1]]
    