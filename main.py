import discord
from discord import app_commands
import random
import asyncio
import requests
from discord.ext import commands
import sqlite3

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)
bot = client
auto_responders = {}

responses = [
    "The stars align in your favor... but they might be drunk.",
    "Ask me after my coffee break.",
    "My sources say... check your horoscope instead.",
    "Outlook hazy, try bribing me with cookies.",
    "Absolutely not! Just kidding, maybe.",
    "The answer is blowing in the wind... or maybe it's just gas.",
    "Don't count on it, unless you have a four-leaf clover handy.",
    "It's a possibility, but only if you wear mismatched socks.",
    "Better not tell you now, the suspense is more fun.",
    "Signs point to yes, but I wouldn't bet my life on it.",
    "Without a doubt... that I'm the best 8 Ball bot around.",
    "As I see it, the answer is hidden in a fortune cookie.",
    "The universe says... consult a psychic octopus.",
    "It's more likely than a unicorn stampede.",
    "My reply is no, but don't blame me, blame the algorithms.",
    "Outlook not so good, unless you change your question.",
    "Very doubtful, but stranger things have happened.",
    "Concentrate and ask again, I wasn't paying attention.",
    "The odds are ever in your favor... or so I've been told.",
    "Reply hazy, try asking a magic cat.",
    "I'm an 8ball and i don't want to deal with that question HAHAHAHAHAHAHAH",
    "Go to mars to know the answer",
    "I didn't go to mars but the answer is yes",
    "Ask your friend",
    "NO, I don't think so, no I do!!"

]

