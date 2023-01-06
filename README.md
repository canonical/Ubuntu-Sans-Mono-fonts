# Ubuntu Mono

[![][Fontbakery]](https://djrrb.github.io/UbuntuMono-fonts/fontbakery/fontbakery-report.html)
[![][Universal]](https://djrrb.github.io/UbuntuMono-fonts/fontbakery/fontbakery-report.html)
[![][GF Profile]](https://djrrb.github.io/UbuntuMono-fonts/fontbakery/fontbakery-report.html)
[![][Outline Correctness]](https://djrrb.github.io/UbuntuMono-fonts/fontbakery/fontbakery-report.html)
[![][Shaping]](https://djrrb.github.io/UbuntuMono-fonts/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdjrrb%2FUbuntuMono-fonts%2Fgh-pages%2Fbadges%2Foverall.json
[GF Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdjrrb%2FUbuntuMono-fonts%2Fgh-pages%2Fbadges%2FGoogleFonts.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdjrrb%2FUbuntuMono-fonts%2Fgh-pages%2Fbadges%2FOutlineCorrectnessChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdjrrb%2FUbuntuMono-fonts%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdjrrb%2FUbuntuMono-fonts%2Fgh-pages%2Fbadges%2FUniversal.json

The **Ubuntu Font Family** are a set of matching libre/open fonts. The fonts were originally developed in 2010–2011, further expanded and improved in 2015, and expanded again in 2022–2023 when variable fonts were added. 

The development is being funded by Canonical Ltd on behalf the wider Free Software community and the Ubuntu project. The technical font design work and implementation has been undertaken by [Dalton Maag](http://daltonmaag.com), [Type Network](http://typenetwork.com), and [DJR Type](http://djr.com).

Both the final font TrueType/OpenType files and the design files used to produce the font family are distributed under an open licence and you are expressly encouraged to experiment, modify, share and improve.

http://font.ubuntu.com/

![Sample Image](documentation/image1.png)

A proportional-width variant, **Ubuntu**, is available in a separate repository: [https://github.com/djrrb/ubuntu-fonts](https://github.com/djrrb/ubuntu-fonts)

## About

Description of you and/or organisation goes here.

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce all font files formats.
* `make dev` will produce only variable font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://djrrb.github.io/UbuntuMono-fonts.

## Changelog

When you update your font (new version or new release), please report all notable changes here, with a date.
[Font Versioning](https://github.com/googlefonts/gf-docs/tree/main/Spec#font-versioning) is based on semver. 
Changelog example:

**26 May 2021. Version 2.13**
- MAJOR Font turned to a variable font.
- SIGNIFICANT New Stylistic sets added.

## License

This Font Software is licensed under the UBUNTU FONT LICENCE Version 1.0
This license is available with a FAQ at
https://ubuntu.com/legal/font-licence