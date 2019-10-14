import argparse #for parsing input argument [-f]
import csv #for parsing csv file
import mysql.connector #for connection with mysql database
import sys


#dbconnect: connects to database with provided host, user, pwd and dbname
def dbconnect(dbhost, dbuser, dbpasswd, dbname):
    try:
        dbcon = mysql.connector.connect(
            host = dbhost,
            user = dbuser,
            passwd = dbpasswd,
            database = dbname
        )

        return dbcon
    except mysql.connector.Error as err:
        print("Can't connect to Database: {}".format(err))
        sys.exit("No connection with database")


#checkIfTableExists: checking if table 'hotels' exists in database
def checkIfTableExists(dbcur):
    dbcur.execute("SELECT table_name FROM information_schema.tables where table_name  = 'hotels';")
    result = dbcur.fetchone()
    if result != None:
        print("Table 'Hotels' exists - OK. \n")
        return True
    else:
        print("Table 'Hotels' doesn't exists - NOT OK. \n")
        return False

#createTable: create table 'hotels' if that one doesn't exists in database
def createTable(dbcur):
    print("Creating table 'Hotels'.\n")
    dbcur.execute("""CREATE TABLE `hotels`(
                `code_hotel` varchar(10) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
                `name` tinytext COLLATE utf8_unicode_ci NOT NULL,
                `type_geo` char(2) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
                `code_geo` varchar(10) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
                `chain_code` char(3) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
                PRIMARY KEY (`code_geo`,`code_hotel`) )
                ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;""")
    print("Table 'Hotels' created.\n")

#parseCsv: parse input file [-f] , by default looking for "hotel_list.csv" in current directory.
#          Getting data from CSV file and validating against missing fields.
def parseCsv(dbcursor):
    parser = argparse.ArgumentParser() #for parsing -f argument
    parser.add_argument("-f", "--file", dest = "file", default="hotel_list.csv", help="CSV file")
    args = parser.parse_args()
    print "Input file: "+ args.file
    
    try:
        with open(args.file,'r') as f:
            csvreader = csv.DictReader(f, delimiter=";")
            print "Parsing "+args.file+" file started.\n" 
            for row in csvreader:
                missingItems = [k for k,v in row.iteritems() if v == ""] #empty values meant missing fields
                if missingItems:
                    print "### WARNING ###:  hotel "+row["code_hotel"]+" not imported because {} is missing.\n".format(','.join(missingItems)) #missing field, using list if more than one fields are missing
                else:
                    insertRow(row, dbcursor) #if data is complete, call function to update DB
    except EnvironmentError as err: #if file couldn't be open - file is missing etc.
        print("Error: {}".format(err)+'\n')
        
#insertRow: inserts data argument into DB, dbcur - database cursor
def insertRow(data, dbcur): 
    sql = "INSERT INTO hotels(code_hotel, name, type_geo, code_geo, chain_code) VALUES('{}','{}','{}','{}','{}');"
    print(sql.format(data["code_hotel"], data["name"],data["city_code"].split(".")[0], data["city_code"] ,data["chain_code"])+'\n')
    
    try:
        dbcur.execute(sql.format(data["code_hotel"], data["name"],data["city_code"].split(".")[0], data["city_code"] ,data["chain_code"])) #prefix of city code is used as a type_geo
    except mysql.connector.IntegrityError as err: #when data already exists in table - exception raised
        print("Error: {}".format(err)+'\n')



#main part
dbConnector = dbconnect('localhost','root','root', 'schema1') #connect to DB with provided data
dbCursor = dbConnector.cursor() #cursor needed to call queries on DB

if checkIfTableExists(dbCursor) == False: #if table not found in DB
    createTable(dbCursor) #create new table
parseCsv(dbCursor) #parse csv and update DB
dbCursor.close() #close cursor to DB




        
