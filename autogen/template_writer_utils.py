def get_path_variables(resource_path):
    ''' Returns wildcard parameters by extracting from path'''
    resource_path = resource_path.replace('/redfish/v1/', '')
    sub_path = resource_path.split("/")
    var_list = [i for j, i in enumerate(sub_path) if j % 2 != 0]
    return var_list