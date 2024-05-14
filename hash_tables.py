#It is recommended to have a prime number of addresses 
#reduces collisions
class Hash_Table:
    def __init__(self, size = 7):
        self.data_map = [None] * size;

    def __hash(self, key):
        my_hash = 0;
        for letter in key:
            #ord returns the unicode value of the alphabetical value
            my_hash = (my_hash + ord(letter)* 23) % len(self.data_map);
        return my_hash;

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val);

    def set_item(self, key, value):
        index = self.__hash(key);
        if self.data_map[index] == None:
            self.data_map[index] = [];
        self.data_map[index].append([key, value]);
        return True;

my_hash = Hash_Table(11);
my_hash.set_item("Emanuel", 36);
my_hash.set_item("Marika", 37);
my_hash.set_item("Cats", 12);


my_hash.print_table()