import pyodbc

# SQL Server’ga ulanish
try:
    connection = pyodbc.connect(
        "DRIVER={msodbcsql.msi};"  # ODBC Driver nomi
        "SERVER=172.16.10.16;"                       # Server nomi yoki IP-manzili
        "DATABASE=L(murakkab so'rovlar);"                 # Ma'lumotlar bazasi nomi
        "UID=Durdona;"                      # Foydalanuvchi nomi
        "PWD=dona_0117;"                      # Parol
    )
    print("SQL Server’ga muvaffaqiyatli ulandingiz!")
    
    # So‘rovlar bilan ishlash
    cursor = connection.cursor()
    cursor.execute("SELECT @@VERSION;")  # SQL Server versiyasini tekshirish
    for row in cursor:
        print(row)

except pyodbc.Error as e:
    print(f"Ulanishda xatolik: {e}")

finally:
    if 'connection' in locals() and connection is not None:
        connection.close()
        print("SQL Server ulanishi yopildi.")
