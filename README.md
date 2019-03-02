# PyWikiClean
Python port of @lintool's comprehensive Java-based Wikipedia markup to plaintext converter: https://github.com/lintool/wikiclean.

## Overview

I couldn't find a Python-based Wikipedia markup cleaner as comprehensive as @lintool's, so I ported [his](https://github.com/lintool/wikiclean). It's easy to use:

1. Install: `pip install git+https://github.com/daemon/pywikiclean`
2. Clean: `import wikiclean; wikiclean.clean("Wikipedia [[markup]] here!") # Wikipedia markup here!`

So how does PyWikiClean compare to other Python tools?

### Original
```
{{good article}}
{{Infobox single &lt;!-- See Wikipedia:WikiProject_Songs --&gt;
| Name           = One of Those Days
| Cover          = Whitney Houston – One of Those Days.jpg
| Border         = yes
| Artist         = [[Whitney Houston]]
| Album          = [[Just Whitney]]
| Released       = {{start date|2002|10|29}}
| Format         = {{flat list|
*[[CD single]]
*[[Music download|digital download]]}}
| Recorded       = February 2002;&lt;br&gt;at Atlanta Premier Recordings&lt;br&gt;([[Atlanta, Georgia]])
| Genre          = [[Contemporary R&amp;B|R&amp;B]]
| Length         = {{Duration|m=3|s=56}}
| Label          = [[Arista Records|Arista]]
| Writer         = {{flat list|
*[[Kevin "She'kspere" Briggs|Kevin Briggs]]
*Dwight Renolds
*Patrice Stewart
*[[Ernest Isley]]
*[[Marvin Isley]]
*Christopher Jasper
*Kelly Isley
*[[Ronald Isley]]
*[[Rudolph Isley]]}}
| Producer       = Kevin Briggs
| Last single    = "[[Whatchulookinat]]"&lt;br /&gt;(2002)
| This single    = "'''One of Those Days'''"&lt;br /&gt;(2002)
| Next single    = "[[Try It on My Own]]"&lt;br /&gt;(2003)
|misc={{External music video|{{YouTube|-GW0jZQSmsw|"One of Those Days"}}}}
}}

"'''One of Those Days'''" is a song by American recording artist [[Whitney Houston]], from her fifth studio album ''[[Just Whitney]]'' (2002). Written by [[Kevin "She'kspere" Briggs|Kevin Briggs]], Dwight Renolds, Patrice Stewart, [[Ernest Isley]], [[Marvin Isley]], Christopher Jasper, Kelly Isley, [[Ronald Isley]], and [[Rudolph Isley]], and produced by Briggs, the song was released as the second single from the album, following the under-performance of the [[lead single]] "[[Whatchulookinat]]", on October 29, 2002 through [[Arista Records]]. A mid-tempo [[Contemporary R&amp;B|R&amp;B]] track, "One of Those Days" samples [[The Isley Brothers]]' song "[[Between the Sheets (song)|Between the Sheets]]" (1983), and its lyrics speak about getting away from the stress of daily life.
```
### [UnWiki](https://github.com/fitnr/unwiki)
```


| Format          
| Recorded        February 2002;&lt;br&gt;at Atlanta Premier Recordings&lt;br&gt;(Atlanta, Georgia)
| Genre           R&amp;B
| Length          
| Label           Arista
| Writer          
| Producer        Kevin Briggs
| Last single     "Whatchulookinat"&lt;br /&gt;(2002)
| This single     "One of Those Days"&lt;br /&gt;(2002)
| Next single     "Try It on My Own"&lt;br /&gt;(2003)
|misc}}
}}

"One of Those Days" is a song by American recording artist Whitney Houston, from her fifth studio album Just Whitney (2002). Written by Kevin Briggs, Dwight Renolds, Patrice Stewart, Ernest Isley, Marvin Isley, Christopher Jasper, Kelly Isley, Ronald Isley, and Rudolph Isley, and produced by Briggs, the song was released as the second single from the album, following the under-performance of the lead single "Whatchulookinat", on October 29, 2002 through Arista Records. A mid-tempo R&amp;B track, "One of Those Days" samples The Isley Brothers' song "Between the Sheets" (1983), and its lyrics speak about getting away from the stress of daily life.

```
### [DeWiki](https://github.com/daddyd/dewiki)
```

{{Infobox single &lt;!-- See Wikipedia:WikiProject_Songs --&gt;
| Name           = One of Those Days
| Cover          = Whitney Houston – One of Those Days.jpg
| Border         = yes
| Artist         = Whitney Houston
| Album          = Just Whitney
| Released       = 
| Format         = {{
*CD single
*digital download}}
| Recorded       = February 2002;&lt;br&gt;at Atlanta Premier Recordings&lt;br&gt;(Atlanta, Georgia)
| Genre          = Contemporary R&amp;R&amp;B
| Length         = 
| Label          = Arista
| Writer         = {{
*Kevin "She'kspere"Kevin Briggs
*Dwight Renolds
*Patrice Stewart
*Ernest Isley
*Marvin Isley
*Christopher Jasper
*Kelly Isley
*Ronald Isley
*Rudolph Isley}}
| Producer       = Kevin Briggs
| Last single    = "Whatchulookinat"&lt;br /&gt;(2002)
| This single    = "One of Those Days"&lt;br /&gt;(2002)
| Next single    = "Try It on My Own"&lt;br /&gt;(2003)
|misc=
}}

"One of Those Days" is a song by American recording artist Whitney Houston, from her fifth studio album Just Whitney (2002). Written by Kevin "She'kspere"Kevin Briggs, Dwight Renolds, Patrice Stewart, Ernest Isley, Marvin Isley, Christopher Jasper, Kelly Isley, Ronald Isley, and Rudolph Isley, and produced by Briggs, the song was released as the second single from the album, following the under-performance of the lead single "Whatchulookinat", on October 29, 2002 through Arista Records. A mid-tempo Contemporary R&amp;R&amp;B track, "One of Those Days" samples The Isley Brothers' song "Between the Sheets" (1983), and its lyrics speak about getting away from the stress of daily life.
```
### PyWikiClean
```
"One of Those Days" is a song by American recording artist Whitney Houston, from her fifth studio album Just Whitney (2002). Written by Kevin Briggs, Dwight Renolds, Patrice Stewart, Ernest Isley, Marvin Isley, Christopher Jasper, Kelly Isley, Ronald Isley, and Rudolph Isley, and produced by Briggs, the song was released as the second single from the album, following the under-performance of the lead single "Whatchulookinat", on October 29, 2002 through Arista Records. A mid-tempo R&B track, "One of Those Days" samples The Isley Brothers' song "Between the Sheets" (1983), and its lyrics speak about getting away from the stress of daily life.
```

For now, the tool handles English only. It should be simple to add the other languages that the original WikiClean supports.
