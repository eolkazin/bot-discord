![Logo do Bot](https://appmaster.io/pt/blog/discord-bot-como-cria-lo-e-adiciona-lo-ao-servidor)

# 🤖 Bot Discord com Python

Um bot simples usando `discord.py` com comandos úteis, eventos personalizados e lógica básica de interação com membros.

## 🚀 Funcionalidades

- Comando `/ola`: Envia uma saudação personalizada.
- Comando `/falar`: Faz o bot repetir qualquer texto.
- Comando `/matematica`: Realiza operações matemáticas básicas.
- Evento `on_member_join`: Dá boas-vindas automáticas.
- Evento `on_reaction_add`: Responde a reações nas mensagens.

## 🧠 Pré-requisitos

- Python 3.8+
- Biblioteca `discord.py`

```bash
pip install discord.py
```

# 🧾 Estrutura do Código

# Criação do bot com intents completas

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Evento ao iniciar o bot

@bot.event
async def on_ready():
print("Bot iniciado com sucesso.")

# Comandos

@bot.command()
async def ola(ctx): ...
@bot.command()
async def falar(ctx, \*, texto): ...
@bot.command()
async def matematica(ctx, num1, num2, operacao): ...

# Eventos personalizados

@bot.event
async def on_member_join(member): ...
@bot.event
async def on_reaction_add(reaction, user): ...

# 🧪 Exemplos de Uso

/ola

# ➜ Olá @usuário, seja bem-vindo!

/falar texto qualquer

# ➜ texto qualquer

/matematica 10 5 soma

# ➜ O resultado da soma entre 10 e 5 é: 15

### 🛠️ Configuração

Substitua "TOKEN" pelo token real do seu bot no final do código.

Altere canal_id = 999 para o ID real do canal de boas-vindas.

### 🔐 Segurança

Nunca compartilhe seu token do bot. Use variáveis de ambiente ou arquivos .env.

### 🧑‍💻 Autor

Desenvolvido por [LK] 🚀
Minas Gerais - BR
