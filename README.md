# ellipse_iso_perimeter
Few programs in RPN (called FOCAL, too) for HP41 C/CV/CX 
a) ellipse perimeter calculation (infinite series or exact AGM/MAGM, with approximations due to the limitation of the hardware precision), 
     or with the help of new models (so far only approximations available for modified shortened cycloids, ellipe/hyperbola etc.).
     The new concept of cosinus elliptique, when coming in use, is only another explanation of the AGM/MAGM methods from author http://semjonadlaj.com/
b) ellipse isoperimeter curve representation (see pdf file)
c) calculus and analysis (error calculation) of curves which define isoperimetercurves of ellipse


These functions together creates a vivarium of functions which are compatible with others regarding memory (register) sharing; 
and compatible with other RPN/FOCAL functions of modules ADVANTAGE (SOLVE) or MATH (SOL).


The memory size of HP41 is limited. 
For now, an HP41CV/CX is used without dynamic use of X-Memory. 
The target will remain to stay in the programm memory of an HP41CV/CX 
(if an HP41C is used, standard memory extensions are required). 
Programs will be reworked or re-constructed in order to stay in the memory size of the HP41CV/CX. 
If the memory size is coming short, then the programs will be adapted for the use of the X-Memory. 
Other possibilities will be to transform the programs in microcode and to transfer them into a Nov64d as new module. 
As you can see, several possibilities exists for keeping using an HP41CV/CX for a longer time.


Some programs use the printing functionality of HP-IL: it can be modified easily for having the data only being printed into the HP41 screen. The issue with this is a print delay has to be programmed for the reader having time to read the screen of the HP41.


However, the recommended setup is an HP41 connected to 
a) a paper HP-IL printer 
b) or pyILPER on a PC via a PILBOX 
(in this case, the printing will be done on a window in the PC and the results can be easily transfered to complementary analysis 
at DESMOS.COM for example via a copy/paste of a PC editor).


Way for using the programms: read the TXT files and put them direct into the HP41 or

a) download the files in a PC

b) use the application hp41uc with "hp41uc.exe /t=SCPEREL.TXT /r /k". see https://sourceforge.net/projects/hp41uc/ 
   (in Windows PC directly or in Linux PCs with the help of "Wine")
   
c) or use nutstudio with "rpncomp --raw-output PEREL6.TXT". see https://drive.google.com/file/d/1cNQAbDJ9dGd7Bosswft3MCbLbHV55qDC/view
   
d) upload the .raw file into the HP41 emulator V41 https://hp.giesselink.com/v41.htm

e) and use the programms there

f) ... or more ...

g) install pyILPER on your PC (see anaconda package)

h) transfer the programs from V41 into a virtual drive in pyILPER

i) connect your HP41 with the PC via pilbox. Here you can order a pilbox http://www.jeffcalc.hp41.eu/hpil/index.html#pilbox

j) download the programs from pyILPER into your HP41 (see HP-IL commands for downloading programs); then use them


List of programs; look at the description in the TXT files for using them.


ellipseperim_iso_surface.py
represent with the help of matplotlib a 3D surface for iso-perimeter representation (X-Y is a-b half-parameter; Z is the value of the Iso).


PEREL3 and PEREL4: calculate the perimeter given a and b (2 different convergences) using infinite series. 
No dependencies.


PEREL6: calculate the perimeter given a and b using convergence calculation of AGM/MAGM. 
No dependencies.
Use of http://www.ams.org/notices/201208/rtx120801094p.pdf from author http://semjonadlaj.com/


PEREL7: calculus of ellipse perimeter using a modified shortened cycloid function. A modified Bohr Magneton electron Adjustment constant was used 
(the constant 1.159.. = ae*1000 gave a good approximation; a modified constant into a function gave a better precision of 0.00173%).
Dependencies of MATH "SOL" or Advantage "SOLVE".


PERE10: calculus (approximation) of ellipse perimeter using a modified shortened cycloid function
with F(t)= ((0.354484 +1.04508*t) - SQRT((0.354484 +1.04508*t)**2  - 4*(0.189207 * (0.210357*t + t**2)))) /.378414 instead of "t" in the 
standard form of a standard shortened cycloid X= (pi/4)*F(t) -(0.5-sqrt(2)/pi)*sin(pi*t), Y= 0.5 +sqrt(2)/pi +(0.5-sqrt(2)/pi)*cos(pi*t)
Dependencies: MATH "SOL" or ADVANTAGE "SOLVE".


