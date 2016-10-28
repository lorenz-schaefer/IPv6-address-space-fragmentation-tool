# IPv6-address-space-fragmentation-tool
Description:
This tool should make assigning of IPv6 adress blocks more manageable and easier to comprehend by showing the availible adress space in an 8-bit matrix. 
In the left frame you can create radiobuttons, assigning them a name, colour and finally a certain adress space, 
which will be colored in the matrix and displayed in a label accordingly.

Usage:
By opening the programm you are automatically put on a blank setup, which you can instanty start to design and save it later.

When you know how the blocks, that are going to be assigned, are called, 
selct a colour for the block(or just use the already shown example colour) and create a new radiobutton, 
naming it accordingly(The colour the button will have is shown by the "create new button"-button background colour).
If you created a radiobutton with a wrong description or a typo, 
just click  the "delete subnet"-button and then click on the radiobutton to delete it.

While having a radiobutton selected you can assign adress space by clicking the button you want to start from.
The adress space not availible in one netmask will be disabled.
Hovering the the end-adresses will mark the space that is going to be assigned,
if the space fits a netmask.
Clicking will then assign the hovered netmask and paint the area in the selected colour.
If you accidently clicked on a button or dont want to assign the net for whatever reason,
you can cancel the action by clicking the "cancel"-button.
Else if you accidently assigned an adress block or want to change it,
click on the "delete subnet"-button, then on the assigned space and if necessary assign it again.

When you wish to save the result, you can click on the "File"-menu and select "save".
A dialogue will open and ask for a name and place to save it to.
The file will be in a .json format.
Opening a file then works similarly.

Hotkeys are availible for most actions:
D => "delete subnet"
N => "new button"
O => "open file"
S => "save file"
Esc => "cancel"

