from db.run_sql import run_sql

from models.transaction import Transaction

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.budget import Budget
import repositories.budget_repository as budget_repository

import datetime

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
    
    return total

def get_decimalised_total():
    total = get_total()
    return decimalise(total)

def get_budget():
    budget = None
    try:
        budget = budget_repository.select_all()[0].amount
    except: 
        pass
    finally:
        return budget

def budget_alerts():
    budget = get_budget()
    if budget:
        dec_budget = decimalise(budget)
    total = get_total()
    if budget == None:
        return "You have not set a budget."
    elif budget > total >= 0.8*budget:
        return f"You are nearing your budget of {dec_budget}, of which {decimalise(budget-total)} remains."
    elif total > 2*budget:
        return f"You have greatly exceeded your budget of {dec_budget}."
    elif total > budget:
        return f"You have gone over your budget of {dec_budget} by {decimalise(total-budget)}."
    else:
        return f"Your budget is {dec_budget}, of which {decimalise(budget-total)} remains."


# LIST BY MERCHANTS

def select_for_merchants(merch_id):
    # import pdb; pdb.set_trace()
    merch_transactions = []
    sql = "SELECT * FROM transactions WHERE merchant_id = %s ORDER BY trans_time DESC"
    values = [merch_id]
    results = run_sql(sql, values)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["trans_time"], result["id"])
        merch_transactions.append(transaction)
    return merch_transactions

def get_merchant_total(merch_id):
    total = 0
    transactions = select_for_merchants(merch_id)
    for transaction in transactions:
        total += transaction.amount
    return decimalise(total)

# LIST BY TAGS

def select_for_tags(tag_id):
    # import pdb; pdb.set_trace()
    tag_transactions = []
    sql = "SELECT * FROM transactions WHERE tag_id = %s ORDER BY trans_time DESC"
    values = [tag_id]
    results = run_sql(sql, values)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["trans_time"], result["id"])
        tag_transactions.append(transaction)
    return tag_transactions

def get_tag_total(tag_id):
    total = 0
    transactions = select_for_tags(tag_id)
    for transaction in transactions:
        total += transaction.amount
    return decimalise(total)

# LIST BY MONTH

def select_for_months(year, month):
    # import pdb; pdb.set_trace()
    month_transactions = []
    if month == 12:
        month_2 = 1
        year_2 = int(year) + 1
    else:
        # difference = datetime.timedelta(months=1)
        month_2 = int(month) + 1
        year_2 = year
    first_date = f"{year}-{month}-01"
    second_date = f"{year_2}-{month_2}-01"
    sql = "SELECT * FROM transactions WHERE trans_time >= timestamp %s AND trans_time < timestamp %s"
    values = [first_date, second_date]
    results = run_sql(sql, values)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["trans_time"], result["id"])
        month_transactions.append(transaction)
    return month_transactions