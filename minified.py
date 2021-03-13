a ='Muted'#line:1
Z =True #line:2
Y ='$inc'#line:3
X ='tails'#line:4
W ='heads'#line:5
M =str #line:6
J =int #line:7
H ='coins'#line:8
G ='id'#line:9
A =False #line:10
from discord.ext import commands as N #line:11
import discord as C ,os ,random as L ,requests as I #line:12
from threading import Thread as O #line:13
from flask import Flask #line:14
import pymongo as P #line:15
B =N.Bot (command_prefix ='cf ')#line:16
K =Flask (__name__ )#line:17
Q =[W ,X ]#line:18
R =os .getenv ('mongokey')#line:19
@K .route ('/')#line:20
def b ():return 'Chill Bot'#line:21
S =os .getenv ('token')#line:22
c =os .getenv ('author')#line:23
D ='Lacking perms'#line:24
T =0xb55a557504e0024 #line:25
B .remove_command ('help')#line:26
d =list (os .getenv ('badwords'))#line:27
U =P .MongoClient ('mongodb://dbUser:'+R +'@cluster0-shard-00-00.xoe4b.mongodb.net:27017,cluster0-shard-00-01.xoe4b.mongodb.net:27017,cluster0-shard-00-02.xoe4b.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-rj95f3-shard-0&authSource=admin&retryWrites=true&w=majority')#line:28
F =U .money .coins #line:29
@B .event #line:30
async def e ():await B .change_presence (activity =C .Activity (type =C .ActivityType .playing ,name ='Chill Bot | Prefix: cf'));print (f"{B.user.name} has connected to Discord!")#line:31
def E (O00OO0OOO0O0O0OO0 ,OOO0O0OOO0O000000 ):F .update_one ({G :O00OO0OOO0O0O0OO0 },{Y :{H :OOO0O0OOO0O000000 }},upsert =Z )#line:32
@B .command ()#line:33
async def f (O0O0000OO000O0OO0 ,OO0OO0OOOOO0O00OO ,O0000O0000OO0000O ):O00O0O0OOOOOO0O0O =O0000O0000OO0000O ;E (OO0OO0OOOOO0O00OO .id ,O00O0O0OOOOOO0O0O *-1 );E (O0O0000OO000O0OO0 .author .id ,O00O0O0OOOOOO0O0O *-1 );O0OOOOO00O0000OOO =C .Embed (color =4737096 );O0OOOOO00O0000OOO .add_field (name ='Shootout',value =f"You and <@{OO0OO0OOOOO0O00OO.id}> both lost {O00O0O0OOOOOO0O0O}",inline =A );await O0O0000OO000O0OO0 .send (embed =O0OOOOO00O0000OOO )#line:34
@B .command ()#line:35
async def g (O0O0OOOO00O0O00OO ,O0O0OO0OOOOO0O00O ):#line:36
	O00OOO0O000O0O00O ='Gamble';OOOO0O0O0O0OOOOOO =O0O0OOOO00O0O00OO ;OOO0O00OO00000000 =O0O0OO0OOOOO0O00O ;OO0000000OO0O000O =C .Embed (color =4737096 );OOOO00O00O00O000O =F .find_one ({G :OOOO0O0O0O0OOOOOO .author .id });OO0OO00000OO00OOO =OOOO00O00O00O000O [H ]#line:37
	try :#line:38
		if OO0OO00000OO00OOO >=J (OOO0O00OO00000000 ):#line:39
			O0OO00O00O0O00OOO =L .choice (Q )#line:40
			if O0OO00O00O0O00OOO ==X :E (OOOO0O0O0O0OOOOOO .author .id ,OOO0O00OO00000000 *-1 );OO0000000OO0O000O .add_field (name =O00OOO0O000O0O00O ,value =f"Lost {OOO0O00OO00000000} ChillCoins",inline =A )#line:41
			elif O0OO00O00O0O00OOO ==W :E (OOOO0O0O0O0OOOOOO .author .id ,OOO0O00OO00000000 );OO0000000OO0O000O .add_field (name =O00OOO0O000O0O00O ,value =f"Won {OOO0O00OO00000000} ChillCoins",inline =A )#line:42
		else :OO0000000OO0O000O .add_field (name =O00OOO0O000O0O00O ,value =f"Not enough ChillCoins, need {OOO0O00OO00000000} have {OO0OO00000OO00OOO}",inline =A )#line:43
	except :OO0000000OO0O000O .add_field (name =O00OOO0O000O0O00O ,value ='Invalid amount',inline =A )#line:44
	await OOOO0O0O0O0OOOOOO .send (embed =OO0000000OO0O000O )#line:45
