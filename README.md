# IPv6-address-space-fragmentation-tool

## Description:
This tool should make the assignment of IPv6 address blocks more manageable and easier to comprehend by showing the available address space in an 8-bit matrix. 
In the left frame you can create radio buttons, assign them a name, a colour and finally a certain address space, which will be colored in the matrix and displayed in a label accordingly.

## Usage:
By opening the program you are automatically put on a blank setup, where you can instantly start to design and save it later.

![alt text](https://raw.githubusercontent.com/lorenz-schaefer/IPv6-address-space-fragmentation-tool/master/Documentation/tool-screenshot1.png)

When you know how the blocks that are going to be assigned are called, 
select a colour for the block (or just use the one shown in the example) and create a new radio button, 
naming it accordingly (the colour the button will have is shown by the "create new button" button background colour).
If you created a radio button with a wrong description or a typo, 
just click the "delete subnet" button and then click on the radio button to delete it.

While having a radio button selected you can assign address space by clicking the matrix where you want to start from.
The address space is not portrayable, using one netmask will be disabled.
Hovering over the end addresses will mark the space that is going to be assigned,
if the space fits a netmask.
Clicking will then assign the hovered netmask and paint the area in the selected colour.
If you accidentally clicked on a button or don't want to assign the network for whatever reason,
you can cancel the action by clicking the "cancel" button.

Else, if you accidentally assigned an address block or want to change it,
click on the "delete subnet" button, then on the assigned space and, if necessary, assign it again.

To assign a subnet in an already assigned space, just create a new subnet and assign it in that space.
The legend will be restructured to show the hierarchy.
Only a subnet that has no further subnets assigned in it can be deleted.
Sometimes subnets can cover the parent subnet entirely so that it can not be seen anymore.
Hovering over a legend will highlight the assigned space.

When you wish to save the result, you can click on the "File" menu and select "save".
A dialogue will open and ask for a name and place to save it to.
The file will be in *.json* format.
Opening a file works similarly.

Hotkeys are availible for most actions:

```shell
D => "delete subnet"
N => "new button"
O => "open file"
S => "save file"
Esc => "cancel"
```

