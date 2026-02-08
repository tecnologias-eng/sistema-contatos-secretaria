import psycopg2

print("🔍 VERIFICAÇÃO DE BANCO DE DADOS")
print("=" * 50)

# TROQUE A SENHA ABAIXO PELA SUA SENHA DO POSTGRESQL
SENHA_POSTGRES = "postgres"  # ← ALTERE AQUI!

try:
    # Testar conexão com PostgreSQL
    print("1. Testando conexão com PostgreSQL...")
    
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password=SENHA_POSTGRES
    )
    
    print("   ✅ Conexão estabelecida!")
    
    cursor = conn.cursor()
    
    # Verificar se o banco existe
    print("\n2. Verificando banco 'solicitacoes_ti'...")
    cursor.execute("SELECT datname FROM pg_database WHERE datname = 'solicitacoes_ti';")
    resultado = cursor.fetchone()
    
    if resultado:
        print("   ✅ Banco 'solicitacoes_ti' EXISTE!")
        
        # Verificar encoding
        cursor.execute("""
            SELECT 
                datname,
                pg_encoding_to_char(encoding) as encoding,
                datcollate,
                datctype
            FROM pg_database 
            WHERE datname = 'solicitacoes_ti';
        """)
        
        info = cursor.fetchone()
        print(f"\n3. Informações do banco:")
        print(f"   📁 Nome: {info[0]}")
        print(f"   🔤 Encoding: {info[1]}")
        print(f"   🌍 Collate: {info[2]}")
        print(f"   🔡 Ctype: {info[3]}")
        
        # Verificar se há tabelas
        cursor.execute("""
            SELECT COUNT(*) 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_catalog = 'solicitacoes_ti';
        """)
        
        num_tabelas = cursor.fetchone()[0]
        print(f"\n4. Tabelas no banco: {num_tabelas}")
        
        if num_tabelas > 0:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                AND table_catalog = 'solicitacoes_ti'
                ORDER BY table_name;
            """)
            
            print("   📋 Lista de tabelas:")
            for tabela in cursor.fetchall():
                print(f"      - {tabela[0]}")
        
    else:
        print("   ❌ Banco 'solicitacoes_ti' NÃO existe!")
        print("\n   Próximo passo: Criar o banco de dados.")
    
    cursor.close()
    conn.close()
    
except psycopg2.OperationalError as e:
    print(f"\n❌ ERRO DE CONEXÃO: {e}")
    print("\n📌 Possíveis causas:")
    print("   1. PostgreSQL não está rodando")
    print("   2. Senha incorreta (atual: '" + SENHA_POSTGRES + "')")
    print("   3. Servidor não está em localhost:5432")
    
    # Verificar se PostgreSQL está rodando
    import os
    print("\n🔍 Verificando se PostgreSQL está ativo...")
    os.system('netstat -an | findstr :5432')
    
except Exception as e:
    print(f"\n❌ ERRO: {e}")

print("\n" + "=" * 50)
print("✅ Diagnóstico completo!")
