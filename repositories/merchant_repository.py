from db.run_sql import run_sql
from models.merchant import Merchant

# CREATE

def save(merchant):
    sql = "INSERT INTO merchants (name, activated) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.activated]
    results = run_sql(sql, values)
    id = results[0]["id"]
    merchant.id = id
    return merchant

# READ 

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for result in results:
        merchant = Merchant(result["name"], result["id"], result["activated"])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT * FROM merchants where ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = Merchant(result["name"], result["id"], result["activated"])
    return merchant

# UPDATE

def update(merchant):
    sql = "UPDATE merchants SET (name, activated) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.activated, merchant.id]
    run_sql(sql, values)

def deactivate(id):
    sql = "UPDATE merchants SET activated = %s WHERE id = %s"
    values = [False, id]
    run_sql(sql, values)

def activate(id):
    sql = "UPDATE merchants SET activated = %s WHERE id = %s"
    values = [True, id]
    run_sql(sql, values)

# DELETE

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)