import pandas as pd
import os


def get_vocabulary():
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, "..", "files", "spanish.xlsx")

    if os.path.exists(file_path):
        try:
            with open(file_path, "r"):
                data = pd.read_excel(file_path)
                df = pd.DataFrame(data, columns=["foreign", "base"])
                vocabulary = df.values.tolist()
                return vocabulary
        except IOError as e:
            print(f"Error: Can't open the file. See more: {e}")
        except Exception as e:
            print(f"Error: Unexpected error. See more: {e}")
    else:
        print("Error: File not found")
