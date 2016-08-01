#import pymysql

#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', 
#                                              user='root', passwd="faustmeow", db='mysql')
# Connect to the database
#conn = pymysql.connect(host='localhost',
#                            user='root',
#                          password='faustmeow',
#                             db='mysql')
#cur = conn.cursor()
#cur.execute("USE scraping")
#cur.execute("SELECT * FROM pages")
#print(cur.fetchone())
#print(cur.fetchone())
#cur.close()
#conn.close()

###########################################
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='faustmeow', #faustmeow@163.com can contact me~ 
                             db='mysql',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
#with expression [as variable]:  
#    with-block  
#It is designed to replaced "try ... finally ..."
#"with" keyword like "if/while/try/for" followed ":"

#the __enter__ and __exit__ function is defined in the object of the expression

#this statement works like this:
#first, it would exe the function called "__enter__" and return an object
#the object would be catched by the variable which is behind the "as"
#then, it would exe the "with-blcok " 
#finally, no matter the expression exe is okay or not, it would exe "__exit__" function
try:
    with connection.cursor() as cursor:
        #so in this case, the connection.cursor() would create an cursor object and 
        #use it do something and close it(cur.close() ) no matter of the things it do having exceptions or not 
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        #so the email "webmaster@python.org" and password "very-secret" insert into the database

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()