@B .command ()#line:46
async def h (OO000OOOO0OO0OOOO ,O0O00OO0OO0000OOO ,O00000OO0OO00O000 ):#line:47
	OO00O00OO00O0O00O ='Donate';OO0O00OOOO0O000OO =OO000OOOO0OO0OOOO ;O00000000000O00O0 =O00000OO0OO00O000 ;O0OOO0O00O0000000 =C .Embed (color =4737096 );O00O000O0O0O0O0OO =F .find_one ({G :OO0O00OOOO0O000OO .author .id });O0OO0OO00OO0000O0 =O00O000O0O0O0O0OO [H ]#line:48
	try :#line:49
		if O0OO0OO00OO0000O0 >=J (O00000000000O00O0 ):O0OOO0O00O0000000 .add_field (name =OO00O00OO00O0O00O ,value =f"Donated {O00000000000O00O0} ChillCoins to <@{O0O00OO0OO0000OOO.id}>",inline =A );E (OO0O00OOOO0O000OO .author .id ,O00000000000O00O0 *-1 );E (O0O00OO0OO0000OOO .id ,O00000000000O00O0 )#line:50
		else :O0OOO0O00O0000000 .add_field (name =OO00O00OO00O0O00O ,value =f"Not enough ChillCoins, need {O00000000000O00O0} have {O0OO0OO00OO0000O0}",inline =A )#line:51
	except :O0OOO0O00O0000000 .add_field (name =OO00O00OO00O0O00O ,value ='Something went wrong',inline =A )#line:52
	await OO0O00OOOO0O000OO .send (embed =O0OOO0O00O0000000 )#line:53
@B .command ()#line:54
async def i (OO0O000O0OO0OOO0O ):O00OO0000OOOOOO0O =F .find_one ({G :OO0O000O0OO0OOO0O .author .id });O0OO000OOO0OOO0OO =C .Embed (color =4737096 );O0OO000OOO0OOO0OO .add_field (name ='Balance',value =O00OO0000OOOOOO0O [H ],inline =A );await OO0O000O0OO0OOO0O .send (embed =O0OO000OOO0OOO0OO )#line:55
@B .command ()#line:56
async def j (OO00OO0000OOO00O0 ,O0OOO00O000OOO0OO ):#line:57
	O000000OO000OO0O0 ='Mute';O0O00OO00000O00OO =OO00OO0000OOO00O0 ;O0O000O000000OO0O =C .Embed (color =4737096 )#line:58
	if O0O00OO00000O00OO .author .guild_permissions .administrator :await O0OOO00O000OOO0OO .add_roles (C .utils .get (O0O00OO00000O00OO .message .guild .roles ,name =a ));O0O000O000000OO0O .add_field (name =O000000OO000OO0O0 ,value =f"<@{O0OOO00O000OOO0OO.id}>",inline =A )#line:59
	else :O0O000O000000OO0O .add_field (name =O000000OO000OO0O0 ,value =D ,inline =A )#line:60
	await O0O00OO00000O00OO .send (embed =O0O000O000000OO0O )#line:61
@B .command ()#line:62
async def k (O0OO0O000O000O000 ,OOO0O00OOO0000000 ):#line:63
	OOOO0O0OO00OOO00O ='Unmute';OO0O0O00000OO000O =O0OO0O000O000O000 ;O00O0O0OOO0O0000O =C .Embed (color =4737096 )#line:64
	if OO0O0O00000OO000O .author .guild_permissions .administrator :await OOO0O00OOO0000000 .remove_roles (C .utils .get (OO0O0O00000OO000O .message .guild .roles ,name =a ));O00O0O0OOO0O0000O .add_field (name =OOOO0O0OO00OOO00O ,value =f"<@{OOO0O00OOO0000000.id}>",inline =A )#line:65
	else :O00O0O0OOO0O0000O .add_field (name =OOOO0O0OO00OOO00O ,value =D ,inline =A );await OO0O0O00000OO000O .send (D )#line:66
	await OO0O0O00000OO000O .send (embed =O00O0O0OOO0O0000O )#line:67
@B .command ()#line:68
async def l (OOOO000O0OO00OOOO ,O000O0OO0OO000O00 ):#line:69
	O0O0OO0OO00O0O0OO ='Kick';OOO0OOOO000OOO00O =OOOO000O0OO00OOOO ;OO000O00OOO0OO0OO =C .Embed (color =4737096 )#line:70
	if OOO0OOOO000OOO00O .author .guild_permissions .administrator :await OOO0OOOO000OOO00O .guild .kick (O000O0OO0OO000O00 ,reason ='Kicked');OO000O00OOO0OO0OO .add_field (name =O0O0OO0OO00O0O0OO ,value =f"<@{O000O0OO0OO000O00.id}>",inline =A )#line:71
	else :OO000O00OOO0OO0OO .add_field (name =O0O0OO0OO00O0O0OO ,value =D ,inline =A );await OOO0OOOO000OOO00O .send (D )#line:72
	await OOO0OOOO000OOO00O .send (embed =OO000O00OOO0OO0OO )#line:73
