import os
import pickle


def save_obj(file_path , obj):

    try:

        dir_name = os.path.dirname(file_path)

        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "w") as f:
            pickle.dump(obj, f)

    except Exception as e:
        print(e)