rps_choice = ['rock, paper, scissors']
cat_facts = [
    "Cats have a specialized vocalization called a 'hiss,' which they use to express fear or aggression.",
    "The Manx breed is known for its taillessness, although some Manx cats may have a short stump or full tail.",
    "Cats have a keen sense of hearing and can detect sounds as high as 64 kHz, well above the range of human hearing.",
    "The Siamese breed is known for its striking blue eyes, sleek coat, and vocal personality.",
    "Cats have a specialized vocalization called a 'growl,' which they use to warn off potential threats.",
    "The Birman breed is known for its striking blue eyes and colorpoint coat, similar to the Siamese.",
    "Cats have a highly developed sense of smell, with approximately 200 million scent receptors in their nasal cavity.",
    "The Maine Coon breed is known for its large size, tufted ears, and bushy tail.",
    "Cats have a unique grooming behavior called 'social grooming,' where they groom other cats as a sign of affection.",
    "The Ragdoll breed is known for its docile temperament and tendency to go limp when picked up.",
    "Cats have a specialized vocalization called a 'chatter,' which they use when observing birds or other prey.",
    "The Sphynx breed is known for its lack of fur and affectionate nature, making it a popular choice for allergy sufferers.",
    "Cats have a specialized vocalization called a 'trill,' which they use to greet their owners or other friendly cats.",
    "The Bengal breed is known for its distinctive spotted or marbled coat, resembling that of a wild leopard.",
    "Cats have a unique hunting behavior called 'play stalking,' where they mimic the movements of prey to hone their skills.",
    "The Scottish Fold breed is known for its distinctive folded ears, which give it an owl-like appearance.",
    "Cats have a specialized vocalization called a 'yowl,' which they use to seek attention or express frustration.",
    "The Persian breed is known for its long, luxurious coat and sweet, gentle temperament.",
    "Cats have a keen sense of balance and can walk along narrow ledges or perches with precision.",
    "The Devon Rex breed is known for its large ears, slender body, and short, wavy coat.",
    "Cats have a specialized vocalization called a 'purr,' which they use to express contentment or soothe themselves.",
    "The Norwegian Forest Cat breed is adapted to cold climates and has a thick, water-repellent double coat.",
    "Cats have a unique grooming behavior called 'allo-grooming,' where they groom other cats as a sign of social bonding.",
    "The Abyssinian breed is known for its sleek, muscular body and ticked coat, resembling that of a wildcat.",
    "Cats have a specialized vocalization called a 'mew,' which they use as a general form of communication.",
    "The Cornish Rex breed has a unique curly coat that is soft to the touch and sheds less than other breeds.",
    "Cats have a keen sense of sight and can see in low light conditions due to a reflective layer behind their retinas.",
    "The Russian Blue breed is known for its short, dense coat and striking green eyes.",
    "Cats have a specialized vocalization called a 'meow,' which they use to communicate with humans.",
    "The American Shorthair breed is known for its sturdy build, dense coat, and friendly disposition.",
    "Cats have a highly developed sense of taste and can detect bitter flavors more strongly than humans.",
    "The Chartreux breed is known for its dense, water-repellent fur and copper or gold eyes.",
    "Cats have a specialized vocalization called a 'chirp,' which they use to express excitement or anticipation.",
    "The Burmese breed is known for its affectionate nature and tendency to form strong bonds with its owners.",
    "Cats have a unique hunting strategy where they use their keen senses to ambush prey from a concealed position.",
    "The Oriental Shorthair breed is a close relative of the Siamese and is known for its sleek, muscular body and large ears.",
    "Cats have a specialized vocalization called a 'yowl,' which they use to seek attention or express frustration.",
    "The Exotic Shorthair breed is a cross between the Persian and the American Shorthair, resulting in a cat with a flat face and plush coat.",
    "Cats have a unique grooming behavior called 'social grooming,' where they groom other cats as a sign of affection.",
    "The Balinese breed is a longhaired variant of the Siamese and is known for its striking blue eyes and luxurious coat.",
    "Cats have a specialized vocalization called a 'growl,' which they use to warn off potential threats.",
    "The British Shorthair breed is known for its round face, dense coat, and sturdy build.",
    "Cats have a highly developed sense of smell, with approximately 200 million scent receptors in their nasal cavity.",
    "The Siamese breed is known for its striking blue eyes, sleek coat, and vocal personality.",
    "Cats have a specialized vocalization called a 'hiss,' which they use to express fear or aggression.",
    "The Manx breed is known for its taillessness, although some Manx cats may have a short stump or full tail.",
    "Cats have a keen sense of hearing and can detect sounds as high as 64 kHz, well above the range of human hearing.",
    "The Scottish Fold breed is known for its distinctive folded ears, which give it an owl-like appearance.",
    "Cats have a specialized vocalization called a 'growl,' which they use to warn off potential threats.",
    "The Birman breed is known for its striking blue eyes and colorpoint coat, similar to the Siamese.",
    "Cats have a highly developed sense of smell, with approximately 200 million scent receptors in their nasal cavity.",
    "The Maine Coon breed is known for its large size, tufted ears, and bushy tail.",
    "Cats have a unique grooming behavior called 'social grooming,' where they groom other cats as a sign of affection.",
    "The Ragdoll breed is known for its docile temperament and tendency to go limp when picked up.",
    "Cats have a specialized vocalization called a 'chatter,' which they use when observing birds or other prey.",
    "The Sphynx breed is known for its lack of fur and affectionate nature, making it a popular choice for allergy sufferers.",
    "Cats have a specialized vocalization called a 'trill,' which they use to greet their owners or other friendly cats.",
    "The Bengal breed is known for its distinctive spotted or marbled coat, resembling that of a wild leopard.",
    "Cats have a unique hunting behavior called 'play stalking,' where they mimic the movements of prey to hone their skills.",
    "The Scottish Fold breed is known for its distinctive folded ears, which give it an owl-like appearance.",
    "Cats have a specialized vocalization called a 'yowl,' which they use to seek attention"
]
dog_facts = [
    "A dog's sense of smell is about 10,000 to 100,000 times more acute than a human's.",
    "The Basenji is the only breed of dog that cannot bark.",
    "Dogs have three eyelids - an upper lid, a lower lid, and a third lid called the nictitating membrane.",
    "The world's smallest dog breed is the Chihuahua.",
    "The world's tallest dog breed is the Irish Wolfhound.",
    "The Saluki is the fastest dog breed, capable of running up to 43 mph.",
    "Dogs' noses are wet to help them absorb scent chemicals.",
    "Puppies are born deaf and blind.",
    "Dogs can dream, just like humans.",
    "Dogs can learn up to 250 words and gestures.",
    "Dogs can detect medical conditions like cancer and low blood sugar.",
    "The Beatles song 'A Day in the Life' has a high-pitched whistle at the end only dogs can hear.",
    "Dogs have a 'sixth sense' that can detect changes in the Earth's magnetic field.",
    "Dogs can see in shades of blue and yellow, but not red or green.",
    "Dogs' whiskers help them navigate in the dark.",
    "Dogs sweat through their paws.",
    "The oldest dog ever lived to be 29 years old.",
    "Dogs have a unique 'nose print' that is as individual as a fingerprint.",
    "The average lifespan of a dog is 10-13 years.",
    "Dogs can be trained to detect earthquakes, avalanches, and tsunamis.",
    "The Dalmatian was originally bred to run alongside horse-drawn carriages.",
    "The Newfoundland is a breed of dog known for its water rescue abilities.",
    "Dogs have a social hierarchy and communicate through body language and vocalizations.",
    "Dogs can be left-pawed or right-pawed.",
    "Dogs can get sunburned, especially on their noses and ears.",
    "Dogs can have allergies, just like humans.",
    "The largest litter of puppies ever recorded was 24.",
    "Dogs wag their tails to the right when they're happy and to the left when they're scared.",
    "Dogs were the first animals to be domesticated by humans.",
    "Dogs can be trained to detect explosives and drugs.",
    "Dogs can be trained to help people with disabilities.",
    "Dogs can be used for therapy and emotional support.",
    "Dogs can be trained to herd sheep and cattle.",
    "Dogs can be trained to hunt and retrieve game.",
    "Dogs can be trained to participate in agility competitions.",
    "Dogs can be trained to perform tricks and stunts.",
    "Dogs can be used for search and rescue missions.",
    "There are over 340 recognized dog breeds worldwide.",
    "Dogs' ears come in a variety of shapes and sizes, each with a purpose for capturing sound.",
    "Dogs' tails serve as a communication tool, expressing emotions and intentions.",
    "Dogs' teeth are designed for different functions: tearing, grinding, and gnawing.",
    "The Chow Chow and Shar-Pei are the only dog breeds with blue-black tongues.",
    "Dogs have a 'flehmen response' where they curl their upper lip to better analyze scents.",
    "Dogs have a natural instinct to chase moving objects.",
    "Dogs can be trained to play musical instruments, like piano or guitar.",
    "Dogs can be used to detect bed bugs and termites.",
    "The ancient Egyptians revered dogs and even mummified them alongside their owners.",
    "The term 'dog days of summer' refers to the hottest days of the year, named after the star Sirius (the 'Dog Star').",
    "The first dog in space was a Soviet dog named Laika.",
    "The United States has the highest dog population in the world.",
    "The most popular dog breed in the United States is the Labrador Retriever.",
    "The rarest dog breed in the world is the Norwegian Lundehund.",
    "Dogs' nails grow continuously and need to be trimmed regularly.",
    "Dogs have a 'dewclaw,' a vestigial toe on the inner side of their paws.",
    "Dogs can get car sick, just like humans.",
    "The oldest dog breed is the Saluki, dating back to ancient Egypt.",
    "The Puli is a Hungarian dog breed known for its corded coat that resembles dreadlocks.",
    "The Mexican Hairless Dog, or Xoloitzcuintli, is an ancient breed that was considered sacred by the Aztecs.",
    "Dogs have a ' Jacobson's organ' in their noses that helps them detect pheromones.",
    "The tallest dog ever recorded was a Great Dane named Zeus, standing at 44 inches tall at the shoulder.",
    "The smallest dog ever recorded was a Yorkshire Terrier named Sylvia, weighing just 4 ounces.",
    "Dogs have a natural instinct to bury bones and other valuables.",
    "The Australian Cattle Dog, or Blue Heeler, is known for its intelligence and herding abilities.",
    "The Greyhound is the fastest dog breed, capable of running up to 45 mph.",
    "Dogs have a unique way of cooling down by panting, which helps regulate their body temperature.",
    "Dogs have a 'stay apparatus' in their legs that allows them to lock their knees and stand for long periods without tiring.",
    "Dogs have a natural instinct to protect their pack, including their human family.",
    "Dogs can be trained to detect changes in blood sugar levels in people with diabetes.",
    "The Bloodhound has the most acute sense of smell of any dog breed.",
    "Dogs have a special gland called the anal gland that releases a unique scent for identification.",
    # ... (Add even more facts!)
]

