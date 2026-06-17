# Demonstracao-Z-API
Projeto simples para demonstração de sistema em python usando Z-API para automação no whatsapp

# Como iniciar
1. Crie um ambiente virtual:
```bash
python -m venv .venv
```
2. Ative o ambiente virtual:
```bash
.venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Crie um arquivo .env com as seguintes variáveis (igual há no arquivo .env.example):
```
ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=sua-anon-key
```
5. Execute o projeto:
```bash
python main.py
```