from logging import getLogger,config as logging_conf
logger_config = {}
logger_config['version'] = 1
logger_config['disable_existing_loggers'] = False
logger_config['formatters'] = {}
logger_config['formatters']['simple'] = {}
logger_config['formatters']['simple']['format'] = '%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s'
logger_config['formatters']['simple']['format'] = '%(asctime)s %(levelname)s: %(message)s'
logger_config['handlers'] = {}
logger_config['handlers']['consoleHandler'] = {}
logger_config['handlers']['consoleHandler']['class'] = 'logging.StreamHandler'
logger_config['handlers']['consoleHandler']['level'] = 'INFO'
logger_config['handlers']['consoleHandler']['formatter'] = 'simple'
logger_config['handlers']['consoleHandler']['stream'] = 'ext://sys.stdout'
logger_config['handlers']['fileHandler'] = {}
logger_config['handlers']['fileHandler']['class'] = 'logging.FileHandler'
logger_config['handlers']['fileHandler']['level'] = 'DEBUG'
logger_config['handlers']['fileHandler']['formatter'] = 'simple'
logger_config['handlers']['fileHandler']['filename'] = '/log/custom/console.log'
logger_config['handlers']['discord'] = {}
logger_config['handlers']['discord']['class'] = 'logging.FileHandler'
logger_config['handlers']['discord']['level'] = 'DEBUG'
logger_config['handlers']['discord']['formatter'] = 'simple'
logger_config['handlers']['discord']['filename'] = '/log/custom/console.log'
logger_config['handlers']['discord.http'] = {}
logger_config['handlers']['discord.http']['class'] = 'logging.FileHandler'
logger_config['handlers']['discord.http']['level'] = 'DEBUG'
logger_config['handlers']['discord.http']['formatter'] = 'simple'
logger_config['handlers']['discord.http']['filename'] = '/log/custom/console.log'
logger_config['loggers'] = {}
logger_config['loggers']['__main__'] = {}
logger_config['loggers']['__main__']['level'] = 'DEBUG'
logger_config['loggers']['__main__']['handlers'] = ['consoleHandler', 'fileHandler']
logger_config['loggers']['__main__']['propagate'] = False
logger_config['loggers']['same_hierarchy'] = {}
logger_config['loggers']['same_hierarchy']['level'] = 'DEBUG'
logger_config['loggers']['same_hierarchy']['handlers'] = ['consoleHandler', 'fileHandler']
logger_config['loggers']['same_hierarchy']['propagate'] = False
logger_config['loggers']['lower.sub'] = {}
logger_config['loggers']['lower.sub']['level'] = 'DEBUG'
logger_config['loggers']['lower.sub']['handlers'] = ['consoleHandler', 'fileHandler']
logger_config['loggers']['lower.sub']['propagate'] = False
logger_config['root'] = {}
logger_config['root']['level'] = 'INFO'
logging_conf.dictConfig(logger_config)
logger = getLogger(__name__)
logger.info('Init')

import os,sys
import traceback
import discord
import datetime
import json
import fasteners
import inspect
from dotenv import load_dotenv
from mcrcon import MCRcon

def file_put_contents(filepath: str = None, writedata: str = None):
    if os.path.exists(filepath):
        if not os.path.isfile(filepath):
            raise FileExistsError
        with fasteners.InterProcessLock(filepath):
            logger.debug(f'Locked by {os.getpid()}')
            with open(filepath, mode='w') as f:
                f.write(writedata)
        return True
    else:
        return False

logger.info(f'Pwd: {os.getcwd()}')

load_dotenv()
TOKEN_DISCORD=os.getenv('TOKEN_DISCORD', '')
if len(TOKEN_DISCORD) > 0:
    logger.info('Load & set the token DISCORD')
else:
    logger.error('Require the token.discord')
    raise ValueError('Require the token.discord')

CREDENTIAL_MCRCON={
    'addr': os.getenv('ADDRESS_MCRCON', 'localhost'),
    'port': os.getenv('PORTNUM_MCRCON', 25575),
    'pass': os.getenv('PASSWORD_MCRCON', 'minecraft'),
}

FILES_CONFIG={
    'discord-apps-config.json': os.getenv('FILES_CONFIG_DISCORD_APPS_CONFIG', 'discord-apps-config.json'),
}

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.typing = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