@client.event  # Or wherever your bot's "on_ready" event is handled
async def on_ready():
    game_activity = discord.Game(name="/help")
    await client.change_presence(activity=game_activity)
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print("Syncing commands...")
    await client.tree.sync()
    print("Syncing complete.")


    print('------')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except discord.errors.Forbidden:
        print("Could not sync commands. Bot does not have permissions or the commands are in a guild.")

# Auto-kick trigger (on member join)
@bot.event
async def on_member_join(member):
    forbidden_words = [
        "nigga",
        "bitch",
        "porn",
        "gay",
        "sex",
        "nude"
    ]  # Sample bad words 
    for word in forbidden_words:
        if word in member.name.lower():
            await member.kick(reason="Forbidden word in username")
            await member.guild.system_channel.send(f"{member.mention} was kicked for having a forbidden word in their username.")
            return 

# Auto-kick trigger (on message sent)
@bot.event
async def on_message(message):
    forbidden_words = ["poop", "idiot", "dummy", "stupid"] 
    for word in forbidden_words:
        if word in message.content.lower():
            await message.author.kick(reason="Used forbidden word")
            await message.channel.send(f"{message.author.mention} was kicked for using a forbidden word.")
            return 

    await bot.process_commands(message)

@client.tree.command(name="ping", description="Returns the ping of the bot")
async def ping(interaction: discord.Interaction):
    embed = discord.Embed(title=":ping_pong: Pong!", description=f"Ping: {round(client.latency * 1000)}ms", color=discord.Color.red())
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="say", description="Sends a message in the current channel")
@app_commands.describe(message="The message that will be sent")
async def say(interaction: discord.Interaction, message: str):
    try:
        if interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("Message sent!", ephemeral=True)
            await interaction.channel.send(message)
        else:
            embed = discord.Embed(title=":x: Couldn't send message", description="Missing Permissions: Manage Messages")
            await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(title=":warning: WARNING", description="Missing Permissions")
        await interaction.response.send_message(embed=embed)
    except discord.HTTPException as e:
        embed = discord.Embed(title=":warning: Error", description=f"Error: {e}")
        await interaction.response.send_message(embed=embed)  # Send the embed

