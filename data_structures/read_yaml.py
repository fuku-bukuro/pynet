from pprint import pprint
import yaml

filename = input("enter file name: ")
with open(filename) as f:
    yaml_out = yaml.safe_load(f)
    print(yaml_out)

    #    with open("out_file.log", 'w') as out_f:
 #       out_f.write(yaml_out)
  #      pprint(out_f)

