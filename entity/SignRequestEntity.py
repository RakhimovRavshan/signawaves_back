class SignRequestEntity(object):
    document_id = ""
    user_id = ""
    is_signed = ""

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'is_signed': self.is_signed,
        }
