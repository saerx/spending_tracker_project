from db.run_sql import run_sql
from models.tag import Tag

#CREATE 

def save(tag):
    sql = "INSERT INTO tags (name, activated) VALUES (%s, %s) RETURNING id"
    values = [tag.name, tag.activated]
    results = run_sql(sql, values)
    id = results[0]["id"]
    tag.id = id
    return tag

#READ

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for result in results:
        tag = Tag(result["name"], result["id"], result["activated"])
        tags.append(tag)
    return tags

def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    tag = Tag(result["name"], result["id"], result["activated"])
    return tag


#UPDATE

def update(tag):
    sql = "UPDATE tags SET (name, activated) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.activated, tag.id]
    run_sql(sql, values)

def deactivate(id):
    sql = "UPDATE tags SET activated = %s WHERE id = %s"
    values = [False, id]
    run_sql(sql, values)

def activate(id):
    sql = "UPDATE tags SET activated = %s WHERE id = %s"
    values = [True, id]
    run_sql(sql, values)

# DELETE

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)