PERE12: AGM/MAGM like calculation.


PEREL9: calculus of ellipse perimeter using an approximation function for the iso-perimeter curves. Further works planned. 
The first level of calculus is implemented: isoperimeter function is curve fitted with an ellipse and a constant 1.64079 (see file header).
Dependencies: none.


PERELS: calculate the perimeter of an ellipse according the best suitable method (best convergency identified depending of the factor b/a). 
Dependencies: PEREL3 and PEREL4 and PEREL6.


PERELC: calculate the perimeter of an ellipse according convercence algorithm (AGM, MAGM), now only PEREL6 listed.
Dependencies: PEREL6.
Remark: PERELS or PERELC will give the same result. Use of PEREL6 only is recommended for now.


BPEREL: calculate the other half-parameter of an ellipse by a given perimeter. 
Dependencies: PERELS (or PEREL6), SOLVE from Advantage 
(or "SOL" from Math module by replacing the Line 
XEQ "SOLVE" 
with 
ASTO 06
XEQ "SOL").


SCPEREL: output several isoperimeter points of an ellipse by a given perimeter. 
Dependencies: BPEREL, HP-IL (for outputs logging into printer/screen).


CMPPER1: compare 
a) exact ellipse perimeter calculation based on infinite serial calculations or AGM/MAGM and 
b) ellipse perimeter calculation based on PEREL7 or PERE10 or others.
by giving the differences in absolute and %.
Dependencies: BPEREL, HP-IL (for outputs logging into printer/screen), new function "PEREL7" (or others).


SCFPER1: calculus of several points of a modified shortened cycloid with a curve f(t) curve replacing the Bohr Magneton electron Adjustment constant 
which is multiplied by 1000 in (t^ae*1000 change into t^f(t)) for use in the PEREL7 function. 
Based on the calculated points of this curve, a curve fitting was done and a good guess of a function was defined. See PEREL7.


SCFPER2: calculus of several points of a modified shortened cycloid with a curve f(t) curve for calculating ellipse perimeter 
in a precise (approximnation) method.
Dependencies: BPEREL, SOLVE from Sandmath. 


SCFPER3: calculus of several parameters of an elliptic approximation curve for diverse (b) factors of PEREL9 (see header in it).
Dependencies: BPEREL, SOLVE from Sandmath. 


TPEREL: calculate the angle of the cosinus elliptique ("Ce") when its overall ellipse radius is given. See the explanation in the program file

To Cosinus elliptique "Ce": 1/Ce(a/b)=(pi*N(tan**2(angle)))/(2*SQRT(1+tan**2(angle))*M(tan(angle)))
M and N are the AGM and MAGM (see PEREL6). MAGM created by http://semjonadlaj.com/
Ce(a/b): Maximum 1 and Minimum 0.9003.. (=2*SQRT(2)/pi) for a/b between 0 and 1.
angle: between 0 and pi/4 (= atan(a/b) where a<b)
where the final explanation of it is >> Ellipse perimeter of (a,b) = 4 * SQRT(a**2+b**2) / Ce(a/b) <<
Ce is independant of the ellipse form. It is valid for all ellipses. It depends only of the factor a/b.


RPEREL: calculate the radius of the cosinus elliptique when its angle is given (see TPEREL and the explanation in the program file).


Final word: 
these functions which can be used in the HP41 must be understood in the terms of mocks in the area of agile working. 
They are "Good enough" functions for quick evaluations of new ideas in ellipse-perimeter calculus.
Any functions with precise results will have to be checked and released on higher precision calculators (HP71 for example) 
and perhaps larger 64bits processors before any further use or creating mathematical or physician conclusions.
All the functions are NOT for any legal and productive use in the real world. Just use it in order to developp your creativity and thoughts.
Contact me if you want to share new thoughts or have any question.


Keywords: ellipse circumference, cosinus elliptique, modified shortened cycloid, AGM/MAGM
