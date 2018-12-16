class DocumentEntity(object):
    id = ""
    owner_id = ""
    title = ""
    description = ""
    creation_time = ""
    update_time = ""
    is_signed = ""

    def serialize(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'title': self.title,
            'description': self.description,
            'creation_time': self.creation_time,
            'update_time': self.update_time,
            'is_signed': self.is_signed
        }
