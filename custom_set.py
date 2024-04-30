
class CustomSet:

    def __init__(self):
        self.custom_set = []

    def add(self, item: str):
        if item not in self.custom_set:
            self.custom_set.append(item)

    def remove(self, item: str):
        if item not in self.custom_set:
            raise ValueError(f"{item} is not in the set")
        self.custom_set.remove(item)
        
    
    def as_list(self):
        return list(self.custom_set)

    def clear(self):
        self.custom_set.clear()


def main():

    set = CustomSet()
   
    set.add("bingo bongo")
    set.add("mountain dew")
    set.add("bingo bongo")

    print(set.as_list())
    
    set.remove("mountain dew")
    print(set.as_list())
    
    try:
        set.remove("lksdlkjf")
        
    except ValueError as error:
        print("\nError:", error)
    
    set.clear()
    print(set.as_list())

if __name__ == "__main__":
    main()
