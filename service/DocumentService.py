from repository import DocumentRepository
from waves import Waves


def get_documents(seed):
    waves = Waves('https://testnode2.wavesnodes.com', 'testnet', seed)
    address = waves.get_address_from_seed()
    print(str(address))
    return DocumentRepository.find_all(address)


def get_document(id):
    return DocumentRepository.find_by_id(id)

def sign_document(id, seed):
    waves = Waves('https://testnode2.wavesnodes.com', 'testnet', seed)
    address = waves.get_address_from_seed()
    transaction = [{
        'type': 'string',
        'key': 'file',
        'value': id
    }]
    waves.send_data_transaction(transaction)
    DocumentRepository.update_status(address, id)





def get_documents_outbox(seed):
    waves = Waves('https://testnode2.wavesnodes.com', 'testnet', seed)
    address = waves.get_address_from_seed()
    print(str(address))
    return DocumentRepository.find_all_outbox(address)


def get_counters(seed):
    waves = Waves('https://testnode2.wavesnodes.com', 'testnet', seed)
    address = waves.get_address_from_seed()
    return DocumentRepository.find_counters(address)


def send_file(data,seed):
    waves = Waves('https://testnode2.wavesnodes.com', 'testnet', seed)
    print(seed)
    tx_data = data.get("content").get("content")
    owner_id=waves.get_address_from_seed()
    title = data.get("file").get("title")
    description=data.get("file").get("description")
    user_id=data.get("recipients")[0]

    transaction = [{
        'type': 'string',
        'key': 'file',
        'value': tx_data
    }]
    print(transaction)
    tx_info=waves.send_data_transaction(transaction)
    print(tx_info)
    tx_id=tx_info.get("id")
    DocumentRepository.add_info_into_documents(tx_id, owner_id, title, description)
    DocumentRepository.add_info_into_sign_request(tx_id, user_id)
    return tx_id


def download_file(id):
    waves = Waves('https://testnode2.wavesnodes.com', 'testnet', seed)
    file = waves.get_transaction_by_id(id)
    file1=file.get("data")
    #to 64
    return file1

