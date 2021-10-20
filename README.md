# ellipse_perimeter
Few programs in RPN (called FOCAL, too) for HP41 C/CV/CX 
a) ellipse perimeter calculation
b) ellipse isoperimeter curve representation (see pdf file)
c) calculus and analysis (error calculation) of curves which define isoperimetercurves of ellipse


These functions together creates a vivarium of functions which are compatible with others regarding memory (register) sharing; 
and compatible with other RPN/FOCAL functions of modules ADVANTAGE (SOLVE) or MATH (SOL).


Some programs use the printing functionality of HP-IL: it can be modified easily for having the data only being printed into the HP41 screen. 


However, the recommended setup is an HP41 connected to pyILPER on a PC via a PILBOX 
(in this case, the printing will be done on a window in the PC and the results can be easily transfered to complementary analysis 
at DESMOS.COM for example via a copy/paste of a PC editor).


Way for using the programms: read the TXT files and put them direct into the HP41 or

a) download the files in a PC

b) use the application hp41uc with "hp41uc.exe /t=SCPEREL.TXT /r /k". see https://sourceforge.net/projects/hp41uc/
   or use nutstudio with "rpncomp --raw-output PEREL6.TXT". see https://drive.google.com/file/d/1cNQAbDJ9dGd7Bosswft3MCbLbHV55qDC/view


c) upload the .raw file into the HP41 emulator V41 https://hp.giesselink.com/v41.htm

d) and use the programms there

e) ... or more ...

f) install pyILPER on your PC (see anaconda package)

g) transfer the programs from V41 into a virtual drive in pyILPER

h) connect your HP41 with the PC via pilbox. Here you can order a pilbox http://www.jeffcalc.hp41.eu/hpil/index.html#pilbox

i) download the programs from pyILPER into your HP41 (see HP-IL commands for downloading programs); then use them


List of programs; look at the description in the TXT files for using them.


ellipseperim_iso_surface.py
represent with the help of matplotlib a 3D surface for iso-perimeter representation (X-Y is a-b half-parameter; Z is the value of the Iso).


PEREL3 and PEREL4: calculate the perimeter given a and b (2 different convergences) using infinite series. 
No dependencies.


PEREL6: calculate the perimeter given a and b using convergence calculation of AGM/MAGM. 
No dependencies.


PEREL7: calculus of ellipse perimeter using a modified shortened cycloid function. A modified Bohr Magneton electron Adjustment constant was used 
(the constant 1.159.. = ae*1000 gave a good approximation; a modified constant into a function gave a better precision of 0.00173%).
Dependencies of MATH "SOL" or Advantage "SOLVE".


PERELS: calculate the perimeter of an ellipse according the best suitable method (best convergency identified depending of the factor b/a). 
Dependencies: PEREL3 and PEREL4 and PEREL6 (however it could be simplified for using PEREL6 only which is the quickest convergence for the whole area a/b 0..1).


BPEREL: calculate the other half-parameter of an ellipse by a given perimeter. 
Dependencies: PERELS, SOLVE from Advantage 
(or "SOL" from Math module by replacing the Line 
XEQ "SOLVE" 
with 
ASTO 06
XEQ "SOL").


SCPEREL: output several isoperimeter points of an ellipse by a given perimeter. 
Dependencies: BPEREL, HP-IL (for outputs logging into printer/screen).


CMPPER1: compare 
a) ellipse perimeter calculation based on infinite serial calculations and 
b) ellipse perimeter calculation based on PEREL7.
Dependencies: BPEREL, HP-IL (for outputs logging into printer/screen), new function "PEREL7" (or other tbd).


SCFPER1: calculus of several points of a modified shortened cycloid with a curve f(t) curve replacing the Bohr Magneton electron Adjustment constant * 1000 in (t^ae*1000 change into t^f(t)) for use in the PEREL7 function. 
Based on the calculated points of this curve, a curve fitting was done and a good guess of a function was defined. See PEREL7.


Final word: 
these functions which can be used in the HP41 must be understood in the terms of mocks in the area of agile working. 
They are "Good enough" functions for quick evaluations of new ideas in ellipse-perimeter calculus.
Any functions with precise results will have to be checked and released on higher precision calculators (HP71 for example) 
and perhaps larger 64bits processors before any further use or creating mathematical or physician conclusions.
All the functions are NOT for any legal and productive use in the real world. Just use it in order to developp your creativity and thoughts.
Contact me if you want to share new thoughts or have any question.