template = {
    "color": {
        'success': 0x008000,
        'failure': 0xFF0000,
        'caution': 0xFFFF00,
        'none': 0x000000,
    },
    "discord-apps-config.json": {
        "{discord-user-id}": {
            "name": "{discord-user-name}",
            "{discord-guild-id}":{
                "name": "{discord-guild-name}",
                "{discord-channel-id}":{
                    "name": "{discord-channel-name}",
                    "userPreferences": {
                        "ephemeral": True
                    }
                }
            }
        }
    }
}

configuration = {}

logger.info('Loading config files: {}'.format(
    FILES_CONFIG['discord-apps-config.json'],
))
if os.path.exists(FILES_CONFIG['discord-apps-config.json']):
    if not os.path.isfile(FILES_CONFIG['discord-apps-config.json']):
        logger.error('Not File Exists')
        raise FileExistsError
    with open(FILES_CONFIG['discord-apps-config.json'], mode='r') as f:
        try:
            configuration |= {'discord-apps-config.json': json.load(f)}
            logger.info('Loaded')
            logger.debug(configuration.get('discord-apps-config.json'))
        except json.JSONDecodeError as e:
            logger.error(e)
else:
    logger.warning('File Not Exists. Creating file from template.')

    configuration |= {'discord-apps-config.json': {}}
    with open(FILES_CONFIG['discord-apps-config.json'], mode='w') as f:
        try:
            json.dump(template['discord-apps-config.json'], fp=f)
            logger.info('Created file from template.')
            logger.debug(configuration.get('discord-apps-config.json'))
        except Exception as e:
            logger.error(f'File write error: {e}')

@client.event
async def on_ready():
    logger.info('Connect OK ID:{} NAME:{}'.format(client.user.id, client.user.name))
    logger.info('Invite link: https://discord.com/oauth2/authorize?client_id={}'.format(client.user.id))

    # アクティビティステータスを設定
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.CustomActivity(name=client.user.name)
    )
    logger.info('Change presence status to {}'.format(discord.Status.online))
    logger.info('Change presence activity to {}'.format(discord.CustomActivity(name=client.user.name)))

    # アクティビティステータスを設定
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.CustomActivity(name='/mcrcon:help')
    )
    logger.info('Change presence status to {}'.format(discord.Status.online))
    logger.info('Change presence activity to {}'.format(discord.CustomActivity(name='/mcrcon:help')))

    # スラッシュコマンドを同期
    try:
        await tree.sync()
    except discord.HTTPException as e:
        logger.warning(e)
        logger.error(traceback.format_exc())
    except discord.app_commands.CommandSyncFailure as e:
        logger.warning(e)
        logger.error(traceback.format_exc())
    except discord.Forbidden as e:
        logger.warning(e)
        logger.error(traceback.format_exc())
    except discord.MissingApplicationID as e:
        logger.warning(e)
        logger.error(traceback.format_exc())
    except discord.app_commands.TranslationError as e:
        logger.warning(e)
        logger.error(traceback.format_exc())
    logger.info('Synced slash commands.')

    # レイテンシ測定
    logger.info(f'Latency: {round(client.latency*1000)}ms')

    # 起動完了
    logger.info('Ready')

@client.event
async def on_connect():
    logger.info('Connected')

@client.event
async def on_disconnect():
    logger.warning('Disconnected')

@client.event
async def on_resumed():
    logger.info('resumed')

@client.event
async def on_error(event, args, kwargs):
    logger.error('on_error: {}'.format(
        event,
    ))
    logger.error(sys.exc_info())

@client.event
async def on_typing(channel, user, when):
    logger.info('on_typing: channel:{} user:{} when:{}'.format(
        channel.id,
        user.id,
        when,
    ))

@client.event
async def on_message_delete(message):
    logger.info('on_message_delete')

@client.event
async def on_bulk_message_delete(message):
    logger.info('on_bulk_message_delete')

@client.event
async def on_message_edit(before, after):
    # 送信者が自分自身である場合は弾く
    if after.author.id == client.user.id:
        return
    # 送信者がbotである場合は弾く
    if after.author.bot:
        logger.warning('Message author is BOT: {}({})'.format(
            after.author.name,
            after.author.id,
        ))
        return
    # テキストチャンネルのみ処理
    if after.channel.type != discord.ChannelType.text:
        logger.warning('Channel type is not text channel')
        return
    # メッセージ受取り
    logger.info('on_message_edit author: {}({}) guild:{} channel:{}'.format(
        after.author.name,
        after.author.id,
        after.guild.id,
        after.channel.id,
    ))
    logger.debug('on_message_edit author: {}({}) guild:{}({}) channel:{}({}) content:{}'.format(
        after.author.name,
        after.author.id,
        after.guild.id,
        after.guild.name,
        after.channel.id,
        after.channel.name,
        after.content,
    ))

