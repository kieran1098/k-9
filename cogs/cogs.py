import discord
from discord.ext import commands





class cogset(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(name='_load')
  @commands.is_owner()
  async def load(self, ctx, *, module):
    
    try:
      self.bot.load_extension(module)
    #Check to see if we have any errors. if so return the error in a nice format
    except Exception as e:
           await ctx.send(' {}   {}   '.format(type(e ) .__name__, e    )    )

    else:
#notify the bot loaded the module
         await ctx.send(f"Loaded `{module}`")
      
      
      
  
  @commands.command(name='_unload')
  @commands.is_owner()
  async def unload(self, ctx, *, module):

    try: 
      self.bot.unload_extension(module)

    except Exception as e:
      
      await ctx.send('  {}   {}       '.format(type   (e   ) .__name__, e   )            )

    else:

      await ctx.send(f"Unloaded `{module}` ")

  
  

  
  
  #_ is required as the bot has a default command called reload.
  
  
  @commands.command(name='_reload')
  @commands.is_owner()
  async def reload(self, ctx, *, module):
    
    try:
      self.bot.unload_extension(module)
      self.bot.load_extension(module)

    except Exception as e:
      await ctx.send('  {}   {}       '.format(type   (e   ) .__name__, e   )            )
    
    else:
      
      await ctx.send(f"Reloaded `{module}` ")
      




def setup(bot):
  bot.add_cog(cogset(bot))