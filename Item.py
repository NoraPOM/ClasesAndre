class Item
    def __init__(self, iditem, description, priority, assignad_to):
        self.iditem = iditem
        self.description = description
        self.priority = priority
        self.assigned_to = assigned_to

    def get_id(self):
        return self.iditem

    def get_description(self):
        return self.description
    
    def.set_description(self, description):
        self.description = description

    def get_priotity(self):
        return self.priotity

    def set_priority (self, priority):
        self.priority = priority

    def get_assigned_to(self):
        return self.assigned_to

    def set_assigned_to (self, user):
        self.assigned_to = user
