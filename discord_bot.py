import config
import neo_processing

client = config.discord_init("nsh ")

@client.command()
async def LIST(ctx, command = "-p", page = 0):

    if command == "-p":
        neos = neo_processing.list_neos(page)

        neo = "\n".join(
        f"{neo['name']} | {neo['diameter_interval'][0]:.2f}m - {neo['diameter_interval'][1]:.2f}m"
        for neo in neos
        )

        await ctx.send("NAME | DIAMETER INTERVAL | MISS DISTANCE\n" + neo)

@client.command()
async def SELECT(ctx, date = 0, *, name):

    neos = neo_processing.select(name, date)

    if date > 0:
        date -= 1
        approaches = "\n".join(
            [f"{a}" for i, a in enumerate(neos[2][date])]
        )
    else:
        approaches = "\n".join(
            [f"{a}" for i, a in enumerate(neos[2])]
        )

    neo = f"NAME\n{neos[0]}\nDIAMETER INTERVAL (METERS)\n{neos[1][0]} - {neos[1][1]}\nAPPROACHES\n{approaches}"

    await ctx.send(neo)

@client.event
async def on_ready():
    
    config.message("Iniciado", "green", client.user.name, client.user.id)

client.run(config.token)
