import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 - reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                
                if("https://www.youtube.com/watch?" in item): #If there's 
                  info = ydl.extract_info(item, download=False)
                  print(info)
                else:
                  
                  info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]  
                
            except Exception: 
                return False


        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            #try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            print(self.music_queue)
            self.music_queue.pop(0)
            source = await discord.FFmpegOpusAudio.from_probe(m_url, **self.FFMPEG_OPTIONS)
            self.vc.play(source, after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="play", help="Plays a selected song from youtube", aliases = ["p"])
    async def p(self, ctx, *args):
        query = " ".join(args)
        
        
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download the song.")
            else:
                
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await ctx.send('``🎵 Now playing``')
                    await self.play_music()

    @commands.command(name="queue", help="Displays the current songs in queue", aliases = ["q"])
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue")

    @commands.command(name="skip", help="Skips the current song being played")
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            await ctx.send('``⏭️ Music skipped``')
            await self.play_music()

    @commands.command(name="pause", help="Pauses the music")
    async def pause(self, ctx):
      await ctx.send('``⏸️ Music paused``')
      await ctx.voice_client.pause()
    
    @commands.command(name="resume", help="Resumes the music")
    async def resume(self, ctx):
      await ctx.send('``⏯️ Music resumed``')
      await ctx.voice_client.resume()

    @commands.command(name="disconnect", help="Disconnects the bot", aliases = ["leave"])
    async def disconnect(self, ctx):
      await ctx.send('``👋 goodbye``')
      await ctx.voice_client.disconnect()


def setup(client):
 client.add_cog(music(client))
    
    