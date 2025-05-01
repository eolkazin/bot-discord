import discord
from discord.ext import commands

# Inicializa as permissões necessárias para o bot
intents = discord.Intents.all()

# Cria a instância do bot com prefixo de comando "/"
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print("Bot iniciado com sucesso.")


@bot.command()
async def ola(ctx: commands.Context):
    """Envia uma mensagem de saudação ao usuário."""
    await ctx.send(f"Olá {ctx.author.mention}, seja bem-vindo!")


@bot.command()
async def falar(ctx: commands.Context, *, texto: str):
    """Faz o bot repetir o texto informado pelo usuário."""
    await ctx.send(texto)


# Evento para boas-vindas a novos membros
@bot.event
async def on_member_join(member: discord.Member):
    canal_id = 999  # Substituir pelo ID real do canal de boas-vindas
    canal = bot.get_channel(canal_id)

    if canal:
        await canal.send(
            f"Seja bem-vindo(a) {member.mention} ao servidor {member.guild.name}!"
        )
    else:
        print("Canal de boas-vindas não encontrado.")


# Evento para resposta a reações em mensagens
@bot.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    await reaction.message.reply(
        f"{user.mention} reagiu com {reaction.emoji} na mensagem: {reaction.message.content}"
    )


@bot.command()
async def matematica(ctx: commands.Context, num1: str, num2: str, operacao: str):
    """
    Realiza uma operação matemática entre dois números.
    Operações disponíveis: soma, subtracao, multiplicacao, divisao.
    """
    try:
        n1, n2 = int(num1), int(num2)

        if operacao == "soma":
            resultado = n1 + n2
        elif operacao == "subtracao":
            resultado = n1 - n2
        elif operacao == "multiplicacao":
            resultado = n1 * n2
        elif operacao == "divisao":
            resultado = n1 / n2
        else:
            await ctx.send(
                "Operação inválida. Use: soma, subtracao, multiplicacao ou divisao."
            )
            return

        await ctx.send(f"O resultado da {operacao} entre {n1} e {n2} é: {resultado}")
    except ValueError:
        await ctx.send("Erro: Certifique-se de informar dois números válidos.")


# Inicia o bot
bot.run("TOKEN")