@client.event
async def on_message(message):
    # 変数初期化
    timeu=datetime.datetime.now(datetime.timezone.utc)
    title=None
    descr=None
    color=template['color']['none']
    url=None
    text=None

    # 送信者が自分自身である場合は弾く
    if message.author.id == client.user.id:
        return
    # 送信者がbotである場合は弾く
    if message.author.bot:
        logger.warning('Message author is BOT: {}({})'.format(
            message.author.name,
            message.author.id,
        ))
        return
    # テキストチャンネルのみ処理
    if message.channel.type != discord.ChannelType.text:
        logger.warning('Channel type is not text channel')
        return

@tree.command(name="bothelp",description="コマンドヘルプを表示")
async def help(ctx: discord.Interaction):
    try:
        logger.debug('Call from name:{}({}) command:{} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            ctx.guild.name,
            ctx.channel.name,
        ))

        title = 'Usage'
        description = ''
        description += '`/bothelp`\n'
        description += 'コマンドのヘルプを表示\n'
        description += 'ephemeral: True\n'
        description += '`/ping`\n'
        description += 'レイテンシを計測\n'
        description += 'ephemeral: True\n'
        description += '---\n'
        description += '`/banlist`\n'
        description += 'サーバーのブラックリストを表示\n'
        description += 'ephemeral: True\n'
        description += '`/datapack`\n'
        description += '存在するデータパック、または有効化されているデータパックの一覧を表示\n'
        description += 'ephemeral: True\n'
        description += '`/help`\n'
        description += 'コマンドのヘルプを表示\n'
        description += 'ephemeral: True\n'
        description += '`/list`\n'
        description += '現在サーバーに接続しているプレイヤーのリストを表示\n'
        description += 'ephemeral: True\n'
        description += '`/say`\n'
        description += 'サーバー上のすべてのプレイヤーにメッセージを送信\n'
        description += 'ephemeral: True\n'
        color = template['color']['none']
        logger.info(description)
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)
    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

@tree.command(name="ping", description="レイテンシを計測")
async def ping(ctx: discord.Interaction):
    try:
        logger.debug('Call from name:{}({}) command:{} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            ctx.guild.name,
            ctx.channel.name,
        ))

        title = 'Latency'
        description = f'Pong! {round(client.latency*1000)}ms'
        color = template['color']['caution']
        logger.info(description)
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)
    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

@tree.command(name="discord_config", description="Discordに関連する設定を表示・変更")
@discord.app_commands.describe(args1="設定項目名")
@discord.app_commands.describe(args2="設定値")
async def discord_config(ctx: discord.Interaction, args1: str = None, args2: str = None):
    try:
        logger.debug('Call from name:{}({}) command:{} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            ctx.guild.name,
            ctx.channel.name,
        ))

        try: 
            configuration['discord-apps-config.json'][str(ctx.user.id)][str(ctx.guild.id)][str(ctx.channel.id)]['userPreferences']
            logger.info('Load configuration.get({}).get({}).get({}).get({}).get({})'.format(
                'discord-apps-config.json',
                str(ctx.user.id),
                str(ctx.guild.id),
                str(ctx.channel.id),
                'userPreferences',
            ))
        except KeyError:
            configuration['discord-apps-config.json'][str(ctx.user.id)] = {
                'name': ctx.user.name,
                str(ctx.guild.id): {
                    'name': ctx.guild.name,
                    str(ctx.channel.id): {
                        'name': ctx.channel.name,
                        'ephemeral': True,
                    }
                }
            }
            logger.warning(f'KeyError: {inspect.currentframe().f_back}')
            file_put_contents(FILES_CONFIG['discord-apps-config.json'], json.dumps(configuration['discord-apps-config.json'], indent=2))

        if args1 is None and args2 is None:
            result = configuration['discord-apps-config.json'][str(ctx.user.id)][str(ctx.guild.id)][str(ctx.channel.id)]
        elif args1 is not None and args2 is None:
            try:
                result = configuration['discord-apps-config.json'][str(ctx.user.id)][str(ctx.guild.id)][str(ctx.channel.id)][args1]
            except KeyError:
                result = configuration['discord-apps-config.json'][str(ctx.user.id)][str(ctx.guild.id)][str(ctx.channel.id)][args1] = None
                logger.warning(f'KeyError: {inspect.currentframe().f_back}')
                file_put_contents(FILES_CONFIG['discord-apps-config.json'], json.dumps(configuration['discord-apps-config.json'], indent=2))
        elif args1 is not None and args2 is not None:
            try:
                configuration['discord-apps-config.json'][str(ctx.user.id)][str(ctx.guild.id)][str(ctx.channel.id)][args1] = args2
                result = configuration['discord-apps-config.json'][str(ctx.user.id)][str(ctx.guild.id)][str(ctx.channel.id)][args1]
                file_put_contents(FILES_CONFIG['discord-apps-config.json'], json.dumps(configuration['discord-apps-config.json'], indent=2))
            except KeyError as e:
                logger.warning(e)
                logger.warning(f'KeyError: {inspect.currentframe().f_back}')

        title = 'Discord config'
        description = ''
        description += '```json\n'
        description += json.dumps(result, indent=2, ensure_ascii=False)
        description += '\n'
        description += '```\n'
        color = template['color']['success']
        logger.info(description)
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)
    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

