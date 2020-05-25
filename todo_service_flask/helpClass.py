#day 4 - helper function to perform crud functions

import sqlite3

DB_PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = ' In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute('insert into items(items,status) values(?,?)', (item , NOTSTARTED))

        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ',e)
        return None