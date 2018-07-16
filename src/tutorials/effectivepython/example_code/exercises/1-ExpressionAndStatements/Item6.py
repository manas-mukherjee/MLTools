#Item6 : Take adv of each block
# TRY/EXCEPT/ELSE/FINALLY

handle = open("/tmp/random_data.txt", "w", encoding="utf-8")
handle.write('Mr\nManas\n\Kumar\nMukherjee')
handle.close() #not guranteed to work in all cases

handle1 = open('/tmp/random_data.txt') #IOError
try:
    data = handle1.read() #Unicode decoder
finally:
    print("finally called")
    handle1.close()
    print("finally closed")

print(data)


#try/except/else
import json

def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # Raise valueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key] # Key Error

try:
    #load_json_key('{"foo": bad payload', 'foo')
    #load_json_key('{"foo": "bar"}', 'zoo')
    load_json_key('{"foo": "bar"}', 'foo')
except KeyError:
    print('Saw Keyerror')


UNDEFINED = object()

def divide_json(path):
    hl = open(path, 'r+') #IOError
    try:
        data = hl.read() #UnicodeDecode Error
        op = json.laods(data) # ValueError
        value = op['numerator'] / op['denominator'] #ZeroDivision Error
    except ZeroDivisionError:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dump(op)
        hl.seek(0)
        handle.write(result) #IOError
        return value
    finally:
        hl.close() #Always runs

temp_path = '/temp/random_data.json'
with open(temp_path, 'w') as hl:
    hl.write('{"numerotor":1, "denominaotr":0}')

print((divide_json(temp_path)))

