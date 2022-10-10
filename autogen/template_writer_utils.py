def get_path_variables(resource_path):
    ''' Returns wildcard parameters by extracting from path'''
    resource_path = resource_path.replace('/redfish/v1/', '')
    sub_path = resource_path.split("/")
    var_list = []

    # var_list = [i for j, i in enumerate(sub_path) if j % 2 != 0]
    for sub in sub_path:
        if '{' in sub:
            var_list.append(sub)
    return var_list