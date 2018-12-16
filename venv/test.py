import pywaves as pw

pw.setNode(node = 'https://testnode2.wavesnodes.com', chain = 'testnet')
script = 'match tx { \n' + \
'  case _ => true\n' + \
'}'
myAddress = pw.Address(seed='kind expire cream settle tribe despair act endorse boss material lonely piano advice laundry visa')
pw.setOnline()
data = [{
        'type':'string',
        'key': 'test',
        'value':'testval'
        }]

print(myAddress.dataTransaction(data))

def send_data_transaction(seed, data):
    adr= pw.Address(seed=seed)
    pw.setOnline()
    adr.dataTransaction()
