from template_writer_utils import get_path_variables


def write_program_header(outfile, base_template_name):
    """ Writes a template program header """
    outfile.write('#\n')
    outfile.write('# Copyright (c) 2017-2021, The Storage Networking Industry Association.\n')
    outfile.write('#\n')
    outfile.write('# Redistribution and use in source and binary forms, with or without\n')
    outfile.write('# modification, are permitted provided that the following conditions are met:\n')
    outfile.write('#\n')
    outfile.write('# Redistributions of source code must retain the above copyright notice,\n')
    outfile.write('# this list of conditions and the following disclaimer.\n')
    outfile.write('#\n')
    outfile.write('# Redistributions in binary form must reproduce the above copyright notice,\n')
    outfile.write('# this list of conditions and the following disclaimer in the documentation\n')
    outfile.write('# and/or other materials provided with the distribution.\n')
    outfile.write('#\n')
    outfile.write('# Neither the name of The Storage Networking Industry Association (SNIA) nor\n')
    outfile.write('# the names of its contributors may be used to endorse or promote products\n')
    outfile.write('# derived from this software without specific prior written permission.\n')
    outfile.write('#\n')
    outfile.write('#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"\n')
    outfile.write('#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n')
    outfile.write('#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n')
    outfile.write('#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE\n')
    outfile.write('#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR\n')
    outfile.write('#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF\n')
    outfile.write('#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS\n')
    outfile.write('#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN\n')
    outfile.write('#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)\n')
    outfile.write('#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF\n')
    outfile.write('#  THE POSSIBILITY OF SUCH DAMAGE.\n')
    outfile.write('\n')
    outfile.write("# Template for - {0}\n".format(base_template_name))
    outfile.write('# Program name - {0}.py\n'.format(base_template_name))
    outfile.write('\n')
    outfile.write('import copy\n')
    outfile.write('from flask import json\n')
    outfile.write('\n')
    return

def write_template(outfile, resource_path, json_schema):
    ''' Writes actual template body'''
    outfile.write("_TEMPLATE = \\")
    outfile.write("\n")
    outfile.write("{\n")
    outfile.write('\t"@Redfish.Copyright": "Copyright 2014-2021 SNIA. All rights reserved.",\n')

    # All the template will have required properties -
    #  "@odata.id", "@odata.type", "Id", "Name", etc
    resource = json_schema['$ref'].split('/')[-1]
    required_properties = json_schema["definitions"][resource]["required"]

    for req_prop in required_properties:
        if req_prop == '@odata.id':
            new_resource_path = resource_path.replace('/redfish/v1/', '')
            outfile.write('\t"@odata.id": "{{rb}}{0}",\n'.format(new_resource_path))
        elif req_prop == '@odata.type':
            outfile.write('\t"@odata.type": "{0}",\n'.format(json_schema["title"]))
        elif req_prop == 'Id':
            outfile.write('\t"Id": "{0}",\n'.format(resource_path.split("/")[-1]))
        elif req_prop == 'Name':
            # Get value for "Name" property from user
            # name = input("Give value to the property 'Name' of {0}:".format(resource_path))
            outfile.write('\t"Name": "{0}",\n'.format(resource))
        else:
            req_prop_value = input("Enter the string value for required property {0} : ".format(req_prop))
            outfile.write('\t"{0}": "{1}",\n'.format(req_prop, req_prop_value))

    # Giving option to user to add more properties and its values.
    # follow = input("Do you want to add more properties to the template file (y/n)?")
    # if follow == 'y':
    #     while True:
    #         added_data = input("Add new property and it's value (to stop, press enter): ")
    #         if added_data != '':
    #             outfile.write("\t"+ added_data)
    #             outfile.write("\n")
    #         else:
    #             break
    # else:
    #     pass

    outfile.write("}\n\n")
    return

def write_program_end(outfile, base_template_name, resource_path):
    ''' Write the get_*_instance() function '''
    argument_string = "def get_{0}_instance(wildcards):\n".format(base_template_name)
    outfile.write(argument_string)
    outfile.write('\t\t"""\n')
    outfile.write('\t\tInstantiates and formats the template\n')
    outfile.write('\t\tArguments:\n')
    outfile.write('\t\t\twildcard - A dictionary of wildcards strings and their repalcement values\n')
    outfile.write('\t\t"""\n')
    outfile.write('\t\tc = copy.deepcopy(_TEMPLATE)\n')
    outfile.write('\t\td = json.dumps(c)\n')
    
    arg_list = get_path_variables(resource_path)
    num = 0
    outfile.write("\t\tg = d.replace('{0}', '{1}')\n".format(arg_list[0], num))
    num = num + 1
    for i in range(len(arg_list)-1):
        outfile.write("\t\tg = g.replace('{0}', '{1}')\n".format(arg_list[i+1], num))
        num = num + 1
    
    outfile.write("\t\tg = g.replace('{rb}', 'NUb')\n")
    outfile.write("\t\tg = g.replace('{{', '~~!')\n")
    outfile.write("\t\tg = g.replace('}}', '!!~')\n")
    outfile.write("\t\tg = g.replace('{', '~!')\n")
    outfile.write("\t\tg = g.replace('}', '!~')\n")

    num = 0
    for arg in arg_list:
        outfile.write("\t\tg = g.replace('{0}', '{1}')\n".format(num, arg))
        num = num + 1

    outfile.write("\t\tg = g.replace('NUb', '{rb}')\n")
    outfile.write("\t\tg = g.format(**wildcards)\n")
    outfile.write("\t\tg = g.replace('~~!', '{{')\n")
    outfile.write("\t\tg = g.replace('!!~', '}}')\n")
    outfile.write("\t\tg = g.replace('~!', '{')\n")
    outfile.write("\t\tg = g.replace('!~', '}')\n")
    outfile.write("\t\treturn json.loads(g)")
    return