@client.tree.command(name="kick", description="Kick a member from the server.")
async def kick(interaction: discord.Interaction, member: discord.Member,*, reason: str = None):
    try:
        if not interaction.user.guild_permissions.kick_members:
            embed = discord.Embed(title=":x: Missing Permissions", description="You don't have Kick Members permssion", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        elif member.guild_permissions.administrator:
            embed = discord.Embed(title=f":x: Couldn't kick {member.name}", description="This member is an Administrator, I'm unable to kick them", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        elif member == interaction.guild.owner:
            embed = discord.Embed(title=":x: Couldn't kick server owner", description="The server owner cannot be kicked.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        elif member.guild_permissions >= interaction.user.guild_permissions:
            embed = discord.Embed(title=f":x: Couldn't kick {member.name}", description="You cannot kick someone who is equal to you or higher than you.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        else:
            if reason:
                await member.kick()
                embed = discord.Embed(title=f":white_check_mark: Kicked {member.name}", description=f"""Kicked {member.name}
reason: {reason}""", color=discord.Color.green())
                embed2 = discord.Embed(title="You have been kicked", description=f"""From: {interaction.guild.name}
Reason: {reason}""")
                await interaction.response.send_message(embed=embed)
                await member.send(embed=embed2)
            else:
                await member.kick()
                embed = discord.Embed(title=f":white_check_mark: Kicked {member.name}", description=f"""Kicked {member.name}
reason: None""", color=discord.Color.green())
                embed2 = discord.Embed(title="You have been kicked", description=f"""From: {interaction.guild.name}
Reason: None""")
                await member.send(embed=embed2)
                await interaction.response.send_message(embed=embed)
                embed = discord.Embed(
            title="--Warning Case--",
            color=discord.Color.blue()
        )
        embed.set_image(url=member.avatar.url)
        embed.add_field(name="Case", value="Kicking")
        embed.add_field(name=f"Mod/Admin", value=interaction.user.name)
        embed.add_field(name="Member", value=member.name)
        embed.add_field(name="Reason", value=reason)
        await interaction.guild.system_channel.send(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(title=":x: Missing Permissions", description="I don't have enough permissions to kick this member", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

    except discord.HTTPException:
        pass

@client.tree.command(name="warn", description="Warns a member")
@app_commands.describe(member="The member to be warned", reason="The reason for the warning")
async def warn(interaction: discord.Interaction, member: discord.Member, *, reason: str = None):
    try:
        if not can_warn(interaction, member):
            await send_error(interaction, get_error_embed(member, reason))
            return

        if reason:
            await send_success(interaction, get_success_embed(member, reason))
        else:
            await send_success(interaction, get_success_embed(member, "No reason"))

        await send_warning_dm(member, interaction.guild, reason)
        await send_warning_log(interaction, member, reason)

    except discord.Forbidden:
        await send_error(interaction, get_forbidden_embed())
    except discord.HTTPException:
        pass
    except Exception as e:
        print(f"Error: {e}")

def can_warn(interaction, member):
    if member == interaction.guild.owner:
        return False
    if member.guild_permissions.administrator:
        return False
    if member == client.user:
        return False
    if member == interaction.user:
        return False
    if member.bot:
        return False
    return True

def get_error_embed(member, reason):
    embed = discord.Embed(title=":x: Couldn't warn that member", description=f"You cannot warn {member.name}", color=discord.Color.red())
    return embed

def get_forbidden_embed():
    embed = discord.Embed(title=":x: Missing Permissions", description="I don't have permissions to warn members", color=discord.Color.red())
    return embed

def get_success_embed(member, reason):
    embed = discord.Embed(title=":white_check_mark: Successful", description=f"Warned {member.name} for {reason}", color=discord.Color.green())
    return embed

async def send_error(interaction, embed):
    await interaction.response.send_message(embed=embed)

async def send_success(interaction, embed):
    await interaction.response.send_message(embed=embed)

async def send_warning_dm(member, guild, reason):
    embed = discord.Embed(
        title=f":warning: WARNING FROM {guild.name.upper()}",
        description=f"You have been warned in {guild.name} for: {reason}",
        color=discord.Color.red()
    )
    await member.send(embed=embed)

async def send_warning_log(interaction, member, reason):
    embed = discord.Embed(
        title="--Warning Case--",
        color=discord.Color.blue()
    )
    embed.set_image(url=member.avatar.url)
    embed.add_field(name="Case", value="Warning")
    embed.add_field(name=f"Mod/Admin", value=interaction.user.name)
    embed.add_field(name="Member", value=member.name)
    embed.add_field(name="Reason", value=reason)
    await interaction.guild.system_channel.send(embed=embed)

@client.tree.command(name="add-role", description="Adds a role to a member")
async def addrole(interaction: discord.Interaction, member: discord.Member, role: discord.Role):
    try:
        if not interaction.user.guild_permissions.manage_roles:
            embed = discord.Embed(title=f":x: Couldn't add {role} to {member.name}", description="Reason: Missing Permissions", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        else:
            await member.add_roles(role)
            embed = discord.Embed(title=":white_check_mark: Successful", description=f"Added {role} to {member}", color=discord.Color.green())
            await interaction.response.send_message(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(title=":x: Forbidden", description="I don't have permissions to add roles to this member", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

    except discord.HTTPException as e:
      embed = discord.Embed(title=":x: An error occured", description=f"Error: {e}", color=discord.Color.red())
      await interaction.response.send_message(embed=embed)

@client.tree.command(name="create-role", description="Creates a role")
async def createrole(interaction: discord.Interaction, name: str):
    try:
        if not interaction.user.guild_permissions.manage_roles:
            embed = discord.Embed(title=":x: Couldn't create role", description="Reason: You don't have Manage Roles permission", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        else:
            await interaction.guild.create_role(name=name)
            embed = discord.Embed(title=f":white_check_mark: Successfully created new role", description=f"Name: {name}", color=discord.Color.green())
            await interaction.response.send_message(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(title=":x: Missing Permissions", description="I don't have permissions to create roles", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

    except discord.HTTPException as e:
        embed = discord.Embed(title=":x: An error occurred ", description=f"Error: {e}")
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="8ball", description="Asks the 8ball a question")
async def eight_ball(interaction: discord.Interaction, question: str):
    embed = discord.Embed(title="--8Ball's Answer--", description=f"""Question: {question}
Answer: {random.choice(responses)}""")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="rps", description="Plays Rock Paper Scissors with the bot.")
async def rps(interaction: discord.Interaction, choice: str):
    valid_choices = ["rock", "paper", "scissors"]

    if choice.lower() not in valid_choices:
        error_embed = discord.Embed(title="Invalid Choice!", description="Please choose rock, paper, or scissors.", color=discord.Color.red())
        await interaction.response.send_message(embed=error_embed)
        return

    client_choice = random.choice(valid_choices)

    if client_choice == choice.lower():
        result_embed = discord.Embed(title="-- RPS --", description=f"""
            User Choice: {choice}
            Bot Choice: {client_choice}
            It's a tie!
            """, color=discord.Color.gold())  # Use gold for a tie
    elif (choice.lower() == "rock" and client_choice == "scissors") or \
         (choice.lower() == "paper" and client_choice == "rock") or \
         (choice.lower() == "scissors" and client_choice == "paper"):
        result_embed = discord.Embed(title="-- RPS --", description=f"""
            User Choice: {choice}
            Bot Choice: {client_choice}
            You win! :tada:
            """, color=discord.Color.green())
    else:
        result_embed = discord.Embed(title="-- RPS --", description=f"""
            User Choice: {choice}
            Bot Choice: {client_choice}
            Bot wins! :robot:
            """, color=discord.Color.red())

    await interaction.response.send_message(embed=result_embed)

@client.tree.command(name="embed", description="Sends an embed with a specific color.")
async def embed(interaction: discord.Interaction, title: str, description: str, color: str, channel: discord.TextChannel = None):
    try:
        if not interaction.user.guild_permissions.manage_messages:
            raise commands.MissingPermissions(["manage_messages"])
        if color:
                color = discord.Color(int(color, 16)) 
        else:
            color = interaction.guild.me.color

        embed = discord.Embed(title=title, description=description, color=color)

        channel = channel or interaction.channel  
        await interaction.response.send_message("Embed sent!", ephemeral=True)
        await interaction.channel.send(embed=embed)

    except commands.MissingPermissions:
        await interaction.response.send_message("You don't have permission to use this command.")

    except commands.BadArgument as e:
        await interaction.response.send_message(str(e), ephemeral=True)

    except discord.Forbidden:
        await interaction.response.send_message("I don't have permission to send embeds in this channel.")

    except discord.HTTPException as e:
        await interaction.response.send_message(f"An error occurred: {e}")


@client.tree.command(name="ban", description="Bans a member")
async def ban(interaction: discord.Interaction, member: discord.Member, *, reason: str = None):
    try:
        if not interaction.user.guild_permissions.ban_members:
            embed = discord.Embed(title=":x: Missing Permissions", description="You don't have Ban Members permission", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member == interaction.guild.owner:
            embed = discord.Embed(title=":x: Couldn't Ban The Owner", description="I cannot ban the guild owner", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member.guild_permissions.administrator or member.guild_permissions.manage_guild:
            embed = discord.Embed(title=":x: Couldn't ban this member", description="This member is a Mod or Admin, I'm unable to do this action", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member == client.user:
            embed = discord.Embed(title=":x: Couldn't ban myself", description="I cannot ban myself", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member.bot:
            embed = discord.Embed(title=":x: Couldn't ban this bot", description="I cannot convert this bot into a member", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title="Member Banned", color=discord.Color.green())
            embed.add_field(name="Banned Member", value=f"{member.mention}", inline=False)
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(title="Error", description="I don't have permission to ban that member.", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="serverinfo", description="Get information about the server")
async def serverinfo(interaction: discord.Interaction):
    guild = interaction.guild

    embed = discord.Embed(
        title=guild.name,
        description=f"Server ID: {guild.id}",
        color=discord.Color.blue()
    )

    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)

    embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)

    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)

    if guild.banner:
        embed.set_image(url=guild.banner.url)

    await interaction.response.send_message(embed=embed)


@client.tree.command(name="user-info", description="Shows information about a specific member")
async def userInfo(interaction: discord.Interaction, *, member: discord.Member = None):
    try:
        if not member:
            user = interaction.user
            embed = discord.Embed(
                title=f"User Info: {user.name}",
                description=f"ID: {user.id}",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=user.display_avatar.url)  
            embed.add_field(name="Joined Server", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="Permissions", value=", ".join([perm[0] for perm in user.guild_permissions if perm[1]]), inline=False) # Improved formatting
            embed.add_field(name="Roles", value=", ".join([role.mention for role in user.roles[1:]]), inline=False)  # Improved formatting
            await interaction.response.send_message(embed=embed)
            
        elif member:
            embed = discord.Embed(
                title=f"User Info: {member.name}",
                description=f"ID: {member.id}",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=member.display_avatar.url) 
            embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="Permissions", value=", ".join([perm[0] for perm in member.guild_permissions if perm[1]]), inline=False) # Improved formatting
            embed.add_field(name="Roles", value=", ".join([role.mention for role in member.roles[1:]]), inline=False)  # Improved formatting
            embed.add_field(name="Nickname", value=member.nick if member.nick else "None", inline=False)
            embed.add_field(name="Status", value=str(member.status).title(), inline=False)

            await interaction.response.send_message(embed=embed)

    except discord.Forbidden:
        await interaction.response.send_message("I don't have permission to send messages in this channel.", ephemeral=True)

    except discord.HTTPException as e:
        embed = discord.Embed(title="Error", description=f"Error {e}")
        await interaction.response.send_message(embed=embed)

# ... (Your other bot setup, database connection, etc.)

@client.tree.command(name="temp-role-add", description="Adds a role and removes it after a specified time")
async def tempRoleAdd(interaction: discord.Interaction, member: discord.Member, role: discord.Role, duration: int, time_unit: str):
    """Adds a role to a member and removes it after a specified duration."""

    time_unit = time_unit.lower()
    valid_units = ["seconds", "minutes", "hours", "days"]
    
    if time_unit not in valid_units:
        await interaction.response.send_message(
            f"Invalid time unit. Please use one of: {', '.join(valid_units)}"
        )
        return
    
    conversion_factors = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400,
    }

    duration_seconds = duration * conversion_factors[time_unit]

    if not interaction.user.guild_permissions.manage_roles:
        embed = discord.Embed(
            title="Missing Permissions",
            description="You don't have Manage Roles permission",
            color=discord.Color.red()
            )
    else:
        await member.add_roles(role)
        embed = discord.Embed(
            title=":white_check_mark: Added role",
            description=f"Added {role} to {member.name}",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
    # Schedule the removal of the role
    await asyncio.sleep(duration_seconds)  # Wait for the specified duration

    try:
        await member.remove_roles(role)
        embed = discord.Embed(
            title=":white_check_mark: Removed role",
            description=f"Removed {role} from {member.name}",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=embed)
    except discord.NotFound:
        pass  # Handle if the member or role is no longer available

@client.tree.command(name="tempban", description="Bans a member for a specific time")
async def tempban(interaction: discord.Interaction, member: discord.Member, hours: int, reason: str):
    try:
        if not interaction.user.guild_permissions.ban_members:
            embed = discord.Embed(title=":x: Missing Permissions", description="You don't have Ban Members permission", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member == interaction.guild.owner:
            embed = discord.Embed(title=":x: Couldn't Ban The Owner", description="I cannot ban the guild owner", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member.guild_permissions.administrator or member.guild_permissions.manage_guild:
            embed = discord.Embed(title=":x: Couldn't ban this member", description="This member is a Mod or Admin, I'm unable to do this action", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member == client.user:
            embed = discord.Embed(title=":x: Couldn't ban myself", description="I cannot ban myself", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member.bot:
            embed = discord.Embed(title=":x: Couldn't ban this bot", description="I cannot convert this bot into a member", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title=f":white_check_mark: Banned {member.name}", description=f"Temporarily banned {member.name} for {reason}", color=discord.Color.green())
            await interaction.response.send_message(embed=embed)

            embed2 = discord.Embed(title=":warning: You have been banned", description=f"in {interaction.guild.name} for {reason}")
            await member.send(embed=embed2)

            async def unban_task():
                await asyncio.sleep(hours * 3600)  # Convert hours to seconds
                await member.unban(reason="Temporary ban expired")
                await interaction.followup.send(f"Unbanned {member.name}. Temporary ban expired.")

            asyncio.create_task(unban_task())

    except discord.Forbidden:
        embed = discord.Embed(
            title="Missing Permissions",
            description="I don't have permissons to ban this member",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="catfact", description="Tells you a random cat fact")
async def catFact(interaction: discord.Interaction):
    try:
        embed = discord.Embed(title="--Cat Fact--", description=random.choice(cat_facts), color=discord.Color.orange())
        await interaction.response.send_message(embed=embed)

    except discord.Forbidden as m:
        embed = discord.Embed(title="Missng Permissions", description=f"{m}", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

    except discord.HTTPException:
        embed = discord.Embed(title="Error", description=f"{discord.HTTPException}", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="avatar", description="Shows the avatar of a specific member")
async def avatar(interaction: discord.Interaction, member: discord.Member = None):
    try:
        member = member or interaction.user  # If no member is mentioned, use the author of the command.

        embed = discord.Embed(
            title=f"{member.name}'s Avatar",
            color=discord.Color.random()
        )
        embed.set_image(url=member.display_avatar.url)  # Set the image to the avatar URL
        await interaction.response.send_message(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(
            title="Missing Permissions",
            description="I don't have enough permissions to send embed or there is a bug",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    except discord.HTTPException as e:
        embed = discord.Embed(
            title="An Error Occurred",
            description=f"Error: {e}",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="servericon", description="Shows the server's icon")
async def serverIcon(interaction: discord.Interaction):
    guild_icon = interaction.guild.icon
    if guild_icon is None:
        embed = discord.Embed(title="No Server Icon", description="This server doesn't have a custom icon.", color=discord.Color.greyple())
    else:
        embed = discord.Embed(title=f"{interaction.guild.name}'s Icon", color=discord.Color.random())
        embed.set_image(url=guild_icon.url)  # Use the icon's URL property

    try:
        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        await interaction.response.send_message("I don't have enough permissions to send messages here.", ephemeral=True)
    except Exception as e:  # Catch more general errors
        print(f"Error in serverIcon command: {e}")  # Log the error for debugging
        await interaction.response.send_message("An unexpected error occurred.", ephemeral=True)

@client.tree.command(name="meme", description="Fetches a random meme from the internet.")
async def meme(interaction: discord.Interaction):
    try:
        response = requests.get("https://rapidapi.com/meme-generator-api-meme-generator-api-default/api/meme-generator")
        response.raise_for_status()  # Raise an exception if the request fails
        data = response.json()

        meme_title = data["title"]
        meme_url = data["url"]
        post_link = data["postLink"]

        embed = discord.Embed(title=meme_title, url=post_link, color=discord.Color.random())
        embed.set_image(url=meme_url)
        await interaction.response.send_message(embed=embed)

    except requests.exceptions.RequestException as e:
        error_embed = discord.Embed(title="Error Fetching Meme", description=f"An error occurred while fetching the meme: {e}", color=discord.Color.red())
        await interaction.response.send_message(embed=error_embed)

@client.tree.command(name="dogfact", description="Tells you a random dog fact")
async def dogFact(interaction: discord.Interaction):
    try:
        fact = random.choice(dog_facts)  
        while len(fact) > 2048:  # Discord embed description character limit
            fact = random.choice(dog_facts)

        embed = discord.Embed(
            title="🐾 Dog Fact 🐾",
            description=fact,
            color=discord.Color.orange()
        )

        # Optionally add a dog image:
        # embed.set_image(url="https://...")  # Replace with API call or image URL

        await interaction.response.send_message(embed=embed)
    except discord.HTTPException as e:
        errorEmbed = discord.Embed(
            title="⚠️ An Error Occurred",
            description=f"Oops! Something went wrong. Please try again later.\nError details: {e}",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=errorEmbed)

@client.tree.command(name="about", description="Get information about Z-Bot")
async def about(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🤖 About Z-Bot 🤖",
        description="Z-Bot is your trusty moderation assistant, keeping your Discord server safe and organized!",
        color=discord.Color.blue()  # Or choose your bot's color
    )

    embed.add_field(name="Creator", value="Robot", inline=True)  # Replace with your name
    embed.add_field(name="Version", value="2.4", inline=True)       # Update as needed
    
    # Emphasize moderation features:
    embed.add_field(name="Key Features", value="\n".join([
        "🛡️ Moderation:",
        "  • Muting/Unmuting",
        "  • Warning/Kicking/Banning",
        "  • Adding Roles",
        "  • Creating Roles",
        # Add more moderation features if applicable
        "\n Other:",
        "  • Random Dog Facts",  
        "  • Random Cat Facts",
        "  • Economy Commands"
        # List any additional non-moderation features
    ]), inline=False)
    
    embed.add_field(name="Commands", value="Use `/help` to see all of my commands!", inline=False)
    
    # Optionally, include additional information about your bot's moderation philosophy, etc.

    # Add an image or your bot's profile picture for a nice touch
    # embed.set_image(url="YOUR_BOT_IMAGE_URL") 

    await interaction.response.send_message(embed=embed)

# ... (Your bot setup code)

@client.tree.command(name="help", description="Provides information about the bot's commands")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Bot Help", 
        description="Here's a list of commands you can use:", 
        color=discord.Color.blue()
    )

    # Dynamically load commands from the tree
    for command in client.tree.get_commands():
        embed.add_field(
            name=f"/{command.name}", 
            value=command.description or "No description provided.", 
            inline=False
        )

    await interaction.response.send_message(embed=embed)



@client.tree.command(name="mute", description="Mutes the specified member")
@app_commands.describe(member="The member to mute", reason="The reason for muting")
@commands.has_permissions(moderate_members=True)
async def mute(interaction: discord.Interaction, member: discord.Member, *, reason: str = None):
    try:
        muted_role = discord.utils.get(interaction.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await interaction.guild.create_role(name="Muted")
            for channel in interaction.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False, speak=False)

        await member.add_roles(muted_role, reason=reason)

        # Create Embed
        embed = discord.Embed(title="Member Muted", color=discord.Color.red())
        embed.add_field(name="Member", value=member.mention, inline=False)
        embed.add_field(name="Moderator", value=interaction.user.mention, inline=False)
        embed.add_field(name="Reason", value=reason or "No reason provided", inline=False)

        await interaction.response.send_message(embed=embed)
    except Exception as e:
        embed = discord.Embed(title="Error", description=f"An error occurred: {e}", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="unmute", description="Unmutes the specified member")
@app_commands.describe(member="The member to unmute")
@commands.has_permissions(moderate_members=True)  # Only moderators can use this
async def unmute(interaction: discord.Interaction, member: discord.Member):
    # Check if user invoking the command is the server owner
    if interaction.user == interaction.guild.owner:
        pass  # Allow the owner to unmute anyone
    elif not interaction.user.guild_permissions.moderate_members:
        # Not a moderator or owner; deny access
        embed = discord.Embed(
            title="Insufficient Permissions", 
            description="You need the 'Moderate Members' permission to use this command.", 
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True) #Send only to the command user
        return 
 

    try:
        muted_role = discord.utils.get(interaction.guild.roles, name="Muted")

        # Check if the target member is actually muted
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            embed = discord.Embed(title="Member Unmuted", color=discord.Color.green())
            embed.add_field(name="Member", value=member.mention, inline=False)
            embed.add_field(name="Moderator", value=interaction.user.mention, inline=False)
        else:
            embed = discord.Embed(
                title="Not Muted", 
                description=f"{member.mention} is not currently muted.", 
                color=discord.Color.yellow()
            )
    except Exception as e:
        embed = discord.Embed(title="Error", description=f"An error occurred: {e}", color=discord.Color.red())

    await interaction.response.send_message(embed=embed)

@client.tree.command(name="lock", description="Locks the current channel.")
@app_commands.guild_only()
@app_commands.default_permissions(manage_channels=True)
async def lock_channel(interaction: discord.Interaction):
    channel = interaction.channel

    # Error Handling and Permission Checks
    if not interaction.user.guild_permissions.manage_channels:
        embed = discord.Embed(title="Permission Denied", description="You don't have permission to lock channels.", color=0xff0000) # Red
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    if not isinstance(channel, discord.TextChannel):
        embed = discord.Embed(title="Invalid Channel", description="This command can only be used in text channels.", color=0xff0000)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    try:
        overwrite = channel.overwrites_for(interaction.guild.default_role)
        if overwrite.send_messages is False:
            embed = discord.Embed(title="Already Locked", description="This channel is already locked.", color=0xffff00) # Yellow
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        overwrite.send_messages = False
        await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title="Channel Locked", description=f"Channel {channel.mention} is now locked.", color=0x00ff00) # Green
        await interaction.response.send_message(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(title="Missing Permissions", description="I don't have permission to lock this channel. Please check my permissions and role hierarchy.", color=0xff0000)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    except discord.HTTPException as e:
        embed = discord.Embed(title="Error", description=f"An error occurred while locking the channel: {e}", color=0xff0000)
        await interaction.response.send_message(embed=embed, ephemeral=True)



@client.tree.command(name="unlock", description="Unlocks the previously locked channel.")
async def unlock_command(interaction: discord.Interaction):
    # 1. Permissions Check
    if not interaction.user.guild_permissions.manage_channels:
        await interaction.response.send_message("You don't have permission to unlock channels.", ephemeral=True)
        return

    # 2. Retrieve Locked Channel
    # You'll need a way to store which channel was locked (e.g., in a database or a variable).
    # Here's an example assuming you store the locked channel ID in a global variable:
    global locked_channel_id
    if locked_channel_id is None:
        await interaction.response.send_message("No channel is currently locked.", ephemeral=True)
        return
    channel = client.get_channel(locked_channel_id)
    if channel is None:
        await interaction.response.send_message("The locked channel seems to be unavailable.", ephemeral=True)
        return

    # 3. Unlock the Channel
    await channel.set_permissions(interaction.guild.default_role, send_messages=True)
    
    # 4. Reset Locked Channel Variable
    locked_channel_id = None

    # 5. Send Confirmation
    await interaction.response.send_message(f"Channel {channel.mention} has been unlocked.") 

@client.tree.command(name="flipcoin", description="Confused which answer should you choose? Use this command now!")
async def flipCoin(interaction: discord.Interaction, message: str = None):
  """Flips a coin and displays the result in an embed"""
  choices = ["Heads", "Tails"]
  result = random.choice(choices)
  custom_message = f"{message} it landed on {result}" if message else f"It landed on {result}"
  embed = discord.Embed(
      description=custom_message
  )
  await interaction.response.send_message(embed=embed)

import discord
from discord.ext import tasks
from random import choice

@client.tree.command(name="giveawaycreate", description="Creates a giveaway")
@app_commands.describe(
    hours="The duration of your giveaway (in hours)",
    name="The giveaway's name",
    description="More info about your giveaway",
    channel="The channel where the giveaway will start and end"
)
async def giveawayCreate(interaction: discord.Interaction, hours: int, name: str, description: str, channel: discord.TextChannel):
    if not interaction.user.guild_permissions.manage_events:
        embed = discord.Embed(
            title=":x: Missing Permissions",
            description="You don't have `CREATE_EVENTS` permission",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
        return

    if hours <= 0:
        embed = discord.Embed(
            title=":x: Invalid Duration",
            description="Giveaway duration must be greater than 0 hours",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
        return

    try:
        # Create giveaway announcement embed
        embed = discord.Embed(
            title=f'--The "{name}" Giveaway Started--',
            description=f"Giveaway started, Who is going to be the winner???, More Info: {description}",
            color=discord.Color.blue()
        )
        giveaway_message = await channel.send(embed=embed)
        giveaway_message_id = giveaway_message.id

        # Send ephemeral message to user
        await interaction.response.send_message(f"Giveaway started in {channel.mention}! Duration: {hours} hours", ephemeral=True)

        # Schedule winner selection task
        async def pick_winner():
            await asyncio.sleep(hours * 3600)  # Convert hours to seconds
            winner = random.choice([m for m in channel.members if not m.bot])  # Exclude bots
            embed = discord.Embed(
                title="--Ended Giveaway",
                description=f"Winner: {winner.mention}",
                color=discord.Color.green()
            )
            await channel.send(embed=embed)
            # Consider sending DM to winner with prize details (if applicable)

        client.loop.create_task(pick_winner())

    except discord.Forbidden:
        embed = discord.Embed(
            title=":x: Missing Permissions",
            description="I don't have `MANAGE_EVENTS` permission",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    except discord.HTTPException as e:
        embed = discord.Embed(
            title=":x: Error",
            description=e,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title=":x: Error",
            description=f"An unexpected error occurred: {e}",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="deleterole", description="Deletes a role from the Guild")
async def deleteRole(interaction: discord.Interaction, role: discord.Role):
    if not interaction.user.guild_permissions.manage_roles:
        embed = discord.Embed(
            title=":x: Missing Permissions",
            description="You don't have `MANAGE_ROLES` permission",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    elif role.permissions.administrator:
        embed = discord.Embed(
            title=":x: Higher Permissions",
            description="This role has Administrator permission, I'm unable to do this action",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    else:
        try:
            await role.delete()
            embed = discord.Embed(
                title=f":white_check_mark: Deleted {role}",
                description=f"Deleted {role.name}\n Color: {role.color}",
                color=discord.Color.green()
            )
            await interaction.response.send_message(embed=embed)

        except discord.Forbidden:
            embed = discord.Embed(
                title=":x: Missing Permissions",
                description="I don't have permissions to delete roles",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)

        except discord.HTTPException as e:
            embed = discord.Embed(
                title=":x: Error",
                description=e,
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)

@client.tree.command(
    name="roleinfo",
    description="Displays Information About A Role"
)
async def roleinfo(interaction: discord.Interaction, role: discord.Role):
    embed = discord.Embed(
        title=f"--Information About {role.name}--"
    )
    embed.add_field(name="Member Count", value=len(role.members))
    embed.add_field(name="Color", value=str(role.color))
    embed.add_field(name="Permissions", value=str(role.permissions))
    embed.add_field(name="Permissions Amount", value=len(str(role.permissions)))
    if role.mentionable:
        embed.add_field(name="Mentionable", value="True")
    else:
        embed.add_field(name='Mentionable', value="False")
    if role.icon:
        embed.set_image(url=role.icon.url)
    else:
        embed.add_field(name="Icon", value="No Icon Found")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="invitecreate", description="Generates An Invite")
async def createInvite(interaction: discord.Interaction):
    invite = await interaction.channel.create_invite()
    embed = discord.Embed(
        title="Created Invite",
        description=f"Invite URL: {invite.url}",
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="unban", description="Unbans a member")
@app_commands.describe(member="The member to be unbanned", reason="The reason for them to be unbanned")
async def unban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    try:
        if not interaction.user.guild_permissions.ban_members:
            embed = discord.Embed(title=":x: Missing Permissions", description="You don't have unban Members permission", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member == interaction.guild.owner:
            embed = discord.Embed(title=":x: Couldn't unban The Owner", description="I cannot unban the guild owner", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member.guild_permissions.administrator or member.guild_permissions.manage_guild:
            embed = discord.Embed(title=":x: Couldn't unban this member", description="This member is a Mod or Admin, I'm unable to do this action", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member == client.user:
            embed = discord.Embed(title=":x: Couldn't unban myself", description="I cannot unban myself", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        elif member.bot:
            embed = discord.Embed(title=":x: Couldn't unban this bot", description="I cannot convert this bot into a member", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)

        else:
            await member.unban()
            if reason:
                embed = discord.Embed(
                    title=f":white_check_mark: Unbanned {member.name}",
                    description=f"Member: {member.name}\n Reason: {reason}"
                )
                await interaction.response.send_message(embed=embed)

            else:
                embed = discord.Embed(
                    title=f":white_check_mark: Unbanned {member.name}",
                    description=f"Member: {member.name}\n Reason: None",
                    color=discord.Color.green()
                )
                await interaction.response.send_message(embed=embed)
            await client.tree.add_command(unban)

    except discord.Forbidden:
        embed = discord.Embed(
            title=":x: Missing Permissions",
            description="I don't have permissions to unban this member",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)


    except discord.HTTPException as e:
        embed = discord.Embed(
            title=":x: Error",
            description=e,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="purge", description="Deletes messages in a specific channel")
async def purge(interaction: discord.Interaction, amount: int, target_channel: discord.TextChannel = None) -> None:

    # Check for MANAGE_MESSAGES permission
    if not interaction.user.guild_permissions.manage_messages:
        embed = discord.Embed(
            title=":x: Missing Permissions",
            description="You don't have the `MANAGE_MESSAGES` permission to use this command.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    # Validate message amount (1-100)
    if amount < 1 or amount > 100:
        embed = discord.Embed(
            title=":warning: Invalid Amount",
            description="Please enter a valid amount between 1 and 100 messages to delete.",
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)
        return

    # Determine the channel to purge
    channel = target_channel or interaction.channel  # Use specified channel or current channel

    # Send temporary message indicating deletion
    await interaction.response.send_message("Deleting messages...", ephemeral=True)

    try:
        # Perform the purge with proper error handling
        deleted = await channel.purge(limit=amount, before=interaction.message)  # Include before for efficiency
        await interaction.followup.send(f"Deleted `{len(deleted)}` messages in {channel.mention}", ephemeral=True)
    except discord.NotFound:
        await interaction.followup.send("Channel not found. Please ensure the channel exists and you have permission to manage messages in it.", ephemeral=True)
    except discord.HTTPException as e:
        await interaction.followup.send(f"An error occurred: {e}", ephemeral=True)

client.run("YOUR_BOT_TOKEN")