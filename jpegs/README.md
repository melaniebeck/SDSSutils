## jpegCreator
this little module creates SDSS jpeg urls given all the standard SDSS args and options.\\
it can also create a bash script to wget a list of SDSS jpegs.\\
or you can just make an ascii file that lists all the jpeg url names.\\


|Parameters	|Expected Values
|Ra	        |Right Ascention in degrees
|Dec	Declination in degrees
|scale	Scale of image in arsec per pixel, 0.4 is default
|height	in pixels
|width	in pixels

opt	a string of characters for overlays on image (details below). This is an optional parameter

|Code	|Effect on image|
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

