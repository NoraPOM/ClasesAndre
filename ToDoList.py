import Item from Item
import User from User

class To_do_list:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        items.append(self.item)

    def delete_item(self, id_item):
        for i in self.items:
            if (i.get_id()  == id_item):
                items.remove(i)

    def get_item(self, id_item):
        for i in self.items:
            if (i.get_id()  == id_item):
                print("id:" + i.id)
                print("description: " + i.description)
                print("priority: " + i.priority)
                print("user name: " + i.assigned_to.name)
                print("user last_name: " + i.assigned_to.last_name)


    def show_items(self):
        for i in self.items:
            print("id:" + i.id)
            print("description: " + i.description)
            print("priority: " + i.priority)
            print("user name: " + i.assigned_to.name)
            print("user last_name: " + i.assigned_to.last_name)

def main():

if __name__ == "__main__":
    main()

