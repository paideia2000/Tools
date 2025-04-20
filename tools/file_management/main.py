import pickle
import json

def create_file(PATH: str, CONTENT: str) -> None:
    """ create the file .txt """
    
    try:
        
        with open(PATH, "x") as x:
            x.write(CONTENT)
            print("\nThe file '(.TXT)' created  was succesfully.\n")
    
    except FileNotFoundError:
        print("\nThe file was not found.",)
        raise
    except FileExistsError as fex:
        print(f"\n- Into the function '{create_file.__name__}' - ", end="")
        raise fex

def write_json(PATH: str, CONTENT: str) -> None:
    """ create a file with the format .josn """
    
    try:
        
        with open(PATH, "w") as f:
            json.dump(CONTENT, f, ensure_ascii=False, indent=4)
            print("\nThe file '(.JSON)' created was succesfully.\n")
        
    except IsADirectoryError:
        print(f"\n- Into the function '{write_json.__name__}' - ", end="")
        raise
    except FileNotFoundError:
        print(f"\n- Into the function '{write_json.__name__}' - ", end="")
        raise

def write_bin(PATH: str, CONTENT: str) -> None:
    """ create a file with the format .bin """
    
    try:
        
        with open(PATH, "wb") as f:
            pickle.dump(CONTENT, f)
            print("\nThe file '(.BIN)' created was succesfully.\n")
        
    except IsADirectoryError as isdr:
        print(f"\n{isdr}\n")
    except FileNotFoundError as fnf:
        print(f"\nAn error ocurred {fnf}\n")
        
def read_txt(PATH_TXT: str) -> None:
    """ get the content to the file .txt """
    
    try:
        with open(PATH_TXT, "r") as f:
            content = f.read()
            print("\nThe content was extracted successfully\n")
        return content
            
    except IsADirectoryError as isa:
            raise isa

    except FileNotFoundError as fnf:
            raise fnf

def read_json(PATH_JSON) -> None:
    """ get the content to the file .json """

    try:
        with open(PATH_JSON, "r") as f:
            content = json.load(f)
            print("\nThe content was extracted successfully\n")
        return content
            
    except IsADirectoryError as isa:
            raise isa

    except FileNotFoundError as fnf:
            raise fnf

def read_bin(PATH_BIN) -> None:
    """ get the content to the file .json """

    try:
        with open(PATH_BIN, "rb") as f:
            content = pickle.load(f)
            print("\nThe content was extracted successfully\n")
        return content
            
    except IsADirectoryError as isa:
            raise isa

    except FileNotFoundError as fnf:
            raise fnf

def main():
    """ execute all functions """
    
    PATH_TXT = "tools/file_management/create_file.txt"
    PATH_JSON = "tools/file_management/create_file.json"
    PATH_BIN = "tools/file_management/create_file.bin"
    CONTENT = "Hello, World!"
    
    try:
        pass
        # create_file(PATH_TXT, CONTENT)
        # write_json(PATH_JSON, CONTENT)
        # write_bin(PATH_BIN, CONTENT)
        # read_txt(PATH_TXT)
        # read_json(PATH_JSON)
        # read_bin(PATH_BIN)
        
        
    except Exception as e:
        print(f"An error ocurred: {e}\n")

if __name__ == "__main__":
    main()