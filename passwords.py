import sqlite3

MASTER_PASSWORD = '123456'

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        );
         ''')
def menu():
    print("*********************************")
    print("* i : inserir nova senha         *")
    print("* l : listar serviçõs salvos     *")
    print("* r : recuperar uma senha        *")
    print("* s :                Sair        *")
    print("*********************************")

while True:
    menu()
    op = input("O que deseja fazer?")
    if op not in ['l', 'l', 'r', 's']:
        print("Opção inválida")
    continue

    if op == 's':
         break

conn.close()