@tree.command(name="help", description="コマンドのヘルプを表示")
async def mcrcon_help(ctx: discord.Interaction):
    try:
        logger.debug('Call from name:{}({}) command:{} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            ctx.guild.name,
            ctx.channel.name,
        ))

        result = None

        try:
            CREDENTIAL_MCRCON['port']=int(CREDENTIAL_MCRCON['port'])
            with MCRcon(
                CREDENTIAL_MCRCON['addr'],
                CREDENTIAL_MCRCON['pass'],
                CREDENTIAL_MCRCON['port']
            ) as mcr:
                result = mcr.command('{}'.format(' '.join([
                    ctx.command.name,
                ])))
            title = '[mcrcon] Result: /{}'.format(' '.join([
                ctx.command.name,
            ]))
            color = template['color']['success']
            logger.info(result)
        except Exception as e:
            title = '[mcrcon] Error Result: /{}'.format(' '.join([
                ctx.command.name,
            ]))
            result = ''.join(traceback.format_exc())
            color = template['color']['failure']
            logger.warning(e)
            logger.error(result)
        result = result.replace('/', '\n/')
        result = '\n'.join(sorted([line.strip() for line in result.splitlines()]))

        description = ''
        description += '```\n'
        description += result
        description += '\n'
        description += '```\n'
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)

    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

@tree.command(name="list", description="現在サーバーに接続しているプレイヤーのリストを表示")
async def mcrcon_list(ctx: discord.Interaction):
    try:
        logger.debug('Call from name:{}({}) command:{} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            ctx.guild.name,
            ctx.channel.name,
        ))

        result = None

        try:
            CREDENTIAL_MCRCON['port']=int(CREDENTIAL_MCRCON['port'])
            with MCRcon(
                CREDENTIAL_MCRCON['addr'],
                CREDENTIAL_MCRCON['pass'],
                CREDENTIAL_MCRCON['port']
            ) as mcr:
                result = mcr.command('{}'.format(' '.join([
                    ctx.command.name,
                ])))
            title = '[mcrcon] Result: /{}'.format(' '.join([
                ctx.command.name,
            ]))
            color = template['color']['success']
            logger.info(result)
        except Exception as e:
            title = '[mcrcon] Error Result: /{}'.format(' '.join([
                ctx.command.name,
            ]))
            result = ''.join(traceback.format_exc())
            color = template['color']['failure']
            logger.warning(e)
            logger.error(result)
        result = result.replace(':', ':\n')
        result = '\n'.join([line.strip() for line in result.splitlines()])

        description = ''
        description += '```\n'
        description += result
        description += '\n'
        description += '```\n'
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)

    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

@tree.command(name="banlist", description="サーバーのブラックリストを表示")
async def mcrcon_banlist(ctx: discord.Interaction):
    try:
        logger.debug('Call from name:{}({}) command:{} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            ctx.guild.name,
            ctx.channel.name,
        ))

        result = None

        try:
            CREDENTIAL_MCRCON['port']=int(CREDENTIAL_MCRCON['port'])
            with MCRcon(
                CREDENTIAL_MCRCON['addr'],
                CREDENTIAL_MCRCON['pass'],
                CREDENTIAL_MCRCON['port']
            ) as mcr:
                result = mcr.command('{}'.format(' '.join([
                    ctx.command.name,
                ])))
            title = '[mcrcon] Result: /{}'.format(' '.join([
                ctx.command.name,
            ]))
            color = template['color']['success']
            logger.info(result)
        except Exception as e:
            title = '[mcrcon] Error Result: /{}'.format(' '.join([
                ctx.command.name,
            ]))
            result = ''.join(traceback.format_exc())
            color = template['color']['failure']
            logger.warning(e)
            logger.error(result)
        result = result.replace(':', ':\n')
        result = '\n'.join([line.strip() for line in result.splitlines()])

        description = ''
        description += '```\n'
        description += result
        description += '\n'
        description += '```\n'
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)

    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

