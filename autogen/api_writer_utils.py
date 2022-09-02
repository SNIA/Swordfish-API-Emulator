import re


def get_function_parameters(path):
    ''' get parameters for function definition'''
    sub_path = re.split(r"\/", path)
    arg_str = ''
    arg_list = []

    for sub in sub_path:
        if '{' in sub:
            arg_list.append(sub.replace('{', '').replace('}', ''))

    if len(arg_list) >= 1 :
        arg_str = arg_list[0]
        for i in range(len(arg_list)-1):
            arg_str = arg_str + ', ' + arg_list[i+1]
    
    return arg_str

def get_path_parameters(path):
    ''' get path specific parameters to create a either collection path or instance path'''
    sub_path = re.split(r"\/", path)
    arg_list = []
      
    for sub in sub_path:
        if '{' in sub:
            arg_list.append(sub.replace('{', '').replace('}', ''))

    if(len(arg_list) >= 1):
        num = 0
        for res in arg_list:
            if (path.find(res)!=1):
                path = path.replace(res, '{0}'.format(num))
                num = num +1
    return path

def get_wildcard_parameters(arg_str):
    arguments = re.split(', ', arg_str)
    wc_str = ''
    for i in range(len(arguments)):
        wc_str = wc_str + "'{0}':{0}, ".format(arguments[i])
    return wc_str