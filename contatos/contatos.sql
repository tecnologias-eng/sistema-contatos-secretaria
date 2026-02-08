# Backup completo do banco
pg_dump -U postgres contatos > backup_completo_$(date +%Y%m%d).sql

# Backup apenas da estrutura
pg_dump -U postgres -s contatos > backup_estrutura.sql