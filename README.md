<p align="center"><img src="screenshots/progress_bar_top.png"></p>

<h2 align="center">Progress Bar for Anki</h2>

<p align="center">
<a title="Latest (pre-)release" href="https://github.com/glutanimate/progress-bar/releases"><img src ="https://img.shields.io/github/release-pre/glutanimate/progress-bar.svg?colorB=brightgreen"></a>
<a title="License: GNU AGPLv3" href="https://github.com/glutanimate/progress-bar/blob/master/LICENSE"><img  src="https://img.shields.io/badge/license-GNU AGPLv3-green.svg"></a>
<a title="Rate on AnkiWeb" href="https://ankiweb.net/shared/info/2091361802"><img src="https://glutanimate.com/logos/ankiweb-rate.svg"></a>
<br>
<a title="Buy me a coffee :)" href="https://ko-fi.com/X8X0L4YV"><img src="https://img.shields.io/badge/ko--fi-contribute-%23579ebd.svg"></a>
<a title="Support me on Patreon :D" href="https://www.patreon.com/bePatron?u=7522179"><img src="https://img.shields.io/badge/patreon-support-%23f96854.svg"></a>
<a title="Follow me on Twitter" href="https://twitter.com/intent/user?screen_name=glutanimate"><img src="https://img.shields.io/twitter/follow/glutanimate.svg"></a>
</p>

> Your Anki session progress at a glance

This is an add-on for the spaced-repetition flashcard app [Anki](https://apps.ankiweb.net/) that adds a progress bar to the review screen.

### Table of Contents <!-- omit in toc -->

<!-- MarkdownTOC levels="1,2,3" -->

- [Installation](#installation)
- [Documentation](#documentation)
- [Building](#building)
- [Contributing](#contributing)
- [License and Credits](#license-and-credits)

<!-- /MarkdownTOC -->

<!-- ### Screenshots

![](screenshots/screenshot.png) -->

### Installation

#### AnkiWeb <!-- omit in toc -->

The easiest way to install Progress Bar is through [AnkiWeb](https://ankiweb.net/shared/info/2091361802).

#### Manual installation <!-- omit in toc -->

Please click on the entry corresponding to your Anki version:

<details>

<summary><i>Recent Anki 2.1 versions</i></summary>

<br>

*Note: These instructions only work on Anki 2.1.17 and up. For older Anki releases please see the next section.*

<br>

1. Download the latest `.ankiaddon` file from the [releases tab](https://github.com/glutanimate/progress-bar/releases) (you might need to click on *Assets* below the description to reveal the download links)
2. Open the folder where your downloads are located and double-click on the downloaded `.ankiaddon` file.
3. Follow the installation prompt and restart Anki if it asks you to

</details>

<details>

<summary><i>Older Anki 2.1 versions</i></summary>

1. Make sure you are [using at least Anki 2.1.10](https://apps.ankiweb.net/#download). Earlier releases (e.g. found in various Linux distros) do not support `.ankiaddon` packages.
2. Download the latest `.ankiaddon` package from the [releases tab](https://github.com/glutanimate/progress-bar/releases) (you might need to click on *Assets* below the description to reveal the download links)
3. From Anki's main window, head to *Tools* → *Add-ons*
4. Drag-and-drop the `.ankiaddon` package onto the add-ons list
5. Restart Anki

Video summary:

<img src="https://raw.githubusercontent.com/glutanimate/docs/master/anki/add-ons/media/ankiaddon-installation-macos.gif" width=640>

</details>

### Documentation

For further information on the use of this add-on please check out [the description text](docs/description.md) for AnkiWeb.

### Building

With [Anki add-on builder](https://github.com/glutanimate/anki-addon-builder/) installed:

    git clone https://github.com/glutanimate/progress-bar.git
    cd progress-bar
    aab build

For more information on the build process please refer to [`aab`'s documentation](https://github.com/glutanimate/anki-addon-builder/#usage).

### Contributing

Contributions are welcome! Please review the [contribution guidelines](./CONTRIBUTING.md) on how to:

- Report issues
- File pull requests
- Support the project as a non-developer

### License and Credits

*Progress Bar* is

*Copyright © 2017-2021 [Aristotelis P.](https://glutanimate.com/) (Glutanimate)*
*Copyright © 2018-2020 [liuzikai](https://github.com/liuzikai)*
*Copyright © 2017 [SebastienGllmt](https://github.com/SebastienGllmt)*
*Copyright © 2017 nest0r/Ja-Dark*

This is a fork of an add-on which was removed from AnkiWeb in early 2017. The original was most likely written by nest0r/Ja-Dark. All credit for the original add-on goes to them.

My heartfelt thanks also goes out to Sebastien and liuzikai for their major contributions in fixing longstanding issues and bringing the add-on up-to-speed with recent Anki releases.

For a list of all significant contributors to this project and their contributions please see [CONTRIBUTORS](./CONTRIBUTORS).

Progress Bar is free and open-source software. The add-on code that runs within Anki is released under the GNU AGPLv3 license, extended by a number of additional terms. For more information please see the [LICENSE](https://github.com/glutanimate/progress-bar/blob/master/LICENSE) file that accompanied this program.

Please note that this program uses the [Libaddon](https://github.com/glutanimate/anki-libaddon/) library which comes with [its own additional terms extending the GNU AGPLv3 license](https://github.com/glutanimate/anki-libaddon/blob/master/LICENSE). You may only copy, distribute, or modify the present compilation of this program with Libaddon under the combined licensing terms specified by both licenses.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.


----

<b>
<div align="center">The continued development of this add-on is made possible <br>thanks to my <a href="https://www.patreon.com/glutanimate">Patreon</a> and <a href="https://ko-fi.com/X8X0L4YV">Ko-Fi</a> supporters.
<br>You guys rock ❤️ !</div>
</b>