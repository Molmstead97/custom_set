
class CustomSet:

   
    def __init__(self):
        self.custom_set = []

    
    def add(self, random_string: str):
        self.custom_set.append(random_string)

    def remove(self, random_string: str):
        self.custom_set.remove(random_string)
        
    def as_list(self):
        return list(self.custom_set)

    def clear(self):
        self.custom_set.clear()


def main():

    set = CustomSet()
   
    set.add("bingo bongo")
    set.add("mountain dew")
    set.add("top of the mornin to ya")

    try:
        set.remove("lkjsdf")
    except ValueError:
        print("\nThat's not in the set")
    
    print(set.as_list())

    set.clear()
    print(set.as_list())

    
         
if __name__ == "__main__":
    main()
