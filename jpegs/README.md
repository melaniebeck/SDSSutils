## jpegCreator
this little module creates SDSS jpeg urls given all the standard SDSS args and options.\\
it can also create a bash script to wget a list of SDSS jpegs.\\
or you can just make an ascii file that lists all the jpeg url names.\\


|Parameters	|Expected Values
|-----------|---------------|
|Ra	        |Right Ascention (deg)
|Dec	    |Declination (deg)
|scale	    |Scale of image (''/pixel, default=0.396)
|height	    |pixels
|width	    |pixels
|options	|string of characters for overlays on image


|Code	|Effect on image|
|-------|---------------|
|G	    |Grid           |
|L	    |Label          |
|P	    |PhotoObjs      |
|S	    |SpecObjs       |
|T	    |TargetObjs     |
|O	    |Outline        |
|B	    |BoundingBox    |
|F	    |Fields         |
|M	    |Masks          | 
|Q	    |Plates         |
|I	    |InvertImage    |


## Example usage 1) Create a single jpeg url
```
from jpegCreator import *

jpg = jpegURL(ra, dec, scale, height, width, options='SGPMQ')
print jpg.url
```

## Example usage 2) Create a file with a list of jpg urls for wget-ing
``` from jpegCreator import *

fileCreator.bashScript(data, 'jpgURLs.sh')
```

In the terminal: `source jpgURLs.sh` will start the jpg download. 
Note: `data` needs to have columns for ra, dec, scale, height, width, and options for *each* galaxy 
