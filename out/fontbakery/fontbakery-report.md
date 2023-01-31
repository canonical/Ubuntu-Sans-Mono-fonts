## Fontbakery report

Fontbakery version: 0.8.11a9

<details><summary><b>[1] Family checks</b></summary><div><details><summary>⚠ <b>WARN:</b> Make sure all font files have the same version value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/family/equal_font_versions">com.google.fonts/check/family/equal_font_versions</a>)</summary><div>


* ⚠ **WARN** Version info differs among font files of the same font project.
These were the version values found:
* fonts/ttf/UbuntuMono-BoldItalic.ttf: 0.863006591796875
* fonts/ttf/UbuntuMono-Bold.ttf: 0.86199951171875
* fonts/ttf/UbuntuMono-Medium.ttf: 0.86199951171875
* fonts/ttf/UbuntuMono-MediumItalic.ttf: 0.863006591796875
* fonts/ttf/UbuntuMono-Italic.ttf: 0.863006591796875
* fonts/ttf/UbuntuMono-Regular.ttf: 0.86199951171875
 [code: mismatch]
</div></details><br></div></details><details><summary><b>[14] UbuntuMono-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x1E9E (LATIN CAPITAL LETTER SHARP S)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.863; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23]" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* .notdef
	* A
	* AE
	* AEacute
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Agrave
	* Alpha and 1048 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acute.asc

	- ampersand.001

	- caron.asc

	- circumflex.asc

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0328 (U+0328) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<200.0,440.0>--<162.0,283.0>> -> L<<162.0,283.0>--<94.0,0.0>>

	* uni01CA (U+01CA): L<<254.0,287.0>--<291.0,444.0>> -> L<<291.0,444.0>--<351.0,693.0>>

	* uni01CB (U+01CB): L<<211.0,440.0>--<171.0,279.0>> -> L<<171.0,279.0>--<104.0,0.0>> 

	* uni01CB (U+01CB): L<<264.0,287.0>--<299.0,432.0>> -> L<<299.0,432.0>--<361.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* M (U+004D): B<<459.0,272.0>-<494.0,408.0>-<528.0,544.0>>/L<<528.0,544.0>--<373.0,245.0>> = 13.365738317706885

	* Mu (U+039C): B<<459.0,272.0>-<494.0,408.0>-<528.0,544.0>>/L<<528.0,544.0>--<373.0,245.0>> = 13.365738317706885

	* W (U+0057): B<<231.5,421.0>-<197.0,285.0>-<162.0,149.0>>/B<<162.0,149.0>-<201.0,224.0>-<239.0,298.5>> = 13.04236869014117

	* Wacute (U+1E82): B<<231.5,421.0>-<197.0,285.0>-<162.0,149.0>>/B<<162.0,149.0>-<201.0,224.0>-<239.0,298.5>> = 13.04236869014117

	* Wcircumflex (U+0174): B<<231.5,421.0>-<197.0,285.0>-<162.0,149.0>>/B<<162.0,149.0>-<201.0,224.0>-<239.0,298.5>> = 13.04236869014117

	* Wdieresis (U+1E84): B<<231.5,421.0>-<197.0,285.0>-<162.0,149.0>>/B<<162.0,149.0>-<201.0,224.0>-<239.0,298.5>> = 13.04236869014117

	* Wgrave (U+1E80): B<<231.5,421.0>-<197.0,285.0>-<162.0,149.0>>/B<<162.0,149.0>-<201.0,224.0>-<239.0,298.5>> = 13.04236869014117

	* uni01CA (U+01CA): B<<197.0,318.5>-<198.0,372.0>-<200.0,440.0>>/L<<200.0,440.0>--<162.0,283.0>> = 11.92141873635303

	* uni01CB (U+01CB): B<<208.0,318.5>-<209.0,372.0>-<211.0,440.0>>/L<<211.0,440.0>--<171.0,279.0>> = 12.26779345018865

	* uni041C (U+041C): B<<459.0,272.0>-<494.0,408.0>-<528.0,544.0>>/L<<528.0,544.0>--<373.0,245.0>> = 13.365738317706885 

	* 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[13] UbuntuMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x1E9E (LATIN CAPITAL LETTER SHARP S)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.862; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23]" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* .notdef
	* A
	* AE
	* AEacute
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Agrave
	* Alpha and 1050 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acute.asc

	- caron.asc

	- circumflex.asc

	- uni030C.alt

	- uni0326.001

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* AE (U+00C6): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457

	* AEacute (U+01FC): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457

	* uni01CA (U+01CA): B<<145.0,318.5>-<133.0,372.0>-<118.0,440.0>>/L<<118.0,440.0>--<118.0,0.0>> = 12.439562018846544

	* uni01CB (U+01CB): B<<145.0,318.5>-<133.0,372.0>-<118.0,440.0>>/L<<118.0,440.0>--<118.0,0.0>> = 12.439562018846544

	* uni01E2 (U+01E2): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457

	* uni04CD (U+04CD): L<<220.0,245.0>--<152.0,539.0>>/L<<152.0,539.0>--<152.0,0.0>> = 13.023079670604968

	* uni04CD (U+04CD): L<<394.0,0.0>--<394.0,539.0>>/L<<394.0,539.0>--<319.0,245.0>> = 14.311041262606418

	* uni04CE (U+04CE): B<<186.0,221.0>-<170.0,296.0>-<153.0,372.0>>/L<<153.0,372.0>--<153.0,0.0>> = 12.60860679336622

	* uni04CE (U+04CE): L<<395.0,0.0>--<395.0,372.0>>/B<<395.0,372.0>-<376.0,296.0>-<357.0,221.0>> = 14.036243467926457 

	* uni04D4 (U+04D4): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* kgreenlandic (U+0138): L<<71.0,525.0>--<209.0,526.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] UbuntuMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x1E9E (LATIN CAPITAL LETTER SHARP S)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.862; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23]" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acute.asc

	- caron.asc

	- circumflex.asc

	- uni030C.alt

	- uni0326.001

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<108.0,468.0>--<113.0,269.0>> -> L<<113.0,269.0>--<113.0,0.0>>

	* uni01CA (U+01CA): L<<232.0,238.0>--<225.0,429.0>> -> L<<225.0,429.0>--<225.0,693.0>>

	* uni01CB (U+01CB): L<<108.0,468.0>--<113.0,281.0>> -> L<<113.0,281.0>--<113.0,0.0>>

	* uni01CB (U+01CB): L<<232.0,238.0>--<225.0,415.0>> -> L<<225.0,415.0>--<225.0,693.0>>

	* uni2116 (U+2116): L<<105.0,452.0>--<111.0,270.0>> -> L<<111.0,270.0>--<111.0,0.0>> 

	* uni2116 (U+2116): L<<230.0,255.0>--<224.0,418.0>> -> L<<224.0,418.0>--<224.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<147.5,308.0>-<128.0,383.0>-<108.0,468.0>>/L<<108.0,468.0>--<113.0,269.0>> = 11.801230287304806

	* uni01CA (U+01CA): L<<110.0,693.0>--<232.0,238.0>>/L<<232.0,238.0>--<225.0,429.0>> = 12.910859041736162

	* uni01CB (U+01CB): B<<147.5,308.0>-<128.0,383.0>-<108.0,468.0>>/L<<108.0,468.0>--<113.0,281.0>> = 11.708912123176166

	* uni01CB (U+01CB): L<<110.0,693.0>--<232.0,238.0>>/L<<232.0,238.0>--<225.0,415.0>> = 12.745010426716286

	* uni2116 (U+2116): L<<106.0,693.0>--<230.0,255.0>>/L<<230.0,255.0>--<224.0,418.0>> = 13.698988776330973 

	* uni2116 (U+2116): L<<229.0,0.0>--<105.0,452.0>>/L<<105.0,452.0>--<111.0,270.0>> = 13.452702757263976 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[13] UbuntuMono-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x1E9E (LATIN CAPITAL LETTER SHARP S)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.863; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23]" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acute.asc

	- ampersand.001

	- caron.asc

	- circumflex.asc

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0328 (U+0328) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<194.0,468.0>--<156.0,282.0>> -> L<<156.0,282.0>--<88.0,0.0>>

	* uni01CA (U+01CA): L<<264.0,238.0>--<301.0,424.0>> -> L<<301.0,424.0>--<366.0,693.0>>

	* uni01CB (U+01CB): L<<205.0,468.0>--<165.0,280.0>> -> L<<165.0,280.0>--<98.0,0.0>> 

	* uni01CB (U+01CB): L<<274.0,238.0>--<311.0,419.0>> -> L<<311.0,419.0>--<377.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<196.0,308.0>-<195.0,383.0>-<194.0,468.0>>/L<<194.0,468.0>--<156.0,282.0>> = 12.220727443911795

	* uni01CA (U+01CA): L<<251.0,693.0>--<264.0,238.0>>/L<<264.0,238.0>--<301.0,424.0>> = 12.887258472111856

	* uni01CB (U+01CB): B<<206.5,308.0>-<205.0,383.0>-<205.0,468.0>>/L<<205.0,468.0>--<165.0,280.0>> = 12.01147838636543 

	* uni01CB (U+01CB): L<<261.0,693.0>--<274.0,238.0>>/L<<274.0,238.0>--<311.0,419.0>> = 13.189802233901787 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] UbuntuMono-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x1E9E (LATIN CAPITAL LETTER SHARP S)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.863; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23]" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* .notdef
	* A
	* AE
	* AEacute
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Agrave
	* Alpha and 780 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acute.asc

	- ampersand.001

	- caron.asc

	- circumflex.asc

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: i	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: igrave	Contours detected: 3	Expected: 2

	- Glyph name: iacute	Contours detected: 3	Expected: 2

	- Glyph name: icircumflex	Contours detected: 3	Expected: 2

	- Glyph name: idieresis	Contours detected: 4	Expected: 3

	- Glyph name: hcircumflex	Contours detected: 1	Expected: 2

	- Glyph name: itilde	Contours detected: 3	Expected: 2

	- Glyph name: imacron	Contours detected: 3	Expected: 2

	- Glyph name: ibreve	Contours detected: 3	Expected: 2 

	- 68 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0328 (U+0328) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<187.0,502.0>--<148.0,280.0>> -> L<<148.0,280.0>--<80.0,0.0>>

	* uni01CA (U+01CA): L<<275.0,180.0>--<314.0,400.0>> -> L<<314.0,400.0>--<385.0,693.0>>

	* uni01CB (U+01CB): L<<197.0,502.0>--<158.0,282.0>> -> L<<158.0,282.0>--<90.0,0.0>> 

	* uni01CB (U+01CB): L<<285.0,180.0>--<325.0,403.0>> -> L<<325.0,403.0>--<396.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* asterisk (U+002A): B<<473.0,408.0>-<505.0,376.0>-<529.0,338.0>>/L<<529.0,338.0>--<528.0,339.0>> = 12.724355685422363

	* uni01CA (U+01CA): B<<195.0,338.0>-<192.0,424.0>-<187.0,502.0>>/L<<187.0,502.0>--<148.0,280.0>> = 13.631592245438554

	* uni01CA (U+01CA): L<<256.0,693.0>--<275.0,180.0>>/L<<275.0,180.0>--<314.0,400.0>> = 12.173641223738318

	* uni01CB (U+01CB): B<<205.5,338.0>-<202.0,424.0>-<197.0,502.0>>/L<<197.0,502.0>--<158.0,282.0>> = 13.720332882608297 

	* uni01CB (U+01CB): L<<266.0,693.0>--<285.0,180.0>>/L<<285.0,180.0>--<325.0,403.0>> = 12.29022473115213 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[13] UbuntuMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x1E9E (LATIN CAPITAL LETTER SHARP S)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.862; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23]" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* .notdef
	* A
	* AE
	* AEacute
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Agrave
	* Alpha and 787 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acute.asc

	- caron.asc

	- circumflex.asc

	- uni030C.alt

	- uni0326.001

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 39	Expected: 46

	- Glyph name: shade	Contours detected: 78	Expected: 85 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<260.0,180.0>--<245.0,396.0>> -> L<<245.0,396.0>--<245.0,693.0>>

	* uni01CA (U+01CA): L<<95.0,502.0>--<108.0,289.0>> -> L<<108.0,289.0>--<108.0,0.0>>

	* uni01CB (U+01CB): L<<260.0,180.0>--<245.0,406.0>> -> L<<245.0,406.0>--<245.0,693.0>>

	* uni01CB (U+01CB): L<<95.0,502.0>--<108.0,281.0>> -> L<<108.0,281.0>--<108.0,0.0>>

	* uni2116 (U+2116): L<<261.0,168.0>--<247.0,405.0>> -> L<<247.0,405.0>--<247.0,693.0>> 

	* uni2116 (U+2116): L<<96.0,514.0>--<109.0,289.0>> -> L<<109.0,289.0>--<109.0,0.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<141.5,338.0>-<118.0,424.0>-<95.0,502.0>>/L<<95.0,502.0>--<108.0,289.0>> = 12.936708290677316

	* uni01CA (U+01CA): L<<117.0,693.0>--<260.0,180.0>>/L<<260.0,180.0>--<245.0,396.0>> = 11.603445579167502

	* uni01CB (U+01CB): B<<141.5,338.0>-<118.0,424.0>-<95.0,502.0>>/L<<95.0,502.0>--<108.0,281.0>> = 13.06284078810359

	* uni01CB (U+01CB): L<<117.0,693.0>--<260.0,180.0>>/L<<260.0,180.0>--<245.0,406.0>> = 11.778693639479739

	* uni024A (U+024A): L<<408.0,-1.0>--<408.0,82.0>>/B<<408.0,82.0>-<398.0,41.0>-<357.0,13.0>> = 13.706961004079783

	* uni2116 (U+2116): L<<120.0,693.0>--<261.0,168.0>>/L<<261.0,168.0>--<247.0,405.0>> = 11.6526258660711 

	* uni2116 (U+2116): L<<236.0,0.0>--<96.0,514.0>>/L<<96.0,514.0>--<109.0,289.0>> = 11.929506309926724 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 30 | 50 | 715 | 43 | 485 | 0 |
| 0% | 2% | 4% | 54% | 3% | 37% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
