## Fontbakery report

Fontbakery version: 0.8.8

<details><summary><b>[2] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** sTypoLineGap is not the same across the family:
Ubuntu Mono Regular: 56
Ubuntu Mono Medium: 56
Ubuntu Mono Bold: 56
Ubuntu Mono Italic: 6
Ubuntu Mono Bold Italic: 6
Ubuntu Mono Medium Italic: 6 [code: sTypoLineGap-mismatch]
</div></details><details><summary>🔥 <b>FAIL:</b> Fonts have consistent underline thickness? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/post.html#com.google.fonts/check/family/underline_thickness">com.google.fonts/check/family/underline_thickness</a>)</summary><div>


* 🔥 **FAIL** Thickness of the underline is not the same across this family. In order to fix this, please make sure that the underlineThickness value is the same in the 'post' table of all of this family font files.
Detected underlineThickness values are:
	fonts/ttf/UbuntuMono-Regular.ttf: 79
	fonts/ttf/UbuntuMono-Medium.ttf: 101
	fonts/ttf/UbuntuMono-Bold.ttf: 120
	fonts/ttf/UbuntuMono-Italic.ttf: 79
	fonts/ttf/UbuntuMono-BoldItalic.ttf: 120
	fonts/ttf/UbuntuMono-MediumItalic.ttf: 101
 [code: inconsistent-underline-thickness]
