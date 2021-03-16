import os

from flask import Flask, render_template, request, session, escape
#request 데이터 보낼때 필수
#session은 로그인 확인
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/display_all/')
def  display_con()->'html':
     result="sarah1"
     import mysql 
     import mysql.connector
     dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
     conn=mysql.connector.connect(**dbconfig)
     cursor=conn.cursor()
     SQL = '''SELECT * FROM login_t'''
     cursor.execute(SQL)
     alldata = cursor.fetchall()
    
     conn.disconnect()  
     return render_template('display_all.html',datapack=alldata)


@app.route('/')
def  home()->'html':
 return render_template('index.html')

@app.route('/login/')
def  login_con()->'html':
 return render_template('login.html')

@app.route('/mem_fix_edit/',methods=['POST'])
def  mem_fix_edit_con()->'html':
    id=request.form['hide']
    e_id=request.form['e_id']
    e_pw=request.form['e_pw']
    e_name=request.form['e_name']
    e_add=request.form['e_add']
    e_num=request.form['e_num']
    
    session['username']=id
    result = '%s' % escape(session['username'])

    if e_id :
     import mysql 
     import mysql.connector
     dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
     conn=mysql.connector.connect(**dbconfig)
     cursor=conn.cursor()
     SQL = '''UPDATE login_t SET u_id = %s WHERE u_id=%s'''
     cursor.execute(SQL,(e_id,result))
     conn.commit() 
     SQL = '''SELECT * FROM login_t WHERE u_id = %(u_id)s'''
     cursor.execute(SQL,({'u_id':e_id}))
     alldata = cursor.fetchall()
     conn.disconnect()
     
    elif e_pw:
     import mysql 
     import mysql.connector
     dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
     conn=mysql.connector.connect(**dbconfig)
     cursor=conn.cursor()
     SQL = '''UPDATE login_t SET u_pw = %s WHERE u_id=%s'''
     cursor.execute(SQL,(e_pw,result))
     conn.commit() 
     SQL = '''SELECT * FROM login_t WHERE u_id = %(u_id)s'''
     cursor.execute(SQL,({'u_id':result}))
     alldata = cursor.fetchall()
     conn.disconnect()
         
    elif e_name:
     import mysql 
     import mysql.connector
     dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
     conn=mysql.connector.connect(**dbconfig)
     cursor=conn.cursor()
     SQL = '''UPDATE login_t SET u_name = %s WHERE u_id=%s'''
     cursor.execute(SQL,(e_name,result))
     conn.commit() 
     SQL = '''SELECT * FROM login_t WHERE u_id = %(u_id)s'''
     cursor.execute(SQL,({'u_id':result}))
     alldata = cursor.fetchall()
     conn.disconnect()

    elif e_add:
     import mysql 
     import mysql.connector
     dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
     conn=mysql.connector.connect(**dbconfig)
     cursor=conn.cursor()
     SQL = '''UPDATE login_t SET u_add = %s WHERE u_id=%s'''
     cursor.execute(SQL,(e_add,result))
     conn.commit() 
     SQL = '''SELECT * FROM login_t WHERE u_id = %(u_id)s'''
     cursor.execute(SQL,({'u_id':result}))
     alldata = cursor.fetchall()
     conn.disconnect()        

    elif e_num:
     import mysql 
     import mysql.connector
     dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
     conn=mysql.connector.connect(**dbconfig)
     cursor=conn.cursor()
     SQL = '''UPDATE login_t SET u_pn= %s WHERE u_id=%s'''
     cursor.execute(SQL,(e_num,result))
     conn.commit() 
     SQL = '''SELECT * FROM login_t WHERE u_id = %(u_id)s'''
     cursor.execute(SQL,({'u_id':result}))
     alldata = cursor.fetchall()
     conn.disconnect()  
    return render_template('mem_fix.html',datapack=alldata)
#==========================================================================

