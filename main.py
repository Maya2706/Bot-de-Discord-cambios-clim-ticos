# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random

description = """An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


situaciones = ["""🌞 Hace calor extremo por el cambio climático y quieres refrescarte en casa 
a) Prendes el aire todo el día ❄️
b) Usas un ventilador y abres ventanas 🌬️
c) Tomas mucha agua fría y te duchas rápido 🚿""", # 1:c BIEN

"""🚗 Tu ciudad tiene mucha contaminación ytienes que ir a la escuela
a) Vas caminando o en bici 🚴
b) Tomas el transporte público 🚌
c) Pides que te lleven en auto 🚗""", # 2:a BIEN

"""🍽️ Sobró comida del almuerzo y ya estás lleno
a) La tiras a la basura 🗑️
b) La guardas para otro día 🍱
c) La usas para compost 🌿""", # 3:b

"""🛒 Vas al supermercado a comprar frutas y verduras
a) Llevas tus bolsas reutilizables 👜
b) Aceptas bolsas plásticas en cada compra 🛍️
c) Usas una caja de cartón del local 📦""", # 4:a

"""💧 Te estás lavando los dientes con prisa
a) Dejas el agua corriendo 🚰
b) Cierras el grifo mientras te cepillas 🚿 
c) Llenas un vaso con agua para enjuagarte """, # 5:b

"""📱 Tu celular ya casi no funciona
a) Lo tiras a la basura 🗑️
b) Lo llevas a reciclar correctamente 🔋
c) Lo guardas en un cajón por si acaso 📦""", # 6:b BIEN

"""🍔 Es hora de almorzar
a) Comes carne todos los días 🍖
b) Comes legumbres o verduras algunas veces 🥗
c) Decides dejar la carne por completo sin planificar 🥦""", # 7:b  MAL (aparece lmal antes de responder)

"""🌳 En tu barrio hay un terreno vacío lleno de tierra
a) Plantas un árbol con tus amigos 🌱
b) Lo dejas igual total no es tuyo 😐
c) Tiras más basura ahí 🗑️""", # 8:a

"""💡 Una ampolleta de tu casa se fundió
a) Compras una LED de bajo consumo 💡
b) Compras una común porque es más barata 💸
c) No la reemplazas nunca 😴""", # 9:a # BIEN

"""Terminas una botella de plástico
a) La tiras con la basura común 🚮
b) La reciclas ♻️
c) La rellenas y reutilizas varias veces 💧""", # 10:c BIEN, MAL (Sale mal antes de responder)

"""🎮 Estás jugando y te llaman a cenar
a) Apagas la consola para ahorrar energía 🔌
b) La dejas encendida por si vuelves 🎮
c) Pones el modo suspensión 😴""", # 11:a BIEN

"""🧺 Vas a lavar ropa
a) Lavas con agua fría y cargas completas 🧼
b) Lavas pocas prendas con agua caliente ♨️
c) Lavas a mano con el grifo abierto 💧""", # 12:a BIEN, MAL(Sale mal antes de respoder)

"""🧃 Te da sed y quieres tomar jugo
a) Compras botellas individuales cada día 🧴
b) Tomas del envase grande 🧃
c) Usas un termo o botella reutilizable """, # 13:c BIEN

"""📚 Encuentras cuadernos viejos del año pasado
a) Los tiras directamente 🗑️
b) Reutilizas las hojas vacías ✏️
c) Los guardas sin tocarlos nunca 📦""", # 14:b MAL (Sale mal antes de responder)

"""🎁 Es el cumpleaños de tu mejor amigo
a) Envuelves el regalo con papel reciclado o una tela 🎀
b) Usas papel nuevo brillante 🎁
c) No haces regalo 😐""", # 15:a

"""🚿 Te das una ducha
a) Te duchas 20 minutos cantando 🎤
b) Te duchas en 5 minutos ⏱️
c) Llenas la bañera cada día 🛁""", # 16:b

"""💡 Vas a salir de tu pieza
a) Apagas la luz antes de irte 💡
b) Dejas la luz encendida por si vuelves 🔆
c) Prendes otra luz más brillante ✨""", # 17:a BIEN

"""📦 Recibes un paquete
a) Guardas la caja sin usarla jamás
b) La tiras a la basura común 🗑️
c) Reciclas la caja de cartón ♻️""", # 18:c BIEN

"""🌱 Quieres tener plantas
a) Siembras una planta nativa 🌿
b) Compras una planta rara que necesita mucha agua 💧
c) No riegas nunca tu planta para salvar agua""", # 19:a

"""🍽️ Queda comida del almuerzo
a) La tiras para no tener que guardarla 🗑️
b) La guardas para mañana 🍱
c) La dejas en la mesa hasta que se echa a perder""", # 20:b  MAL

"""📗 Tienes un trabajo del colegio
a) Le pides a alguien que te lo imprima 📚
b) Imprimes todo para leerlo 📄
c) Buscas información en línea sin imprimir 📱""", # 21:c BIEN

"""🚴 Quieres ir donde un amigo
a) Tomas un taxi para no usar tu auto 🚕
b) Pides que te lleven en auto 🚗
c) Vas en bici o caminando 🚶""", # 22:c

"""🛍️ Necesitas ropa
a) Compras solo lo que necesitas 👕
b) Te compras varias cosas porque estaban en oferta 🛒
c) Compras algo que no te gusta pero que es barato 💸""", # 23:a BIEN

"""🔌 Tu cargador queda enchufado
a) Pones otro cargador para no perderlo 🔋
b) Lo dejas enchufado todo el día ⚡
c) Lo desenchufas cuando no lo usas 🔌""", # 24:c 

"""🐶 Juegas con tu mascota
a) Compras un juguete nuevo cada semana 🛍️
b) Usas juguetes viejos o reciclados 🧶
c) Le das cosas que se rompen rápido 😕""", # 25:b BIEN

"""🧃 Quieres tomar un snack
a) Comes fruta 🍎
b) Compras un snack muy empaquetado 🍫
c) Abres dos snacks aunque no tengas tanta hambre""", # 26:a

"""🧹 Tu pieza está desordenada
a) Donas lo que ya no usas 🎁
b) Lo guardas todo en un cajón sin ordenarlo 📦
c) Lo tiras sin revisar nada 🗑️""", # 27:a BIEN

"""🎨 Haces un trabajo manual
a) Usas materiales que se rompen y debes reemplazar 🌪️
b) Compras materiales nuevos aunque tengas en casa ✂️
c) Reutilizas cartones y papeles 🎨""", # 28:c BIEN

"""📬 Te llegan folletos de publicidad
a) Los llevas al reciclaje ♻️
b) Los guardas por si acaso 📚
c) Los tiras con la basura común 🗑️""", # 29:a MAL

"""⚽ En tu recreo
a) Compras una bebida en el kiosco
b) Tomas agua en tu botella reutilizable 💧
c) Tomas bebidas energéticas porque te gustan 🍹"""] # 30:b MAL, BIEN

#               1   2    3    4    5    6    7    8    9   10   11   12    13  14   15    16  17    18  19   20   21   22   23   24   25   26   27   28   29   30
respuestas = ["c", "a", "b", "a", "b", "b", "b", "a", "a", "c", "a", "a", "c", "b", "a", "b", "a", "c", "a", "b", "c", "c", "a", "c", "b", "a", "a", "c", "a", "b"]

puntos = 0

@bot.command()
async def eco_juego(ctx):
    global puntos
    index = random.randint(0, len(situaciones)-1)
    pregunta = situaciones[index]
    respuesta = respuestas[index]
    await ctx.send(pregunta)
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    try:
        mensaje = await bot.wait_for("message", timeout=5, check=check)
    except Exception as e:
        print(e)
        await ctx.send("¡Se acabo el tiempo! ¡perdiste un punto de energía!")
        puntos -= 1
        return
    

    # Responde si tu respuesta está correcta o no y saca puntos

    if mensaje.content.lower() == respuesta:
        await ctx.send("Esa es la mejor opción! Ganaste un punto de energía")
        puntos += 1
    else:
        print(mensaje.content.lower())
        await ctx.send("Tu respuesta no es la mejor opcion... Perdiste un punto de energía")
        puntos -= 1
    
    # Dar un consejo

    consejos = ["Cierra la llave mientras te cepillas, ahorras hasta 6 litros por minuto.", "Reutiliza el agua que queda en la botella para regar plantas.", "Desenchufa cargadores cuando no los uses, sino seguirán gastando energía.", "Usa luz natural siempre que puedas, ilumina mejor y no cuesta energía", "Apaga el computador si no lo estás usando", "Las botellas de plástico se pueden reutilizar varias veces antes de reciclar.", "Evita imprimir si puedes leer algo en digital.", "Apaga la pantalla del computador cuando no lo uses.", "Desenchufa la TV cuando no la mires.", "Elige cuadernos reciclados si tienes opción.", "Una ampolleta LED usa hasta 80% menos energía que una tradicional.", "Reciclar una lata de aluminio ahorra la energía suficiente para usar tu computador por 3 horas.", "Usar termo en vez de botellas de plástico puede evitar más de 150 botellas al año.", "Un árbol grande puede absorber más de 20 kg de CO₂ al año.", "Una llave goteando puede perder más de 30 litros de agua al día.",]
    consejo = random.choice(consejos)
    if puntos == -2 or puntos == -8 or puntos == -15 or puntos == -25 :
        await ctx.send(f"""------------------------------------------------------------------------
{consejo}
------------------------------------------------------------------------""")
    

@bot.command()
async def puntos_E(ctx):
    await ctx.send(f"Tienes {puntos} puntos de energía")

@bot.command()
async def reset(ctx):
    global puntos
    puntos = 0
    await ctx.send("Tus puntos volvieron a 0.")



bot.run('TOKEN')