@B .command ()#line:74
async def m (O000O0000OO0OO0OO ,O00OOOO000OO0OO0O ):#line:75
	OOO0OOOOOOOO0OOOO ='Pardon';OOO0O0000000O00OO =O000O0000OO0OO0OO ;O000OOO0OO0O00OO0 =C .Embed (color =4737096 )#line:76
	if OOO0O0000000O00OO .author .guild_permissions .administrator :await OOO0O0000000O00OO .guild .unban (O00OOOO000OO0OO0O );O000OOO0OO0O00OO0 .add_field (name =OOO0OOOOOOOO0OOOO ,value =f"<@{O00OOOO000OO0OO0O.id}>",inline =A )#line:77
	else :O000OOO0OO0O00OO0 .add_field (name =OOO0OOOOOOOO0OOOO ,value =D ,inline =A );await OOO0O0000000O00OO .send (D )#line:78
	await OOO0O0000000O00OO .send (embed =O000OOO0OO0O00OO0 )#line:79
@B .command ()#line:80
async def n (O00O0OO0OO0OOOO00 ,OO0000OOOO0O00OOO ):#line:81
	OO00OO000000O0OOO ='Ban';O00O0O000OOOO0OO0 =O00O0OO0OO0OOOO00 ;O000O00O00O0OO00O =C .Embed (color =4737096 )#line:82
	if O00O0O000OOOO0OO0 .author .guild_permissions .administrator :await O00O0O000OOOO0OO0 .guild .ban (OO0000OOOO0O00OOO ,reason ='Banned');O000O00O00O0OO00O .add_field (name =OO00OO000000O0OOO ,value =f"<@{OO0000OOOO0O00OOO.id}>",inline =A )#line:83
	else :O000O00O00O0OO00O .add_field (name =OO00OO000000O0OOO ,value =D ,inline =A );await O00O0O000OOOO0OO0 .send (D )#line:84
	await O00O0O000OOOO0OO0 .send (embed =O000O00O00O0OO00O )#line:85
@B .command ()#line:86
async def o (OO0OOO0000OOOOO00 ,OOOO0000OOOOO0OOO ):#line:87
	OOO0OOOOO00OOO0OO ='Purge';O0O00O0OOO00OOOOO =OOOO0000OOOOO0OOO ;O0OOO00O0OO00O00O =OO0OOO0000OOOOO00 ;OOO00000O00O0O000 =C .Embed (color =4737096 )#line:88
	if O0OOO00O0OO00O00O .author .guild_permissions .administrator :await O0OOO00O0OO00O00O .channel .purge (limit =O0O00O0OOO00OOOOO );OOO00000O00O0O000 .add_field (name =OOO0OOOOO00OOO0OO ,value =M (O0O00O0OOO00OOOOO )+' messages',inline =A )#line:89
	else :OOO00000O00O0O000 .add_field (name =OOO0OOOOO00OOO0OO ,value =D ,inline =A );await O0OOO00O0OO00O00O .send (D )#line:90
	await O0OOO00O0OO00O00O .send (embed =OOO00000O00O0O000 )#line:91
