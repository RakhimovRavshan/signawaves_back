import pywaves as pw


class Waves(object):
    def __init__(self, node, chain, seed):
        self.node = node
        self.chain = chain
        self.seed = seed
        pw.setNode(node=self.node, chain=self.chain)

    def send_data_transaction(self, data):
        myaddress = pw.Address(seed=self.seed)
        return myaddress.dataTransaction(data)

    def get_transaction_by_id(self, id):
        return pw.tx(id)

    def get_public_key_from_seed(self):
        myaddress = pw.Address(seed=self.seed)
        return myaddress.publicKey

    def get_address_from_seed(self):
        print(self.seed)
        myaddress = pw.Address(seed=self.seed)
        return myaddress.address
