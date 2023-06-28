## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[12] UbuntuMono[wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.869" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

 | Name | Axis | Current Value | Current Flags | Current LinkedValue | Expected Value | Expected Flags | Expected LinkedValue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Thin | wght | 100.0 | 0 | None | 100.0 | 0 | None |
| ExtraLight | wght | N/A | N/A | N/A | 200.0 | 0 | None |
| Light | wght | 300.0 | 0 | None | 300.0 | 0 | None |
| Regular | wght | 400.0 | 2 | 700.0 | 400.0 | 2 | 700.0 |
| Medium | wght | 500.0 | 0 | None | 500.0 | 0 | None |
| SemiBold | wght | N/A | N/A | N/A | 600.0 | 0 | None |
| Bold | wght | 700.0 | 0 | None | 700.0 | 0 | None |
 [code: bad-axis-values]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 🔥 **FAIL** fvar instances are incorrect:
- Add missing instances

| Name | current | expected |
| :--- | :--- | :--- |
| Thin | wght=100.0 | wght=100.0 |
| ExtraLight | N/A | wght=200.0 |
| Light | wght=300.0 | wght=300.0 |
| Regular | wght=400.0 | wght=400.0 |
| Medium | wght=500.0 | wght=500.0 |
| SemiBold | N/A | wght=600.0 |
| Bold | wght=700.0 | wght=700.0 | [code: bad-fvar-instances]
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
	* Alpha and 776 more.

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


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour order differs in glyph 'quotedbl': [0, 1] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090>, [1, 0] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>.

	- Contour 0 start point differs in glyph 'caron' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>

	- Contour order differs in glyph 'hungarumlaut': [0, 1] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090>, [1, 0] in <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>.

	- Contour 0 start point differs in glyph 'dieresis_breve' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>

	- Contour 0 start point differs in glyph 'dieresis_breve.cap' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>

	- Contour 3 start point differs in glyph 'uni01C4' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>

	- Contour 0 start point differs in glyph 'uni018E' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>

	- Contour 1 start point differs in glyph 'uni01EA' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>

	- Contour 1 start point differs in glyph 'uni01EB' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0>

	- Contour 0 start point differs in glyph 'uni04F6' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845090> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x117845ff0> 

	- 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1356 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tonos.cap (unencoded) [code: spacing-mark-glyphs]
</div></details><br></div></details><details><summary><b>[11] UbuntuMono-Italic[wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.869" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0" [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

 | Name | Axis | Current Value | Current Flags | Current LinkedValue | Expected Value | Expected Flags | Expected LinkedValue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Regular | wght | 400.0 | 2 | 700.0 | 400.0 | 2 | 700.0 |
| Medium | wght | 500.0 | 0 | None | 500.0 | 0 | None |
| SemiBold | wght | N/A | N/A | N/A | 600.0 | 0 | None |
| Bold | wght | 700.0 | 0 | None | 700.0 | 0 | None |
 [code: bad-axis-values]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 🔥 **FAIL** fvar instances are incorrect:
- Add missing instances

| Name | current | expected |
| :--- | :--- | :--- |
| Italic | wght=400.0 | wght=400.0 |
| Medium Italic | wght=500.0 | wght=500.0 |
| SemiBold Italic | N/A | wght=600.0 |
| Bold Italic | wght=700.0 | wght=700.0 | [code: bad-fvar-instances]
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
	* Alpha and 766 more.

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


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour 0 start point differs in glyph 'circumflex.asc' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1162b40a0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x1162b7a60> [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1358 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 10 | 13 | 204 | 17 | 231 | 0 |
| 0% | 2% | 3% | 43% | 4% | 49% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