@B .command ()#line:92
async def p (O00OOO0000O00OOOO ,O0000O0O000000000 ):OO000OOO0O00OOO0O =O0000O0O000000000 ;O00OOO0OO000OOO0O =L .choice ([3800852 ,4149685 ,10233776 ,16635957 ]);OO00OO000O0O000OO =C .Embed (title =f"{OO000OOO0O00OOO0O.name}'s Stats",color =O00OOO0OO000OOO0O );OO00OO000O0O000OO .set_thumbnail (url =M (OO000OOO0O00OOO0O .avatar_url ));OO00OO000O0O000OO .add_field (name ='Name',value =OO000OOO0O00OOO0O .name ,inline =A );OO00OO000O0O000OO .add_field (name ='ID',value =OO000OOO0O00OOO0O .id ,inline =A );OO00OO000O0O000OO .add_field (name ='Tag',value =OO000OOO0O00OOO0O .discriminator ,inline =A );OO00OO000O0O000OO .add_field (name ='Account Creation',value =OO000OOO0O00OOO0O .created_at .strftime ('%Y-%m-%d at %H:%M:%S'),inline =A );OO00OO000O0O000OO .add_field (name ='Bot',value =OO000OOO0O00OOO0O .bot ,inline =A );await O00OOO0000O00OOOO .send (embed =OO00OO000O0O000OO )#line:93
@B .command ()#line:94
async def q (OO0O000O0O00000OO ):O0O0O00O0OO0O0000 =I .get ('https://meme-api.herokuapp.com/gimme/memes');O0O0O00O0OO0O0000 =O0O0O00O0OO0O0000 .json ();O000OOO000O0OO00O =C .Embed (color =4737096 );O000OOO000O0OO00O .add_field (name =O0O0O00O0OO0O0000 ['title'],value ='r/memes',inline =Z );O000OOO000O0OO00O .set_image (url =O0O0O00O0OO0O0000 ['url']);await OO0O000O0O00000OO .send (embed =O000OOO000O0OO00O )#line:95
@B .command ()#line:96
async def r (OO00OOO0O00OOO00O ):O000OO00O00000OOO ='Joke';O00O0OO0000OOOOO0 =I .get ('http://official-joke-api.appspot.com/jokes/random');O00O0OO0000OOOOO0 =O00O0OO0000OOOOO0 .json ();OO00000O0000OOO00 =C .Embed (title =O000OO00O00000OOO ,description ='Dad Jokes',color =4737096 );OO00000O0000OOO00 .add_field (name =O000OO00O00000OOO ,value =O00O0OO0000OOOOO0 ['setup'],inline =A );OO00000O0000OOO00 .add_field (name ='Punchline',value =O00O0OO0000OOOOO0 ['punchline'],inline =A );OO00000O0000OOO00 .add_field (name ='Joke Number',value =O00O0OO0000OOOOO0 [G ],inline =A );await OO00OOO0O00OOO00O .send (embed =OO00000O0000OOO00 )#line:97
@B .command ()#line:98
async def s (OOOO00OOO0OO0OO00 ):O000000OO0OOOOOO0 =C .Embed ();O000000OO0OOOOOO0 .add_field (name ='Ping',value =M (round (B .latency *1000 ,1 ))+' ms',inline =A );await OOOO00OOO0OO0OO00 .send (embed =O000000OO0OOOOOO0 )#line:99
@B .command ()#line:100
async def t (OO0000OO00O0O00O0 ):OOO000OO000O00OOO =C .Embed (title ='Admin Help Page',color =4737096 );OOO000OO000O00OOO .add_field (name ='cf clean [int:messages]',value ='Purge certain number of messages',inline =A );OOO000OO000O00OOO .add_field (name ='cf mute/unmute [id/ping:user]',value ='Mutes or unmutes a user',inline =A );OOO000OO000O00OOO .add_field (name ='cf ban/pardon [id/ping:user]',value ='Ban or unban a user',inline =A );OOO000OO000O00OOO .add_field (name ='cf kick [id/ping:user]',value ='Kick a user',inline =A );await OO0000OO00O0O00O0 .send (embed =OOO000OO000O00OOO )#line:101
@B .command ()#line:102
async def help (OO000OOOO0OOOO000 ):OO0O0000OOO0O0OOO =C .Embed (title ='Help Page',color =4737096 );OO0O0000OOO0O0OOO .add_field (name ='cf user [id/ping:user]',value ='Data for a user',inline =A );OO0O0000OOO0O0OOO .add_field (name ='cf ping',value ='Get bot latency',inline =A );OO0O0000OOO0O0OOO .add_field (name ='cf joke',value ='Get a random joke',inline =A );OO0O0000OOO0O0OOO .add_field (name ='cf meme',value ='Get a reddit meme',inline =A );await OO000OOOO0OOOO000 .send (embed =OO0O0000OOO0O0OOO )#line:103
@B .event #line:104
async def u (OO0OOO00OO0000O0O ):#line:105
	O0O000O00O0O00OO0 =OO0OOO00OO0000O0O ;F .update_one ({G :O0O000O00O0O00OO0 .author .id },{Y :{H :10 }})#line:106
	if O0O000O00O0O00OO0 .channel .id ==T :#line:107
		O00000OO0OO0OO00O =await O0O000O00O0O00OO0 .channel .history (limit =2 ).flatten ();O0O000OOOO000O0OO =O00000OO0OO0OO00O [1 ]#line:108
		try :#line:109
			if J (O0O000O00O0O00OO0 .content )==J (O0O000OOOO000O0OO .content )+1 :await O0O000O00O0O00OO0 .add_reaction ('👍')#line:110
			else :await O0O000O00O0O00OO0 .delete ()#line:111
		except :await O0O000O00O0O00OO0 .delete ()#line:112
	await B .process_commands (O0O000O00O0O00OO0 )#line:113
def V ():K .run (host ='0.0.0.0',port ='8000')#line:114
O (None ,V ).start ()#line:115
B .run (S )