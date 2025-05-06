
def make_dict(LABEL: list[str], TOOLS: list[str] ) -> dict[str]:
    """ make a dictionary """
    
    if isinstance(LABEL, list) and isinstance(TOOLS, list):
        
        if len(LABEL) == len(TOOLS):
            
            return dict(zip(LABEL, TOOLS))
        else:
            raise ValueError("The variales must be the same len")
    
    else:
        raise ValueError("Please check the content of the variables")


def main():
    
    LABEL = ["leanguaje","package", "user"]
    TOOLS = ["python", "pandas", "rene"]

    try:
        new_dict: dict = make_dict(LABEL, TOOLS)

        print("\n",new_dict, "\n")

    except Exception as exp:
        print(f"\nAn error ocurred: {exp}\n")
        
if __name__=="__main__":
    main()




