# owoize your Zoom Client

Ever looked at your Zoom app and thought, "man, this could really use some owo"? If so, you've come to the right place!

![screenshot](https://github.com/naveenarun/Zoom-OWO-Mod-Mac-/blob/master/screenshot.png)

## Installation Instructions

1. Click the green `Clone or download` button on this page, and click `Download ZIP`
2. Open the downloaded zip folder and highlight/copy the folder `ile.lproj`
3. Navigate to `zoom.us` in your `Applications` folder, right-click and select `Show Package Contents`, then open `Contents` > `Resources`
4. With `Resources` selected, paste in `ile.lproj`. You might need to type in your Mac's password to do this.
5. Close any open instances of Zoom and open Zoom
6. Right click on the Zoom logo in the dock and select `Switch Languages` > `Interlingue`
7. Select `Switch to Interlingue` in the pop-up menu

## For developers

Want to make your own mods? You can create a new `lproj` folder in the `Resources` directory using any of the language codes [here](http://www.loc.gov/standards/iso639-2/php/English_list.php), including e.g. `tlh.lproj` for Klingon. You only need to modify the predicates in `Localizable.strings` and `InfoPlist.strings`.

The [Python script](https://github.com/naveenarun/Zoom-OWO-Mod-Mac-/blob/master/ile.lproj/owoize.py) included `ile.lproj` uses [owotrans](https://github.com/usvimal/owotrans) to owoize strings. Install using `pip install owotranslator`.
