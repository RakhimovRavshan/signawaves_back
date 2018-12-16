class MainEntity(object):
    id = ""
    contact_id = ""
    contact_name = ""

    def serialize(self):
        return {
            'id': self.id,
            'contact_id': self.contact_id,
            'contact_name': self.contact_name
        }