@tree.command(name="datapack", description="存在するデータパック、または有効化されているデータパックの一覧を表示")
async def mcrcon_datapack(ctx: discord.Interaction):
    args1='list'
    try:
        logger.debug('Call from name:{}({}) command:{} {} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            args1,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} {} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            args1,
            ctx.guild.name,
            ctx.channel.name,
        ))

        result = None

        try:
            CREDENTIAL_MCRCON['port']=int(CREDENTIAL_MCRCON['port'])
            with MCRcon(
                CREDENTIAL_MCRCON['addr'],
                CREDENTIAL_MCRCON['pass'],
                CREDENTIAL_MCRCON['port']
            ) as mcr:
                result = mcr.command('{}'.format(' '.join([
                    ctx.command.name,
                    args1,
                ])))
            title = '[mcrcon] Result: /{}'.format(' '.join([
                ctx.command.name,
                args1,
            ]))
            color = template['color']['success']
            logger.info(result)
        except Exception as e:
            title = '[mcrcon] Error Result: /{}'.format(' '.join([
                ctx.command.name,
                args1,
            ]))
            result = ''.join(traceback.format_exc())
            color = template['color']['failure']
            logger.warning(e)
            logger.error(result)
        result = result.replace(':', ':\n')
        result = result.replace(',', ',\n')
        result = '\n'.join([line.strip() for line in result.splitlines()])

        description = ''
        description += '```\n'
        description += result
        description += '\n'
        description += '```\n'
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)

    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

@tree.command(name="say", description="サーバー上のすべてのプレイヤーにメッセージを送信")
@discord.app_commands.describe(message="送信するメッセージの内容")
async def mcrcon_msg(ctx: discord.Interaction, message: str = ''):
    args1 = message
    try:
        logger.debug('Call from name:{}({}) command:{} {} on guild:{}({}) channel:{}({})'.format(
            ctx.user.name,
            ctx.user.id,
            ctx.command.name,
            args1,
            ctx.guild.name,
            ctx.guild.id,
            ctx.channel.name,
            ctx.channel.id,
        ))
        logger.info('Call from name:{} command:{} {} on guild:{} channel:{}'.format(
            ctx.user.name,
            ctx.command.name,
            args1,
            ctx.guild.name,
            ctx.channel.name,
        ))

        result = None

        try:
            CREDENTIAL_MCRCON['port']=int(CREDENTIAL_MCRCON['port'])
            with MCRcon(
                CREDENTIAL_MCRCON['addr'],
                CREDENTIAL_MCRCON['pass'],
                CREDENTIAL_MCRCON['port']
            ) as mcr:
                result = mcr.command('{}'.format(' '.join([
                    ctx.command.name,
                    args1,
                ])))
            title = '[mcrcon] Result: /{}'.format(' '.join([
                ctx.command.name,
                args1,
            ]))
            color = template['color']['success']
            logger.info(result)
        except Exception as e:
            title = '[mcrcon] Error Result: /{}'.format(' '.join([
                ctx.command.name,
                args1,
            ]))
            result = ''.join(traceback.format_exc())
            color = template['color']['failure']
            logger.warning(e)
            logger.error(result)
        result = result.replace(':', ':\n')
        result = '\n'.join([line.strip() for line in result.splitlines()])

        description = ''
        description += '```\n'
        description += result
        description += '\n'
        description += '```\n'
    except Exception as e:
        title = 'Error'
        description = ''.join(traceback.format_exc())
        color = template['color']['failure']
        logger.warning(e)
        logger.error(description)

    embed = discord.Embed(
        title=title,
        description=description,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color=color
    )
    await ctx.response.send_message(
        embed=embed,
        ephemeral=True#ephemeral=True→「これらはあなただけに表示されています」
    )

# botを起動
def main():
    logger.info('Connecting to Discord API')
    try:
        client.run(TOKEN_DISCORD)
    except discord.errors.PrivilegedIntentsRequired:
        logger.error(traceback.format_exc())
        sys.exit(1)

logger.info(__name__)
if __name__ == '__main__':
    main()
