from db.run_sql import run_sql
from models.budget import Budget

# CREATE

def save(budget):
    sql = "INSERT INTO budgets (amount) VALUES (%s) RETURNING id"
    values = [budget.amount]
    results = run_sql(sql, values)
    id = results[0]["id"]
    budget.id = id
    return budget

# READ

def select_all():
    budgets = []
    sql = "SELECT * FROM budgets"
    results = run_sql(sql)
    for result in results:
        budget = Budget(result["amount"], result["id"])
        budgets.append(budget)
    return budgets

def select(id):
    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    budget = Budget(result["amount"], result["id"])
    return budget

# UPDATE 

def update(budget):
    sql = "UPDATE budgets SET (amount) = (%s) WHERE id = %s"
    values = [budget.amount, budget.id]
    run_sql(sql, values)


# DELETE

def delete_all():
    sql = "DELETE FROM budgets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)