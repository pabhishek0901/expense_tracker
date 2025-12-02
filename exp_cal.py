from fastapi import APIRouter
import psycopg2
from fastapi.responses import JSONResponse

router=APIRouter()

def get_conn():
    conn=psycopg2.connect(db_url)
    return conn

@router.get('/emp')
def get_emp():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("select * from risk")
    rows=cur.fetchall()
    cur.close()
    conn.close()
    return JSONResponse(content=rows)

@router.get('/emp/{emp_id}')
def get_emp(emp_id):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("select * from risk where employee_id=%s",(emp_id,))
    rows=cur.fetchone()
    cur.close()
    conn.close()
    return JSONResponse(content=rows)

@router.post('/emp')
def get_emp(employee_id,name,salary,expenses,attendance,performance):
    saving=(int(salary)-int(expenses))
    risk=0
    if saving<=0:
        risk+=50
    elif saving<=(int(int(salary)/10)):
        risk+=25
    elif saving<=(int(int(salary)/5)):
        risk+=10
    elif saving>(int(int(salary)/5)):
        risk+=0

    if int(attendance)<70:
        risk+=20
    if int(performance)<70:
        risk+=30
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("insert into risk values (%s,%s,%s,%s,%s,%s,%s,%s)",(employee_id,name,salary,expenses,attendance,performance,saving,risk))
    conn.commit()
    cur.close()
    conn.close()
    return {"msg":"employee added"}

@router.delete('/emp/{employee_id}')
def del_emp(employee_id):
    conn=get_conn()
    cur=conn.cursor()
    query="delete from risk where employee_id=%s"
    value=(employee_id,)
    cur.execute(query,value)
    conn.commit()
    cur.close()
    conn.close()
    return {"msg":"deleted employee"}