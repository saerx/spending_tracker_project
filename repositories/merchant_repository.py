from db.run_sql import run_sql
from models.merchant import Merchant

# CREATE

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING id"
    values = [merchant.name]
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
        merchant = Merchant(result["name"], result["id"])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT * FROM merchants where ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = Merchant(result["name"], result["id"])
    return merchant

# UPDATE

def update(merchant):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)

def change_active_status(merchant):
    if merchant.activated == True:
        sql = "UPDATE merchants SET activated = False WHERE id = %s"
        values = [merchant.id]
        run_sql(sql, values)
    else:
        sql = "UPDATE merchants SET activated = True WHERE id = %s"
    

# DELETE

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)