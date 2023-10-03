# yote-slides: A browser-based server-optional slideshow app

* **Drag-and-drop** files and directories of **images and videos**!
* Browse for specific files, directories, or **list files**!
* Adjustable **seconds-per-slide**! (default: 12)
* **Shuffle**! (**deterministically** if you'd like!)
* Optionally, **run a server that hosts** its own slides on your computer or network!

## Controls

* Just click the slides to fullscreen!
* Left and right to move forward and back!
  * (loops between first and last)
* Scroll down to view the controls and slide index list.
* Click a line in the index to seek to that slide.

## Server: `python http_server.py`

The server just hosts files, nothing more!
If there is a text file at `slides/list.txt`, clients will auto-play that slideshow from the server when they connect!
By default, it only hosts for your local computer.
Use `--public` if you want to serve for your network!

## [Fully-functional live version!](https://kayla-yote.github.io/yote-slides)

Just drag-and-drop!
I did say "server-optional"! :)
