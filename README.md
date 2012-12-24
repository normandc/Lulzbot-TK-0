Lulzbot-TK-0
============
This repository hosts 3D CAD model files (parts and assembly) for the upcoming [Lulzbot TK-0 RepRap 3D printer](http://devel.lulzbot.com/TK-0/). The parts are remodeled from the original Sketchup files in [FreeCAD](http://free-cad.sourceforge.net/), an open source 3D CAD parametric modeler. FreeCAD .fcstd files are provided, as well as [STEP](http://en.wikipedia.org/wiki/ISO_10303), a universal exchange format that can be read by most commercial and open source 3D CAD applications.

As with the original files, design files are under the GPLv3, documentation under CC-BY-SA. The design is not finalized, so these files will keep being updated.

![The TK-0 Assembly in FreeCAD](https://github.com/normandc/Lulzbot-TK-0/blob/master/TK-0_Assembly_thumb.png)

**Notes**
* Files are modeled in the latest development (unstable) version of FreeCAD - v0.13.1764 or later is required to display and edit these files. See the [FreeCAD wiki](https://sourceforge.net/apps/mediawiki/free-cad/index.php?title=Download#Development_Versions) for details.
* All the files are modeled in the PartDesign workbench, 3D features built from constrained sketches. Please be advised that due to the fact that the Sketcher and PartDesign workbenches are still under heavy development, major edits in sketches -- like adding or removing elements -- and features may (or may not) break the model and require its rebuilding.
* There is currently no Assembly features in FreeCAD, although it is planned for v0.14. The supplied TK-0_Assembly.fcstd file is built by positioning the parts separately in the 3D space, with no relationship between each other - in a similar fashion to assemblies done in non-parametric CAD software...
* Since all parts were modeled in separate FreeCAD documents instead of a single document (to allow for easier STL export), and because essential features for assemblies have not been added to FreeCAD yet, I found more practical to export all parts to STEP format, then import the STEP parts into a single FreeCAD document to create the assembly.
* TK-0_Assembly.py is a script to generate the TK-0 assembly from the files in the /STEP folder. Execute the script in FreeCAD from the [Macro dialog](https://sourceforge.net/apps/mediawiki/free-cad/index.php?title=Macros).

**TODO**
* Find a way to batch convert *.fcstd files in the FCStd folder to .stp files in the STEP folder with a python script. This would make the TK-0_Assembly.py script a lot more useful. See [this forum topic](https://sourceforge.net/apps/phpbb/free-cad/viewtopic.php?f=3&t=3332)
* In TK-0_Assembly.py:
  * Add more parts to the assembly (for now only the outer frame is included)
  * Batch import of STEP files would be nice, problem is to set their labels in the FreeCAD document to their original filenames. See [this forum topic](https://sourceforge.net/apps/phpbb/free-cad/viewtopic.php?f=3&t=3332)
* Many parts need updating, more parts are not modeled yet.

**Afterword**
I have a very limited understanding of Python. Help and/or advice with the script would be welcome.

**Acknowldegements**
Thanks to wmayer, FreeCAD dev for the trick to set relative paths in the script!
