## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[11] UbuntuSansMono-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1340 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Ubuntu Sans Mono Medium' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<152.0,468.0>--<114.0,282.0>> -> L<<114.0,282.0>--<46.0,0.0>>

	* uni01CA (U+01CA): L<<222.0,238.0>--<259.0,424.0>> -> L<<259.0,424.0>--<324.0,693.0>>

	* uni01CB (U+01CB): L<<163.0,468.0>--<123.0,280.0>> -> L<<123.0,280.0>--<56.0,0.0>> 

	* uni01CB (U+01CB): L<<232.0,238.0>--<269.0,419.0>> -> L<<269.0,419.0>--<335.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<154.0,308.0>-<153.0,383.0>-<152.0,468.0>>/L<<152.0,468.0>--<114.0,282.0>> = 12.220727443911795

	* uni01CA (U+01CA): L<<209.0,693.0>--<222.0,238.0>>/L<<222.0,238.0>--<259.0,424.0>> = 12.887258472111856

	* uni01CB (U+01CB): B<<164.5,308.0>-<163.0,383.0>-<163.0,468.0>>/L<<163.0,468.0>--<123.0,280.0>> = 12.01147838636543 

	* uni01CB (U+01CB): L<<219.0,693.0>--<232.0,238.0>>/L<<232.0,238.0>--<269.0,419.0>> = 13.189802233901787 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] UbuntuSansMono-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1339 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Ubuntu Sans Mono ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni01C4	Contours detected: 5	Expected: 4

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: uni01C4	Contours detected: 5	Expected: 4 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two (U+0032) contains a short segment B<<98.0,0.0>-<97.0,8.0>-<97.0,12.0>>

	* two (U+0032) contains a short segment B<<97.0,12.0>-<97.0,16.0>-<97.0,21.0>>

	* three (U+0033) contains a short segment L<<206.0,392.0>--<223.0,392.0>>

	* at (U+0040) contains a short segment B<<411.0,475.0>-<424.0,475.0>-<434.5,474.0>>

	* at (U+0040) contains a short segment B<<434.5,474.0>-<445.0,473.0>-<457.0,470.0>>

	* sterling (U+00A3) contains a short segment L<<206.0,316.0>--<206.0,305.0>>

	* onehalf (U+00BD) contains a short segment B<<321.0,9.0>-<321.0,16.0>-<321.0,17.0>>

	* ae (U+00E6) contains a short segment B<<531.5,262.5>-<531.0,256.0>-<531.0,251.0>>

	* eogonek (U+0119) contains a short segment B<<500.0,285.0>-<500.0,278.0>-<499.5,269.5>>

	* eogonek (U+0119) contains a short segment B<<499.5,269.5>-<499.0,261.0>-<498.0,253.0>> 

	* 85 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<266.0,125.0>--<259.0,250.0>> -> L<<259.0,250.0>--<259.0,693.0>>

	* uni01CA (U+01CA): L<<91.0,580.0>--<97.0,446.0>> -> L<<97.0,446.0>--<97.0,0.0>>

	* uni01CB (U+01CB): L<<273.0,125.0>--<266.0,253.0>> -> L<<266.0,253.0>--<266.0,693.0>>

	* uni01CB (U+01CB): L<<98.0,580.0>--<105.0,444.0>> -> L<<105.0,444.0>--<105.0,0.0>>

	* uni2116 (U+2116): L<<260.0,121.0>--<253.0,253.0>> -> L<<253.0,253.0>--<253.0,693.0>> 

	* uni2116 (U+2116): L<<88.0,584.0>--<94.0,446.0>> -> L<<94.0,446.0>--<94.0,0.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<172.5,290.5>-<131.0,438.0>-<91.0,580.0>>/L<<91.0,580.0>--<97.0,446.0>> = 13.16823457364228

	* uni01CA (U+01CA): L<<108.0,693.0>--<266.0,125.0>>/L<<266.0,125.0>--<259.0,250.0>> = 12.339703410390847

	* uni01CB (U+01CB): B<<180.0,290.5>-<139.0,438.0>-<98.0,580.0>>/L<<98.0,580.0>--<105.0,444.0>> = 13.158694704136535

	* uni01CB (U+01CB): L<<115.0,693.0>--<273.0,125.0>>/L<<273.0,125.0>--<266.0,253.0>> = 12.41467447918525

	* uni2116 (U+2116): L<<105.0,693.0>--<260.0,121.0>>/L<<260.0,121.0>--<253.0,253.0>> = 12.12627548922312 

	* uni2116 (U+2116): L<<247.0,0.0>--<88.0,584.0>>/L<<88.0,584.0>--<94.0,446.0>> = 12.740658183940608 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* I (U+0049): L<<255.0,43.0>--<256.0,650.0>>

	* I (U+0049): L<<305.0,650.0>--<304.0,43.0>>

	* Iacute (U+00CD): L<<255.0,43.0>--<256.0,650.0>>

	* Iacute (U+00CD): L<<305.0,650.0>--<304.0,43.0>>

	* Ibreve (U+012C): L<<255.0,43.0>--<256.0,650.0>>

	* Ibreve (U+012C): L<<305.0,650.0>--<304.0,43.0>>

	* Icircumflex (U+00CE): L<<255.0,43.0>--<256.0,650.0>>

	* Icircumflex (U+00CE): L<<305.0,650.0>--<304.0,43.0>>

	* Idieresis (U+00CF): L<<255.0,43.0>--<256.0,650.0>>

	* Idieresis (U+00CF): L<<305.0,650.0>--<304.0,43.0>> 

	* 63 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] UbuntuSansMono-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1340 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: i	Contours detected: 3	Expected: 2

	- Glyph name: igrave	Contours detected: 3	Expected: 2

	- Glyph name: iacute	Contours detected: 3	Expected: 2

	- Glyph name: icircumflex	Contours detected: 3	Expected: 2

	- Glyph name: idieresis	Contours detected: 4	Expected: 3

	- Glyph name: itilde	Contours detected: 3	Expected: 2

	- Glyph name: imacron	Contours detected: 3	Expected: 2

	- Glyph name: ibreve	Contours detected: 3	Expected: 2

	- Glyph name: dotlessi	Contours detected: 2	Expected: 1

	- Glyph name: uni01D0	Contours detected: 3	Expected: 2 

	- 68 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<145.0,502.0>--<106.0,280.0>> -> L<<106.0,280.0>--<38.0,0.0>>

	* uni01CA (U+01CA): L<<233.0,180.0>--<272.0,400.0>> -> L<<272.0,400.0>--<343.0,693.0>>

	* uni01CB (U+01CB): L<<155.0,502.0>--<116.0,282.0>> -> L<<116.0,282.0>--<48.0,0.0>> 

	* uni01CB (U+01CB): L<<243.0,180.0>--<283.0,403.0>> -> L<<283.0,403.0>--<354.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* asterisk (U+002A): B<<431.0,408.0>-<463.0,376.0>-<487.0,338.0>>/L<<487.0,338.0>--<486.0,339.0>> = 12.724355685422363

	* uni01CA (U+01CA): B<<153.0,338.0>-<150.0,424.0>-<145.0,502.0>>/L<<145.0,502.0>--<106.0,280.0>> = 13.631592245438554

	* uni01CA (U+01CA): L<<214.0,693.0>--<233.0,180.0>>/L<<233.0,180.0>--<272.0,400.0>> = 12.173641223738318

	* uni01CB (U+01CB): B<<163.5,338.0>-<160.0,424.0>-<155.0,502.0>>/L<<155.0,502.0>--<116.0,282.0>> = 13.720332882608297 

	* uni01CB (U+01CB): L<<224.0,693.0>--<243.0,180.0>>/L<<243.0,180.0>--<283.0,403.0>> = 12.29022473115213 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] UbuntuSansMono-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1340 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Ubuntu Sans Mono SemiBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<155.0,454.0>--<117.0,282.0>> -> L<<117.0,282.0>--<49.0,0.0>>

	* uni01CA (U+01CA): L<<217.0,263.0>--<254.0,434.0>> -> L<<254.0,434.0>--<317.0,693.0>>

	* uni01CB (U+01CB): L<<166.0,454.0>--<126.0,280.0>> -> L<<126.0,280.0>--<59.0,0.0>> 

	* uni01CB (U+01CB): L<<227.0,263.0>--<263.0,425.0>> -> L<<263.0,425.0>--<327.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): B<<183.0,419.0>-<148.0,275.0>-<114.0,138.0>>/B<<114.0,138.0>-<152.0,210.0>-<193.5,288.0>> = 13.886299175999017

	* Wacute (U+1E82): B<<183.0,419.0>-<148.0,275.0>-<114.0,138.0>>/B<<114.0,138.0>-<152.0,210.0>-<193.5,288.0>> = 13.886299175999017

	* Wcircumflex (U+0174): B<<183.0,419.0>-<148.0,275.0>-<114.0,138.0>>/B<<114.0,138.0>-<152.0,210.0>-<193.5,288.0>> = 13.886299175999017

	* Wdieresis (U+1E84): B<<183.0,419.0>-<148.0,275.0>-<114.0,138.0>>/B<<114.0,138.0>-<152.0,210.0>-<193.5,288.0>> = 13.886299175999017

	* Wgrave (U+1E80): B<<183.0,419.0>-<148.0,275.0>-<114.0,138.0>>/B<<114.0,138.0>-<152.0,210.0>-<193.5,288.0>> = 13.886299175999017

	* uni01CA (U+01CA): B<<154.5,295.0>-<154.0,366.0>-<155.0,454.0>>/L<<155.0,454.0>--<117.0,282.0>> = 11.807186059775386

	* uni01CA (U+01CA): L<<206.0,693.0>--<217.0,263.0>>/L<<217.0,263.0>--<254.0,434.0>> = 13.674506148381406

	* uni01CB (U+01CB): B<<165.0,295.0>-<165.0,366.0>-<166.0,454.0>>/L<<166.0,454.0>--<126.0,280.0>> = 12.295449135407413

	* uni01CB (U+01CB): L<<216.0,693.0>--<227.0,263.0>>/L<<227.0,263.0>--<263.0,425.0>> = 13.994194099036692

	* uni04CD (U+04CD): B<<398.5,274.0>-<433.0,417.0>-<466.0,554.0>>/L<<466.0,554.0>--<310.0,250.0>> = 13.621808414887182 

	* uni04CE (U+04CE): B<<370.5,185.0>-<393.0,279.0>-<414.0,373.0>>/B<<414.0,373.0>-<381.0,308.0>-<346.0,243.0>> = 14.323224660848188 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] UbuntuSansMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1339 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Ubuntu Sans Mono Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
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

	* uni2116 (U+2116): L<<230.0,255.0>--<224.0,418.0>> -> L<<224.0,418.0>--<224.0,693.0>>

	* uni2713 (U+2713): L<<205.0,226.0>--<217.0,243.0>> -> L<<217.0,243.0>--<485.0,602.0>> 

	* uni2713 (U+2713): L<<83.0,383.0>--<193.0,243.0>> -> L<<193.0,243.0>--<205.0,226.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<147.5,308.0>-<128.0,383.0>-<108.0,468.0>>/L<<108.0,468.0>--<113.0,269.0>> = 11.801230287304806

	* uni01CA (U+01CA): L<<110.0,693.0>--<232.0,238.0>>/L<<232.0,238.0>--<225.0,429.0>> = 12.910859041736162

	* uni01CB (U+01CB): B<<147.5,308.0>-<128.0,383.0>-<108.0,468.0>>/L<<108.0,468.0>--<113.0,281.0>> = 11.708912123176166

	* uni01CB (U+01CB): L<<110.0,693.0>--<232.0,238.0>>/L<<232.0,238.0>--<225.0,415.0>> = 12.745010426716288

	* uni2116 (U+2116): L<<106.0,693.0>--<230.0,255.0>>/L<<230.0,255.0>--<224.0,418.0>> = 13.698988776330973 

	* uni2116 (U+2116): L<<229.0,0.0>--<105.0,452.0>>/L<<105.0,452.0>--<111.0,270.0>> = 13.452702757263976 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] UbuntuSansMono-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1340 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<158.0,440.0>--<120.0,283.0>> -> L<<120.0,283.0>--<52.0,0.0>>

	* uni01CA (U+01CA): L<<212.0,287.0>--<249.0,444.0>> -> L<<249.0,444.0>--<309.0,693.0>>

	* uni01CB (U+01CB): L<<169.0,440.0>--<129.0,279.0>> -> L<<129.0,279.0>--<62.0,0.0>> 

	* uni01CB (U+01CB): L<<222.0,287.0>--<257.0,432.0>> -> L<<257.0,432.0>--<319.0,693.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* M (U+004D): B<<417.0,272.0>-<452.0,408.0>-<486.0,544.0>>/L<<486.0,544.0>--<331.0,245.0>> = 13.365738317706885

	* Mu (U+039C): B<<417.0,272.0>-<452.0,408.0>-<486.0,544.0>>/L<<486.0,544.0>--<331.0,245.0>> = 13.365738317706885

	* W (U+0057): B<<189.5,421.0>-<155.0,285.0>-<120.0,149.0>>/B<<120.0,149.0>-<159.0,224.0>-<197.0,298.5>> = 13.04236869014117

	* Wacute (U+1E82): B<<189.5,421.0>-<155.0,285.0>-<120.0,149.0>>/B<<120.0,149.0>-<159.0,224.0>-<197.0,298.5>> = 13.04236869014117

	* Wcircumflex (U+0174): B<<189.5,421.0>-<155.0,285.0>-<120.0,149.0>>/B<<120.0,149.0>-<159.0,224.0>-<197.0,298.5>> = 13.04236869014117

	* Wdieresis (U+1E84): B<<189.5,421.0>-<155.0,285.0>-<120.0,149.0>>/B<<120.0,149.0>-<159.0,224.0>-<197.0,298.5>> = 13.04236869014117

	* Wgrave (U+1E80): B<<189.5,421.0>-<155.0,285.0>-<120.0,149.0>>/B<<120.0,149.0>-<159.0,224.0>-<197.0,298.5>> = 13.04236869014117

	* uni01CA (U+01CA): B<<155.0,318.5>-<156.0,372.0>-<158.0,440.0>>/L<<158.0,440.0>--<120.0,283.0>> = 11.92141873635303

	* uni01CB (U+01CB): B<<166.0,318.5>-<167.0,372.0>-<169.0,440.0>>/L<<169.0,440.0>--<129.0,279.0>> = 12.26779345018865

	* uni041C (U+041C): B<<417.0,272.0>-<452.0,408.0>-<486.0,544.0>>/L<<486.0,544.0>--<331.0,245.0>> = 13.365738317706885 

	* 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] UbuntuSansMono-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1339 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Ubuntu Sans Mono Thin' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two (U+0032) contains a short segment B<<106.0,0.0>-<105.0,9.0>-<105.0,14.0>>

	* two (U+0032) contains a short segment B<<105.0,14.0>-<105.0,19.0>-<105.0,24.0>>

	* three (U+0033) contains a short segment L<<211.0,386.0>--<222.0,386.0>>

	* sterling (U+00A3) contains a short segment L<<196.0,321.0>--<196.0,311.0>>

	* ae (U+00E6) contains a short segment B<<531.5,267.5>-<531.0,261.0>-<531.0,256.0>>

	* Aogonek (U+0104) contains a short segment B<<515.0,-159.0>-<522.0,-159.0>-<530.0,-157.5>>

	* aogonek (U+0105) contains a short segment B<<431.0,-155.0>-<438.0,-155.0>-<446.0,-153.5>>

	* Eogonek (U+0118) contains a short segment B<<463.0,-155.0>-<470.0,-155.0>-<478.0,-153.5>>

	* Eogonek (U+0118) contains a short segment B<<478.0,-153.5>-<486.0,-152.0>-<496.0,-150.0>>

	* eogonek (U+0119) contains a short segment B<<413.0,-155.0>-<420.0,-155.0>-<428.0,-153.5>> 

	* 67 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<269.0,98.0>--<266.0,177.0>> -> L<<266.0,177.0>--<266.0,693.0>>

	* uni01CA (U+01CA): L<<89.0,619.0>--<92.0,525.0>> -> L<<92.0,525.0>--<92.0,0.0>>

	* uni01CB (U+01CB): L<<100.0,619.0>--<103.0,525.0>> -> L<<103.0,525.0>--<103.0,0.0>>

	* uni01CB (U+01CB): L<<280.0,98.0>--<277.0,177.0>> -> L<<277.0,177.0>--<277.0,693.0>>

	* uni2116 (U+2116): L<<259.0,98.0>--<256.0,177.0>> -> L<<256.0,177.0>--<256.0,693.0>> 

	* uni2116 (U+2116): L<<84.0,619.0>--<87.0,525.0>> -> L<<87.0,525.0>--<87.0,0.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<176.5,310.0>-<133.0,465.0>-<89.0,619.0>>/L<<89.0,619.0>--<92.0,525.0>> = 14.117427656617828

	* uni01CA (U+01CA): L<<103.0,693.0>--<269.0,98.0>>/L<<269.0,98.0>--<266.0,177.0>> = 13.413911493807218

	* uni01CB (U+01CB): B<<187.5,310.0>-<144.0,465.0>-<100.0,619.0>>/L<<100.0,619.0>--<103.0,525.0>> = 14.117427656617828

	* uni01CB (U+01CB): L<<114.0,693.0>--<280.0,98.0>>/L<<280.0,98.0>--<277.0,177.0>> = 13.413911493807218

	* uni2116 (U+2116): L<<253.0,0.0>--<84.0,619.0>>/L<<84.0,619.0>--<87.0,525.0>> = 13.442813602023904 

	* uni2116 (U+2116): L<<98.0,693.0>--<259.0,98.0>>/L<<259.0,98.0>--<256.0,177.0>> = 12.966239720466854 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* I (U+0049): L<<262.0,31.0>--<263.0,662.0>>

	* I (U+0049): L<<298.0,662.0>--<297.0,31.0>>

	* Iacute (U+00CD): L<<262.0,31.0>--<263.0,662.0>>

	* Iacute (U+00CD): L<<298.0,662.0>--<297.0,31.0>>

	* Ibreve (U+012C): L<<262.0,31.0>--<263.0,662.0>>

	* Ibreve (U+012C): L<<298.0,662.0>--<297.0,31.0>>

	* Icircumflex (U+00CE): L<<262.0,31.0>--<263.0,662.0>>

	* Icircumflex (U+00CE): L<<298.0,662.0>--<297.0,31.0>>

	* Idieresis (U+00CF): L<<262.0,31.0>--<263.0,662.0>>

	* Idieresis (U+00CF): L<<298.0,662.0>--<297.0,31.0>> 

	* 63 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] UbuntuSansMono-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1339 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Ubuntu Sans Mono SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<113.0,454.0>--<116.0,261.0>> -> L<<116.0,261.0>--<116.0,0.0>>

	* uni01CA (U+01CA): L<<221.0,263.0>--<217.0,442.0>> -> L<<217.0,442.0>--<217.0,693.0>>

	* uni01CB (U+01CB): L<<113.0,454.0>--<116.0,281.0>> -> L<<116.0,281.0>--<116.0,0.0>>

	* uni01CB (U+01CB): L<<221.0,263.0>--<217.0,419.0>> -> L<<217.0,419.0>--<217.0,693.0>>

	* uni2116 (U+2116): L<<108.0,426.0>--<111.0,263.0>> -> L<<111.0,263.0>--<111.0,0.0>>

	* uni2116 (U+2116): L<<218.0,291.0>--<215.0,423.0>> -> L<<215.0,423.0>--<215.0,693.0>>

	* uni2713 (U+2713): L<<204.0,242.0>--<219.0,265.0>> -> L<<219.0,265.0>--<480.0,616.0>> 

	* uni2713 (U+2713): L<<85.0,398.0>--<189.0,264.0>> -> L<<189.0,264.0>--<204.0,242.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<141.5,332.5>-<128.0,388.0>-<113.0,454.0>>/L<<113.0,454.0>--<116.0,261.0>> = 11.913729811926178

	* uni01CA (U+01CA): L<<107.0,693.0>--<221.0,263.0>>/L<<221.0,263.0>--<217.0,442.0>> = 13.568312458572978

	* uni01CB (U+01CB): B<<141.5,332.5>-<128.0,388.0>-<113.0,454.0>>/L<<113.0,454.0>--<116.0,281.0>> = 11.810797209004122

	* uni01CB (U+01CB): L<<107.0,693.0>--<221.0,263.0>>/L<<221.0,263.0>--<217.0,419.0>> = 13.379651303792055 

	* uni04CD (U+04CD): L<<222.0,250.0>--<148.0,551.0>>/B<<148.0,551.0>-<147.0,413.0>-<146.0,271.5>> = 14.227262261099765 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] UbuntuSansMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1339 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni2713 (U+2713): L<<203.0,258.0>--<221.0,287.0>> -> L<<221.0,287.0>--<474.0,631.0>> 

	* uni2713 (U+2713): L<<88.0,412.0>--<184.0,286.0>> -> L<<184.0,286.0>--<203.0,258.0>> [code: found-colinear-vectors]
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
</div></details><br></div></details><details><summary><b>[12] UbuntuSansMono-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1339 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Ubuntu Sans Mono Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni01C4	Contours detected: 5	Expected: 4

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: uni01C4	Contours detected: 5	Expected: 4 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01CA (U+01CA): L<<263.0,153.0>--<252.0,323.0>> -> L<<252.0,323.0>--<252.0,693.0>>

	* uni01CA (U+01CA): L<<93.0,541.0>--<103.0,368.0>> -> L<<103.0,368.0>--<103.0,0.0>>

	* uni01CB (U+01CB): L<<267.0,153.0>--<256.0,330.0>> -> L<<256.0,330.0>--<256.0,693.0>>

	* uni01CB (U+01CB): L<<97.0,541.0>--<106.0,362.0>> -> L<<106.0,362.0>--<106.0,0.0>>

	* uni2116 (U+2116): L<<260.0,145.0>--<250.0,329.0>> -> L<<250.0,329.0>--<250.0,693.0>> 

	* uni2116 (U+2116): L<<92.0,549.0>--<102.0,368.0>> -> L<<102.0,368.0>--<102.0,0.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni01CA (U+01CA): B<<169.0,271.0>-<130.0,411.0>-<93.0,541.0>>/L<<93.0,541.0>--<103.0,368.0>> = 12.5789549688919

	* uni01CA (U+01CA): L<<112.0,693.0>--<263.0,153.0>>/L<<263.0,153.0>--<252.0,323.0>> = 11.920353801419516

	* uni01CB (U+01CB): B<<173.0,271.0>-<134.0,411.0>-<97.0,541.0>>/L<<97.0,541.0>--<106.0,362.0>> = 13.008799003029903

	* uni01CB (U+01CB): L<<116.0,693.0>--<267.0,153.0>>/L<<267.0,153.0>--<256.0,330.0>> = 12.06638556036382

	* uni2116 (U+2116): L<<113.0,693.0>--<260.0,145.0>>/L<<260.0,145.0>--<250.0,329.0>> = 11.905141078781755 

	* uni2116 (U+2116): L<<242.0,0.0>--<92.0,549.0>>/L<<92.0,549.0>--<102.0,368.0>> = 12.11930998255544 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] UbuntuSansMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* 🔥 **FAIL** The Ubuntu Font License is only acceptable on the Google Fonts collection for legacy font families that already adopted such license. New Families should use eigther Apache or Open Font License. [code: ufl]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.11.2 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1339 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- ijacute

	- uni030C.alt

	- uni256A.001 

	- uni256B.001
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni0249	Contours detected: 3	Expected: 2

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: dkshade	Contours detected: 61	Expected: 73

	- Glyph name: ltshade	Contours detected: 36	Expected: 46

	- Glyph name: shade	Contours detected: 72	Expected: 85 

	- Glyph name: uni0249	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
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
| 0 | 44 | 85 | 1344 | 67 | 996 | 0 |
| 0% | 2% | 3% | 53% | 3% | 39% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
