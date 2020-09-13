# Copybunch
An OS utility that keep track of your multiple copied items and remind you while pasting

It becomes a headache when a user has to copy multiple items from a source location to destination location. Until a user paste the selected copied item, one can't copy another instance and thus result in copy paste a single item/instance always. We are solving this problem by keeping a buffer of copied items and let user choose from the same. Every time the user copies an item, a new buffer will be created and when user performs paste(introduced a new HOTKEY **ctrl+b** at os level), the list of all buffer items will be shown from which the user can select the required item. It will not only save time, but provide a much better way for performing copy + paste functionality at operating system level.


## Features

  - Keeping track of multiple copied items
  - Displaying a context menu while performaing the paste
  - For having **cipybunch's paste** context menu while paste, a new key combination has been provided (**ctrl+b**)
  

## Quick start
After cloning or downloading the code, run the following command at the applciation root directory:

    python handlekey.py
    
<i>Make sure that all you have **python** installed in your system, along with all the required dependencies</i>.

#### NOTE: We will be creating an executable in future to make it more easy for the user's to setup and start with the functionality

## Technologies

  - Python

## Demo Link [HERE](https://youtu.be/JV52VGOFSHs)


License
----

MIT

