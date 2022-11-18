import csv
import json
import hashlib
import os
 
csv_file_path = input('Enter the absolute path of the CSV file: ')
json_file_path = input('Enter the absolute path of the JSON file: ')

def csv_to_json(csv_file_path, json_file_path):
    '''
    takes csvfile
    generates CHIP-0007 json
    '''
    data_dict = {}
    
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        for rows in csv_reader:
            key = rows['Serial Number']
            data_dict[key] = rows
 
    with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent = 4))
    
    # return data_dict
    print(data_dict)

def calc_sha256():
    '''
    calculates sha256 of json file
    '''
    filename = json_file_path
    sha256_hash = hashlib.sha256()

    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        return(sha256_hash.hexdigest())
        # print(sha256_hash.hexdigest())

def rename_csv():
    '''
    appends it to each line of csvfile
    '''
    try:
        for filename in os.listdir(csv_file_path.Filename):
            print(filename)
            new_name = f"{csv_file_path}.{calc_sha256()}.'csv'"
        print(os.rename(filename, new_name))
    except OSError:
        raise('there is an error')
