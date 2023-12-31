import os


def extract_number(input_string):
    parts = input_string.split('_')
    if len(parts) == 2 and parts[0] == "IMG" and parts[1].endswith(".JPG"):
        number_part = parts[1][:-4]
        if number_part.startswith("E"):
            number_part = number_part[1:]
        if number_part.isdigit() and len(number_part) == 4:
            return number_part
    return None


path = input("Enter the path to the folder with photo and video files in the following format: drive://folder\n")
os.chdir(path)
print("\n\n\nall_files:\n\n\n", os.listdir(path="."))
all_files = os.listdir(path=".")
print("all_files: ", len(all_files))
original_files, changed_files, other_files = [], [], []

extension = input("Enter file extension (JPG - for photos, PNG - for screenshots)\n")


for file_name in all_files:
    if file_name.startswith("IMG_E") and file_name.endswith("." + extension):
        changed_files.append(file_name)
    elif file_name.startswith("IMG_") and file_name.endswith("." + extension):
        original_files.append(file_name)
    else:
        other_files.append(file_name)

print("\n\n\n\n\n\t\tall_files:\n\n\n\n\n",
      "\n\n\noriginal_files\n\n\n", original_files, "\noriginal_files: ", len(original_files),
      "\n\n\nchanged_files\n\n\n", changed_files, "\nchanged_files: ", len(changed_files),
      "\n\n\nother_files\n\n\n", other_files, "\nother_files: ", len(other_files)
      )
print("\n")

for i in range(len(original_files)):
    number1 = extract_number(original_files[i])
    if original_files[i].endswith(".AAC"):
        os.remove(path=f"{path}\\IMG_{number1}.AAC")
        print(f"file IMG_{number1}.AAC deleted")
    print(f"file1: IMG_{number1}.{extension}")
    for j in range(len(changed_files)):
        number2 = extract_number(changed_files[j])
        print(f"file2: IMG_E{number2}.{extension}")
        if number1 == number2:
            os.remove(path=f"{path}\\IMG_{number1}.{extension}")
            print(f"file IMG_{number1}.JPG deleted")
