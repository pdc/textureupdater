Texture Updater
===============

A texture pack and Texturepacker recipes for upgrading an orphaned
texturepack to the latest Minecraft version.

This package is used by [Texturejam][3].

Wait, what’s a texture pack?
----------------------------

[Minecraft][1] is a game that uses 16×16 textures painted on to cubes to
define the world. Texture packs replace the default imagery to give the
game a different look.

So what’s the problem?
----------------------

The trick is that with recent releases Mojang have added new types of
block to the game, and these need new tiles in the texture pack. Old
texture packs will leave them blank or worse. This means you can must
give up on using your favourite texture pack until the artist draws the
new tiles.

And what is your solution?
--------------------------

[Texurepacker][2] is a tool for remixing texture packs using recipes to
describe which tiles to get from which pack. We use a special pack
called Patches that contains fairly generic versions of the new tiles
added in Minecraft Beta 1.2 onward and recipes to add these to an older
texture pack to make one that supports the latest Minecraft version.

How could I use this?
---------------------

Suppose your favourite texture pack is called `foobar.zip`, but was
designed for Minecraft Beta 1.3. With Texturepacker installed, you could
use a command like this:

    maketexture --out=foobar+patches.zip base=foobar.zip rx/upgrade-beta-13.tprx

This takes the ZIP file `foobar+patches.zip` that can be used to play
the current Minecraft release.


  [1]: http://minecraft.net/
  [2]: http://pdc.github.com/texturepacker/
  [3]: http://texturejam.org.uk/