@app.route('/mem_fix/',methods=['POST'])
def  mem_fix_con()->'html':
    no=request.form['no']
    import mysql 
    import mysql.connector
    dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
    conn=mysql.connector.connect(**dbconfig)
    cursor=conn.cursor()
    SQL = """ SELECT * FROM login_t WHERE no=%(no)s"""
    cursor.execute(SQL,({'no':no}))
    alldata = cursor.fetchall() 
    conn.disconnect()
    return render_template('mem_fix.html',datapack=alldata)

@app.route('/login_db/',methods=['POST'])
def  login_db_con()->'html':
  id=request.form['id']
  pw=request.form['pw']
  session['username']=id
  result = '%s' % escape(session['username'])                  
  import mysql 
  import mysql.connector
  dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
  conn=mysql.connector.connect(**dbconfig)
  cursor=conn.cursor()
  SQL = '''SELECT * FROM login_t WHERE u_id=%s and u_pw=%s'''
 #execute 라는 명령어는 자신이 실행한 SQL의 실행결과가 정상인지 아닌지를 알려줄수 있다.
 #그방법을 나중에알아내서 적어두세요!!(리턴결과)
  cursor.execute(SQL,(id,pw))
  alldata = cursor.fetchall()  #검색된 결과를 모두 가져와라! 그리고 res변수에 저장해줘라.
 #execute 실행결과가 뭔가 있다면 로그인 성공 없다면 그런유저 없음
 #만약 유저가 있다면 id를 세션변수에 저장한다
  if alldata:
      return render_template("login_db.html",datapack=alldata)   
  else:
        return render_template('login_fail.html')
#   if alldata:
#    pass
#   else:
#    return render_template('login_fail.html')
#   if session['user_id'] is None:
#     print("\n로그인중이 아닙니다\n")
#   else:
#    print("\n로그인중입니다\n")
#    
#   return render_template('login_db.html',)
#  else:
#   return render_template('login.html')
#==========================================================================
@app.route('/mem_reg_save/',methods=['POST'])
#여러분들이 직접 어떤 함수(담당자)를 만들어서 처리해야함!
#methods=['POST']가 있어야 데이터 포스트로 전달 기본적으로 'GET' method
def mem_reg_save()->'html':
    a=0
    p_id=request.form['id']
    p_pw=request.form['pw']
    p_name=request.form['name']
    p_add=request.form['add']
    p_pn=request.form['pn']
    import mysql 
    import mysql.connector
    dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
    conn=mysql.connector.connect(**dbconfig)
    cursor=conn.cursor()
    SQL = '''SELECT * FROM login_t'''
    cursor.execute(SQL)
    alldata = cursor.fetchall()
    
    for i in alldata:
     name=alldata[a][0]
     print(alldata[a][0])
     a = a + 1
     if name == p_id:
      print('name:',name)
      print('p_id:',p_id)
      
      return render_template('login_fail2.html')
     else: pass

     
    SQL = '''INSERT INTO login_t (u_id,u_pw,u_name,u_add,u_pn) VALUES(%s,%s,%s,%s,%s)'''
    cursor.execute(SQL,(p_id,p_pw,p_name,p_add,p_pn))
    conn.commit() #commit을 써야 저장!!
    conn.disconnect()
    return render_template('mem_reg_save.html',id=p_id, pw=p_pw, name=p_name, add=p_add, pn=p_pn)
#==========================================================================
@app.route('/mem_del/',methods=['POST'])
def mem_del_manage()->'html':
 no=request.form['no']
 print(id)
 import mysql
 import mysql.connector
 dbconfig= {'host':'localhost','user':'root','password':'','database':'member_db'}
 conn = mysql.connector.connect(**dbconfig)
 cursor=conn.cursor()
 SQL = """DELETE FROM login_t WHERE no=%(no)s"""
 cursor.execute(SQL,{'no':no})
 conn.commit()
 return render_template('mem_del.html')
#==========================================================================
@app.route('/mem_reg/')
def mem_reg_manage()->'html':
 return render_template('mem_register.html')

@app.route('/logout/',methods=['POST'])
def logout():
    p_id=request.form['u_id']
    session.clear()
    session['username']=p_id
    
    session.pop("username",None)
    return render_template('index.html')
 #==========================================================================
 #        
app.run(debug=True)