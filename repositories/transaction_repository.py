from db.run_sql import run_sql

from models.transaction import Transaction

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

# CREATE
def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id, trans_time) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.trans_time]
    results = run_sql(sql, values)
    id = results[0]["id"]
    transaction.id = id
    return transaction

# READ
def select_all():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY trans_time DESC"
    results = run_sql(sql)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["trans_time"], result["id"])
        transactions.append(transaction)
    return transactions


def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = merchant_repository.select(result["merchant_id"])
    tag = tag_repository.select(result["tag_id"])
    transaction = Transaction(result["amount"], merchant, tag, result["trans_time"], result["id"])
    return transaction


# UPDATE

def update(transaction):
    sql = "UPDATE transactions SET (amount, merchant_id, tag_id, trans_time) = (%s, %s, %s, %s ) WHERE id = %s"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.trans_time, transaction.id]
    run_sql(sql, values)


# DELETE

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id): 
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#OTHER

def decimalise(num):
    return ("£%.2f" % num)
 
def get_total():
    total = 0
    transactions = select_all()
    for transaction in transactions:
        total += transaction.amount
    
    return decimalise(total)

# def list_by_month(x):
#     SELECT * FROM transactions WHERE trans_time >= timestamp '2020-09-01' AND trans_time < timestamp '2020-10-01'