import os

def list_files_in_directory(directory_path):
    try:
        
        file_list = os.listdir(directory_path)

        
        files_only = [file for file in file_list if os.path.isfile(os.path.join(directory_path, file))]

        return files_only
    except FileNotFoundError:
        return None

def main():
    user_directory = input("Enter the directory path: ")

    
    files_list = list_files_in_directory(user_directory)

    if files_list:
        print("Files in the specified directory:")
        for file in files_list:
            print(file)
    else:
        print("Directory not found or no files in the specified location.")

if __name__ == "__main__":
    main()
