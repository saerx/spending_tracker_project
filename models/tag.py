class Tag:
    def __init__(self, name, id=None, activated = True):
        self.name = name
        self.id = id
        self.activated = activated

    def mark_deactivated(self):
        self.activated = False

    def mark_activated(self):
        self.activated = True