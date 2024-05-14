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


my_hash = Hash_Table(11);

my_hash.print_table()