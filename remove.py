import os
import write
import read

def remove(new_object):
    if os.path.getsize("db.json") <= 0:
        print("There is no database to remove.")
    else:
        control = read.read_data()
        id = new_object["id"]
        category_id = new_object["category_id"]
        del control[category_id][id]
        write.write_data(control)