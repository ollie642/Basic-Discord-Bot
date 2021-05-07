import discord


# server id =

def read_token():
    with open("testtoken.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()


@client.event
async def on_member_update(before, after):  # Update for Nickname
    n = after.nick
    if n:
        if n.lower().count("ollie") > 0:
            last = before.nick
            if last:
                after.edit(nick=last)
            else:
                after.edit(nick="change name")


@client.event
async def on_member_join(member):  # When someone joins
    for channel in member.server.channels:
        if str(channel) == "🖕-welcome":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(msg):  # Message sent
    id = client.get_guild() #Input server ID
    channels = ["bot-commands", "admin-bot"]
    admin_commands = ["!ban"]
    # Embeds: 0-Commands, 1-
    embeds = []

    # !commands Embed
    embeds.append(discord.Embed(title="Commands:"))
    embeds[0].add_field(name="!hello", value="Says Hi", inline=False)
    embeds[0].add_field(name="!users", value="Returns the No. of Members", inline=False)
    embeds[0].add_field(name="!plug", value="Plugs twitch link", inline=False)
    embeds[0].add_field(name="!commands", value="Shows the full list of commands", inline=False)

    # !plug Embed
    embeds.append(discord.Embed(title="Links"))
    embeds[1].add_field(name="Twitch: ", value="https://www.twitch.tv", inline=False)
    embeds[1].add_field(name="Twitter: ", value="https://twitter.com", inline=False)

    if msg.author == client.user:  # If the msg is the bots msg
        return

    if str(msg.channel) in channels:  # If it occurred in 'channels' channel
        for command in admin_commands:
            if msg.content.find(command) != -1 and str(msg.channel) == "admin-bot":
                # Admin Commands
                if msg.content.find("!ban") != -1:
                    await msg.channel.send("okay")

        # General Commands
        if msg.content == "!hello":
            await msg.channel.send("Hi")
        elif msg.content == "!users":
            await msg.channel.send(f"""# of Members: {id.member_count}""")
        elif msg.content.find("!plug") != -1:
            await msg.channel.send(embed=embeds[1])
        elif msg.content.find("!commands") != -1:
            await msg.channel.send(embed=embeds[0])


client.run(token)
