import sqlite3
db_name = "blog.db"
conn = None
cursor = None
def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
def close():
    cursor.close()
    conn.close()
def getCategories():
    open()
    cursor.execute('SELECT * FROM category')
    result = cursor.fetchall()
    close()
    return result
def getPosts():
    open()
    cursor.execute('SELECT * FROM post')
    result = cursor.fetchall()
    close()
    return result
def getPostsInCategories(id):
    open()
    cursor.execute("SELECT * FROM post WHERE category_id==?", id)
    result = cursor.fetchall()
    close()
    return result
def getCategoryByID(id):
    open()
    cursor.execute("SELECT name FROM category WHERE id==?", id)
    result = cursor.fetchone()
    close()
    return result
def addPosts(category_id, text):
    open()
    cursor.execute("INSERT INTO post (category_id, text) VALUES (?, ?)", [category_id, text] )
    conn.commit()
    close()
def getAmount(category_id):
    open()
    cursor.execute("SELECT count(id) FROM post WHERE category_id == ?", category_id)
    result = cursor.fetchone()
    close()
    return result
def deletePost(id):
    open()
    cursor.execute("DELETE FROM post WHERE id == ?", [id])
    conn.commit()
    close()