</div></details><br></div></details><details><summary><b>[19] UbuntuMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.861; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** fsSelection bit 7 needs to be enabled because the win metrics differ from the family on Google Fonts. [code: bad-fsselection-bit7]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 776 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -185 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/UbuntuMono-Regular.ttf', 'fonts/ttf/UbuntuMono-Medium.ttf', 'fonts/ttf/UbuntuMono-Bold.ttf', 'fonts/ttf/UbuntuMono-Italic.ttf', 'fonts/ttf/UbuntuMono-BoldItalic.ttf', 'fonts/ttf/UbuntuMono-MediumItalic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 954, but got 932 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 191, but got 189 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (776) and hhea ascent (932) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1F77
	* uni0495
	* questiondown
	* uni0229
	* uni04B7
	* Bracketleft
	* uni1F9F
	* braceright
	* six.sups
	* uni1FB0 and 1023 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni256B.001
	- uni256A.001
	- acute.asc
	- caron.asc
	- uni030C.alt 
	- And circumflex.asc
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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
	- And Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 dieresistonos (U+0385), tonos (U+0384), tonos.cap (unencoded), uni1FBD (U+1FBD), uni1FBF (U+1FBF), uni1FC0 (U+1FC0), uni1FC1 (U+1FC1), uni1FCD (U+1FCD), uni1FCE (U+1FCE), uni1FCF (U+1FCF) and 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 breve_inverted (U+0311) and uni030F (U+030F) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0384, U+0385, U+1FBD, U+1FBF, U+1FC0, U+1FC1, U+1FCD, U+1FCE, U+1FCF, U+1FDD and 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* uni01CA (U+01CA): L<<100.0,488.0>--<110.0,281.0>> -> L<<110.0,281.0>--<110.0,0.0>>
	* uni01CA (U+01CA): L<<248.0,205.0>--<237.0,410.0>> -> L<<237.0,410.0>--<237.0,693.0>>
	* uni01CB (U+01CB): L<<100.0,488.0>--<110.0,281.0>> -> L<<110.0,281.0>--<110.0,0.0>>
	* uni01CB (U+01CB): L<<248.0,205.0>--<237.0,410.0>> -> L<<237.0,410.0>--<237.0,693.0>>
	* uni2116 (U+2116): L<<100.0,488.0>--<110.0,281.0>> -> L<<110.0,281.0>--<110.0,0.0>> and uni2116 (U+2116): L<<248.0,205.0>--<237.0,410.0>> -> L<<237.0,410.0>--<237.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni01CA (U+01CA): B<<166.0,244.5>-<133.0,367.0>-<100.0,488.0>>/L<<100.0,488.0>--<110.0,281.0>> = 12.48935686880825
	* uni01CA (U+01CA): L<<114.0,693.0>--<248.0,205.0>>/L<<248.0,205.0>--<237.0,410.0>> = 12.282955931130896
	* uni01CB (U+01CB): B<<166.0,244.5>-<133.0,367.0>-<100.0,488.0>>/L<<100.0,488.0>--<110.0,281.0>> = 12.48935686880825
	* uni01CB (U+01CB): L<<114.0,693.0>--<248.0,205.0>>/L<<248.0,205.0>--<237.0,410.0>> = 12.282955931130896
	* uni2116 (U+2116): L<<114.0,693.0>--<248.0,205.0>>/L<<248.0,205.0>--<237.0,410.0>> = 12.282955931130896 and uni2116 (U+2116): L<<233.0,0.0>--<100.0,488.0>>/L<<100.0,488.0>--<110.0,281.0>> = 12.47942175888303 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[18] UbuntuMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.861; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** fsSelection bit 7 needs to be enabled because the win metrics differ from the family on Google Fonts. [code: bad-fsselection-bit7]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 776 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -185 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/UbuntuMono-Regular.ttf', 'fonts/ttf/UbuntuMono-Medium.ttf', 'fonts/ttf/UbuntuMono-Bold.ttf', 'fonts/ttf/UbuntuMono-Italic.ttf', 'fonts/ttf/UbuntuMono-BoldItalic.ttf', 'fonts/ttf/UbuntuMono-MediumItalic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 954, but got 932 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 191, but got 189 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (776) and hhea ascent (932) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni256B.001
	- uni256A.001
	- acute.asc
	- caron.asc
	- uni030C.alt 
	- And circumflex.asc
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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
	- And Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 dieresistonos (U+0385), tonos (U+0384), tonos.cap (unencoded), uni1FBD (U+1FBD), uni1FBF (U+1FBF), uni1FC0 (U+1FC0), uni1FC1 (U+1FC1), uni1FCD (U+1FCD), uni1FCE (U+1FCE), uni1FCF (U+1FCF) and 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 breve_inverted (U+0311) and uni030F (U+030F) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0384, U+0385, U+1FBD, U+1FBF, U+1FC0, U+1FC1, U+1FCD, U+1FCE, U+1FCF, U+1FDD and 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* uni01CA (U+01CA): L<<110.0,462.0>--<114.0,266.0>> -> L<<114.0,266.0>--<114.0,0.0>>
	* uni01CA (U+01CA): L<<227.0,250.0>--<222.0,435.0>> -> L<<222.0,435.0>--<222.0,693.0>>
	* uni01CB (U+01CB): L<<110.0,462.0>--<114.0,281.0>> -> L<<114.0,281.0>--<114.0,0.0>>
	* uni01CB (U+01CB): L<<227.0,250.0>--<222.0,417.0>> -> L<<222.0,417.0>--<222.0,693.0>>
	* uni2116 (U+2116): L<<107.0,440.0>--<111.0,267.0>> -> L<<111.0,267.0>--<111.0,0.0>> and uni2116 (U+2116): L<<224.0,272.0>--<220.0,420.0>> -> L<<220.0,420.0>--<220.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni01CA (U+01CA): B<<148.5,302.5>-<130.0,376.0>-<110.0,462.0>>/L<<110.0,462.0>--<114.0,266.0>> = 11.922753736439402
	* uni01CA (U+01CA): L<<109.0,693.0>--<227.0,250.0>>/L<<227.0,250.0>--<222.0,435.0>> = 13.367158375322333
	* uni01CB (U+01CB): B<<148.5,302.5>-<130.0,376.0>-<110.0,462.0>>/L<<110.0,462.0>--<114.0,281.0>> = 11.825894063952093
	* uni01CB (U+01CB): L<<109.0,693.0>--<227.0,250.0>>/L<<227.0,250.0>--<222.0,417.0>> = 13.200385878773703 and uni2116 (U+2116): L<<228.0,0.0>--<107.0,440.0>>/L<<107.0,440.0>--<111.0,267.0>> = 14.051729336534981 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] UbuntuMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.861; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** fsSelection bit 7 needs to be enabled because the win metrics differ from the family on Google Fonts. [code: bad-fsselection-bit7]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 776 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -185 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/UbuntuMono-Regular.ttf', 'fonts/ttf/UbuntuMono-Medium.ttf', 'fonts/ttf/UbuntuMono-Bold.ttf', 'fonts/ttf/UbuntuMono-Italic.ttf', 'fonts/ttf/UbuntuMono-BoldItalic.ttf', 'fonts/ttf/UbuntuMono-MediumItalic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 954, but got 932 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 191, but got 189 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (776) and hhea ascent (932) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1F77
	* uni0495
	* questiondown
	* uni0229
	* uni04B7
	* Bracketleft
	* uni1F9F
	* braceright
	* six.sups
	* uni1FB0 and 1051 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni256B.001
	- uni256A.001
	- acute.asc
	- caron.asc
	- uni030C.alt 
	- And circumflex.asc
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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
	- And Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 dieresistonos (U+0385), tonos (U+0384), tonos.cap (unencoded), uni1FBD (U+1FBD), uni1FBF (U+1FBF), uni1FC0 (U+1FC0), uni1FC1 (U+1FC1), uni1FCD (U+1FCD), uni1FCE (U+1FCE), uni1FCF (U+1FCF) and 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 breve_inverted (U+0311) and uni030F (U+030F) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0384, U+0385, U+1FBD, U+1FBF, U+1FC0, U+1FC1, U+1FCD, U+1FCE, U+1FCF, U+1FDD and 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* AE (U+00C6): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457
	* AEacute (U+01FC): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457
	* uni01CA (U+01CA): B<<145.0,318.5>-<133.0,372.0>-<118.0,440.0>>/L<<118.0,440.0>--<118.0,0.0>> = 12.439562018846544
	* uni01CB (U+01CB): B<<145.0,318.5>-<133.0,372.0>-<118.0,440.0>>/L<<118.0,440.0>--<118.0,0.0>> = 12.439562018846544
	* uni01E2 (U+01E2): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457
	* uni04CD (U+04CD): L<<220.0,245.0>--<152.0,539.0>>/L<<152.0,539.0>--<152.0,0.0>> = 13.023079670604968
	* uni04CD (U+04CD): L<<394.0,0.0>--<394.0,539.0>>/L<<394.0,539.0>--<319.0,245.0>> = 14.311041262606418
	* uni04CE (U+04CE): B<<186.0,221.0>-<170.0,296.0>-<153.0,372.0>>/L<<153.0,372.0>--<153.0,0.0>> = 12.60860679336622
	* uni04CE (U+04CE): L<<395.0,0.0>--<395.0,372.0>>/B<<395.0,372.0>-<376.0,296.0>-<357.0,221.0>> = 14.036243467926457 and uni04D4 (U+04D4): L<<286.0,274.0>--<286.0,600.0>>/B<<286.0,600.0>-<267.0,524.0>-<247.5,445.5>> = 14.036243467926457 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * kgreenlandic (U+0138): L<<71.0,525.0>--<209.0,526.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[17] UbuntuMono-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.861; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** fsSelection bit 7 needs to be enabled because the win metrics differ from the family on Google Fonts. [code: bad-fsselection-bit7]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 776 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -185 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/UbuntuMono-Regular.ttf', 'fonts/ttf/UbuntuMono-Medium.ttf', 'fonts/ttf/UbuntuMono-Bold.ttf', 'fonts/ttf/UbuntuMono-Italic.ttf', 'fonts/ttf/UbuntuMono-BoldItalic.ttf', 'fonts/ttf/UbuntuMono-MediumItalic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 954, but got 932 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 191, but got 189 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (776) and hhea ascent (932) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1F77
	* uni0495
	* questiondown
	* uni0229
	* uni04B7
	* Bracketleft
	* uni1F9F
	* braceright
	* six.sups
	* uni1FB0 and 1022 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni256B.001
	- ampersand.001
	- uni256A.001
	- acute.asc
	- caron.asc
	- uni030C.alt 
	- And circumflex.asc
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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
	- And Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 breve_inverted (U+0311), uni030F (U+030F) and uni0328 (U+0328) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* uni01CA (U+01CA): L<<190.0,488.0>--<151.0,281.0>> -> L<<151.0,281.0>--<83.0,0.0>>
	* uni01CA (U+01CA): L<<270.0,205.0>--<309.0,410.0>> -> L<<309.0,410.0>--<377.0,693.0>>
	* uni01CB (U+01CB): L<<200.0,488.0>--<161.0,281.0>> -> L<<161.0,281.0>--<93.0,0.0>> and uni01CB (U+01CB): L<<280.0,205.0>--<319.0,410.0>> -> L<<319.0,410.0>--<388.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni01CA (U+01CA): B<<198.5,244.5>-<195.0,367.0>-<190.0,488.0>>/L<<190.0,488.0>--<151.0,281.0>> = 13.036030795952431
	* uni01CA (U+01CA): L<<254.0,693.0>--<270.0,205.0>>/L<<270.0,205.0>--<309.0,410.0>> = 12.649331607483349
	* uni01CB (U+01CB): B<<208.5,244.5>-<205.0,367.0>-<200.0,488.0>>/L<<200.0,488.0>--<161.0,281.0>> = 13.036030795952431 and uni01CB (U+01CB): L<<264.0,693.0>--<280.0,205.0>>/L<<280.0,205.0>--<319.0,410.0>> = 12.649331607483349 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[17] UbuntuMono-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.861; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** fsSelection bit 7 needs to be enabled because the win metrics differ from the family on Google Fonts. [code: bad-fsselection-bit7]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 776 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -185 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/UbuntuMono-Regular.ttf', 'fonts/ttf/UbuntuMono-Medium.ttf', 'fonts/ttf/UbuntuMono-Bold.ttf', 'fonts/ttf/UbuntuMono-Italic.ttf', 'fonts/ttf/UbuntuMono-BoldItalic.ttf', 'fonts/ttf/UbuntuMono-MediumItalic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 954, but got 932 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 191, but got 189 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (776) and hhea ascent (932) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1F77
	* uni0495
	* questiondown
	* uni0229
	* uni04B7
	* Bracketleft
	* uni1F9F
	* braceright
	* six.sups
	* uni1FB0 and 1049 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni256B.001
	- ampersand.001
	- uni256A.001
	- acute.asc
	- caron.asc
	- uni030C.alt 
	- And circumflex.asc
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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
	- And Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 breve_inverted (U+0311), uni030F (U+030F) and uni0328 (U+0328) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* uni01CA (U+01CA): L<<200.0,440.0>--<162.0,283.0>> -> L<<162.0,283.0>--<94.0,0.0>>
	* uni01CA (U+01CA): L<<254.0,287.0>--<291.0,444.0>> -> L<<291.0,444.0>--<351.0,693.0>>
	* uni01CB (U+01CB): L<<211.0,440.0>--<171.0,279.0>> -> L<<171.0,279.0>--<104.0,0.0>> and uni01CB (U+01CB): L<<264.0,287.0>--<299.0,432.0>> -> L<<299.0,432.0>--<361.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


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
	* uni041C (U+041C): B<<459.0,272.0>-<494.0,408.0>-<528.0,544.0>>/L<<528.0,544.0>--<373.0,245.0>> = 13.365738317706885 and 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] UbuntuMono-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.861; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** fsSelection bit 7 needs to be enabled because the win metrics differ from the family on Google Fonts. [code: bad-fsselection-bit7]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 776 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -185 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/UbuntuMono-Regular.ttf', 'fonts/ttf/UbuntuMono-Medium.ttf', 'fonts/ttf/UbuntuMono-Bold.ttf', 'fonts/ttf/UbuntuMono-Italic.ttf', 'fonts/ttf/UbuntuMono-BoldItalic.ttf', 'fonts/ttf/UbuntuMono-MediumItalic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 954, but got 932 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 191, but got 189 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (776) and hhea ascent (932) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni256B.001
	- ampersand.001
	- uni256A.001
	- acute.asc
	- caron.asc
	- uni030C.alt 
	- And circumflex.asc
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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
	- And Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 breve_inverted (U+0311), uni030F (U+030F) and uni0328 (U+0328) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* uni01CA (U+01CA): L<<195.0,462.0>--<157.0,282.0>> -> L<<157.0,282.0>--<89.0,0.0>>
	* uni01CA (U+01CA): L<<261.0,250.0>--<299.0,429.0>> -> L<<299.0,429.0>--<363.0,693.0>>
	* uni01CB (U+01CB): L<<206.0,462.0>--<166.0,280.0>> -> L<<166.0,280.0>--<99.0,0.0>> and uni01CB (U+01CB): L<<271.0,250.0>--<308.0,422.0>> -> L<<308.0,422.0>--<373.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni01CA (U+01CA): B<<196.0,302.5>-<195.0,376.0>-<195.0,462.0>>/L<<195.0,462.0>--<157.0,282.0>> = 11.920738539922306
	* uni01CA (U+01CA): L<<250.0,693.0>--<261.0,250.0>>/L<<261.0,250.0>--<299.0,429.0>> = 13.407816132757718
	* uni01CB (U+01CB): B<<206.5,302.5>-<206.0,376.0>-<206.0,462.0>>/L<<206.0,462.0>--<166.0,280.0>> = 12.395406833758457
	* uni01CB (U+01CB): L<<260.0,693.0>--<271.0,250.0>>/L<<271.0,250.0>--<308.0,422.0>> = 13.562649973956185
	* uni1F88 (U+1F88): B<<301.5,528.5>-<304.0,572.0>-<307.0,601.0>>/B<<307.0,601.0>-<281.0,528.0>-<250.0,442.0>> = 13.69794703705892
	* uni1F89 (U+1F89): B<<301.5,528.5>-<304.0,572.0>-<307.0,601.0>>/B<<307.0,601.0>-<281.0,528.0>-<250.0,442.0>> = 13.69794703705892
	* uni1F8A (U+1F8A): B<<301.5,528.5>-<304.0,572.0>-<307.0,601.0>>/B<<307.0,601.0>-<281.0,528.0>-<250.0,442.0>> = 13.69794703705892
	* uni1F8B (U+1F8B): B<<301.5,528.5>-<304.0,572.0>-<307.0,601.0>>/B<<307.0,601.0>-<281.0,528.0>-<250.0,442.0>> = 13.69794703705892
	* uni1F8C (U+1F8C): B<<301.5,528.5>-<304.0,572.0>-<307.0,601.0>>/B<<307.0,601.0>-<281.0,528.0>-<250.0,442.0>> = 13.69794703705892
	* uni1F8D (U+1F8D): B<<301.5,528.5>-<304.0,572.0>-<307.0,601.0>>/B<<307.0,601.0>-<281.0,528.0>-<250.0,442.0>> = 13.69794703705892 and 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 44 | 64 | 656 | 43 | 463 | 0 |
| 0% | 3% | 5% | 52% | 3% | 36% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
