## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[11] UbuntuMono[wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 🔥 **FAIL** fvar instances are incorrect:
- Add missing instances
- wght coordinates are wrong for some instances
| Name | current | expected |
| :--- | :--- | :--- |
| Thin | wght=100.0 | wght=100.0 |
| ExtraLight | wght=200.0 | wght=200.0 |
| Light | wght=600.0 | wght=300.0 |
| Regular | wght=400.0 | wght=400.0 |
| Medium | wght=500.0 | wght=500.0 |
| SemiBold | N/A | wght=600.0 |
| Bold | wght=700.0 | wght=700.0 | [code: bad-fvar-instances]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances don't have duplicate names (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_duplicate_instance_names">com.google.fonts/check/varfont_duplicate_instance_names</a>)</summary><div>


* 🔥 **FAIL** Following instances names are duplicate:

* Light
 [code: duplicate-instance-names]
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
	* Alpha and 775 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- acute.asc

	- caron.asc

	- circumflex.asc

	- eight_fraction_nine

	- f_i

	- f_l

	- five_fraction_nine

	- five_fraction_seven

	- four_fraction_nine 

	- 10 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour order differs in glyph 'quotedbl': [0, 1] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280>, [1, 0] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>.

	- Contour 0 start point differs in glyph 'caron' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>

	- Contour order differs in glyph 'hungarumlaut': [0, 1] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280>, [1, 0] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>.

	- Contour 0 start point differs in glyph 'dieresis_breve' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>

	- Contour 0 start point differs in glyph 'dieresis_breve.cap' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>

	- Contour 3 start point differs in glyph 'uni01C4' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>

	- Contour 0 start point differs in glyph 'uni018E' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>

	- Contour 1 start point differs in glyph 'uni01EA' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>

	- Contour 1 start point differs in glyph 'uni01EB' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0>

	- Contour 0 start point differs in glyph 'uni04F6' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9280> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1131d9ca0> 

	- 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1357 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><br></div></details><details><summary><b>[8] UbuntuMono-Italic[wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoAscender is 932 when it should be 830 [code: bad-typo-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: OS/2 sTypoDescender is -189 when it should be -170 [code: bad-typo-descender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Ascender is 932 when it should be 830 [code: bad-hhea-ascender]
* 🔥 **FAIL** Ubuntu Mono Regular: hhea Descender is -189 when it should be -170 [code: bad-hhea-descender]
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
	* Alpha and 765 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- acute.asc

	- ampersand.001

	- caron.asc

	- circumflex.asc

	- eight_fraction_nine

	- f_i

	- f_l

	- five_fraction_nine

	- five_fraction_seven 

	- 11 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour 0 start point differs in glyph 'circumflex.asc' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x112b76040> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x112b76400> [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1359 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 6 | 13 | 204 | 17 | 235 | 0 |
| 0% | 1% | 3% | 43% | 4% | 49% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
