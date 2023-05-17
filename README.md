smb3splitoffsetter
==================

Description: Offset smb3 warpless splits by about 17s/31s each world to accomodate
offscreen wand grabs.

Elaboration: Generally SMB3 runners split when we touch the wand, however,
when we get offscreen wand grabs the split is very inaccurate. So, it is preferable
to split instead on a consistent time, liuke when the king grabs the wand after
all the OSWG action occurs and the runner can accurately split. Change is tough
though since the runner has already split for ages using the old method, so we want
to automate changing those legacy splits. This script performs those offset changes
automatically. 

All the code and assets were made by Lui_!
narfman0 just uselessly packaged it :)

Installation
------------

Navigate to the most recent versioned release here:

https://github.com/narfman0/smb3-split-offsetter/tags

Download the zip and extract to your favorite directory.

License
-------

Copyright (c) 2023 Lui_, narfman0

See LICENSE for details
