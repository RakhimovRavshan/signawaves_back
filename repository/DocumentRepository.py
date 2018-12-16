from db.Connection import Connection
from entity.DocumentEntity import DocumentEntity
from entity.MainEntity import MainEntity


def find_all(address):
    conn = Connection.instance()
    print(address)

    db_res = conn.execute_query(
        "select id, owner_id, title, description, creation_time, update_time, is_signed from document t join sign_request s on s.document_id=t.id where s.user_id=%s",
        address)

    documents = []

    for row in db_res:
        documents.append(build_document_from_row(row))

    return documents


def find_all_outbox(address):
    conn = Connection.instance()
    print(address)

    db_res = conn.execute_query2(
        "select id, owner_id, title, description, creation_time, update_time, is_signed from document t join sign_request s on s.document_id=t.id where t.owner_id=%s",
        address)

    documents = []

    for row in db_res:
        documents.append(build_document_from_row(row))

    return documents


def find_by_id(id):
    conn = Connection.instance()

    db_res = conn.execute_query1("select * from document t where id=%s", id)
    row = db_res
    return build_document_from_row(row)


def find_counters(address):
    conn = Connection.instance()
    db_res = conn.execute_query3("select count(*) from sign_request where user_id=%s and is_signed=false", address)
    db_res1 = conn.execute_query3(
        "select count(*) from document t join sign_request s on s.user_id=t.owner_id where t.owner_id=%s and is_signed=false",
        address)
    db_res2 = conn.execute_query3("select count(*) from sign_request where user_id=%s", address)
    db_res3 = conn.execute_query3(
        "select count(*) from document t join sign_request s on s.user_id=t.owner_id where t.owner_id=%s ", address)
    counters = MainEntity()
    counters.income = db_res[0]
    counters.outcome = db_res1[0]
    counters.total_income = db_res2[0]
    counters.total_outcome = db_res3[0]
    #
    counters.serialize()
    print(counters)
    return counters.serialize()


def add_info_into_documents(id, owner_id, title, description):
    conn = Connection.instance()
    conn.execute_query4(
        "insert into document(id, owner_id, title, description,creation_time,update_time) values(%s,%s,%s,%s, current_date,current_date)", id, owner_id, title, description)


def add_info_into_sign_request(document_id1, user_id1):
    document_id=str(document_id1)
    user_id=str(user_id1)
    conn = Connection.instance()
    print(document_id, user_id)
    conn.execute_query5("insert into sign_request(document_id,user_id, is_signed) values(%s,%s, false)", document_id,
                        user_id)

def update_status(address, id):
    conn = Connection.instance()
    conn.execute_query6("update sign_request set is_signed=true where document_id=%s and user_id=%s", address, id)


def build_document_from_row(row):
    document = DocumentEntity()

    document.id = row[0]
    print(document.id)
    document.owner_id = row[1]
    document.title = row[2]
    document.description = row[3]
    document.creation_time = row[4]
    document.update_time = row[5]
    document.is_signed= row[6]

    return document.serialize()
