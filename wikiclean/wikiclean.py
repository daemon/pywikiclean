import html
import re


CATEGORY_LINKS = re.compile("\\[\\[Category:([^\\]]+)\\]\\]")
HEADINGS = re.compile("=+\\s?(.*?)=+")
HTML_COMMENT_EMPHASIS = re.compile("((<|&lt;|&#60;)!--.*?--(>|&gt;|&#62;)|('''|''))", re.DOTALL)
HTML_TAGS = re.compile("<[^>]+>")
INDENTATION = re.compile("[\\n\\r]:\\s*")
INTER_WIKI_LINKS = re.compile("\\[\\[[a-z\\-]+:[^|\\]]+\\]\\]")
IPA = re.compile("( (\\(|\\[)\\{\\{IPA[^\\}]+\\}\\}(\\)|\\])| \\{\\{IPA[^\\}]+\\}\\})")
LINKS1 = re.compile("\\[\\[[^\\]]+\\|([^\\]]+)\\]\\]")
LINKS2 = re.compile("(\\[\\[|\\]\\])")
MATH_GALLERY_NO_TOC = re.compile("(__NOTOC__|&lt;gallery&gt;.*?&lt;/gallery&gt;|&lt;math&gt;.*?&lt;/math&gt;)")
MULTIPLE_NEWLINES = re.compile("[\\n\\r][\\n\\r]+")
REFS = re.compile("(&lt;br */&gt;|&lt;ref[^/]+/&gt;|&lt;ref.*?&lt;/ref&gt;)", re.DOTALL);
UNIT_CONVERSION1 = re.compile("\\{\\{convert\\|(\\d+)\\|([^|]+)\\}\\}")
UNIT_CONVERSION2 = re.compile("\\{\\{convert\\|(\\d+)\\|([^|]+)\\|[^}]+\\}\\}")

FOOTER_PATT = "(==\\s*See also\\s*==.*|==\\s*References\\s*==.*|==\\s*Further " + \
    "reading\\s*==.*|==\\s*External Links\\s*==.*|==\\s*Related pages" + \
    "\\s*==.*|==\\s*Referenzen\\s*==.*|==\\s*Weblinks\\s*==.*|==\\s*Literatur\\s*==.*)"

MULT_NL_PATT = re.compile("[\\n\\r][\\n\\r]+")


def clean(content, remove_footer=True, remove_links=True, remove_nested_constructs=True, remove_nested_constructs_only=False):
    if remove_nested_constructs_only:
        content = remove_image_captions(content)
        content = remove_double_bracket(content)
        content = remove_table(content)
        return content

    if remove_footer:
        content = re.sub(FOOTER_PATT, "", content)
    content = re.sub(REFS, "", content)
    content = re.sub(INTER_WIKI_LINKS, " ", content)
    content = re.sub(IPA, "", content)
    content = re.sub(UNIT_CONVERSION1, r"\1 \2", content)
    content = re.sub(UNIT_CONVERSION2, r"\1 \2", content)
    if remove_nested_constructs:
        content = remove_image_captions(content)
        content = remove_double_bracket(content)
    content = re.sub(HTML_COMMENT_EMPHASIS, "", content)
    content = re.sub(HEADINGS, r"\1\n", content)
    content = re.sub(CATEGORY_LINKS, "", content)
    if remove_links:
        content = re.sub(LINKS1, r"\1", content)
        content = re.sub(LINKS2, "", content)
    content = re.sub(MATH_GALLERY_NO_TOC, "", content)
    content = re.sub(INDENTATION, "\n", content)
    if remove_nested_constructs:
        content = remove_table(content)
    content = html.unescape(html.unescape(content))
    content = re.sub(HTML_TAGS, "", content)
    return re.sub(MULT_NL_PATT, "\n\n", content).strip()


def remove_table(s):
    DEFAULT = 0
    STATE_PIPE = 1
    STATE_1OPEN_BRACE = 2

    i = s.find("{|")
    while i != -1:
        state = DEFAULT
        level = 1
        cur = i + 2
        while cur < len(s):
            if state == STATE_1OPEN_BRACE and s[cur] == "|":
                level += 1
                state = DEFAULT
            if state == STATE_1OPEN_BRACE:
                state = DEFAULT
            if s[cur] == "{":
                state = STATE_1OPEN_BRACE
            if state == STATE_PIPE and s[cur] == "}":
                level -= 1
                if level == 0:
                    break
                state = DEFAULT
            else:
                if state == STATE_PIPE:
                    state = DEFAULT
                if s[cur] == "|":
                    state = STATE_PIPE
            cur += 1
        if (cur == len(s)):
            return s[:i]
        s = f"{s[:i]}{s[cur + 1:]}"
        i = s.find("{|", i)
    return s


def remove_double_bracket(s):
    DEFAULT = 0
    STATE_1CLOSE_BRACE = 1
    STATE_1OPEN_BRACE = 2

    i = s.find("{{")
    while i != -1:
        state = DEFAULT
        level = 1
        cur = i + 2
        while cur < len(s):
            if state == STATE_1OPEN_BRACE and s[cur] == "{":
                level += 1
                state = DEFAULT
            if state == STATE_1OPEN_BRACE:
                state = DEFAULT
            if s[cur] == "{":
                state = STATE_1OPEN_BRACE
            if state == STATE_1CLOSE_BRACE and s[cur] == "}":
                level -= 1
                if level == 0:
                    break
                state = DEFAULT
            else:
                if state == STATE_1CLOSE_BRACE:
                    state = DEFAULT
                if s[cur] == "}":
                    state = STATE_1CLOSE_BRACE
            cur += 1
        if (cur == len(s)):
            return s[:i]
        s = f"{s[:i]}{s[cur + 1:]}"
        i = s.find("{{", i)
    return s


def remove_image_captions(s):
    return _remove_image_caption(_remove_image_caption(s, "[[File:"), "[[Image:")


def _remove_image_caption(s, label):
    DEFAULT = 0
    STATE_1CLOSE_BRACE = 1
    STATE_1OPEN_BRACE = 2

    i = s.find(label)
    while i != -1:
        state = DEFAULT
        level = 1
        cur = i + len(label)
        while cur < len(s):
            if state == STATE_1OPEN_BRACE and s[cur] == "[":
                level += 1
                state = DEFAULT
            if state == STATE_1OPEN_BRACE:
                state = DEFAULT
            if s[cur] == "[":
                state = STATE_1OPEN_BRACE
            if state == STATE_1CLOSE_BRACE and s[cur] == "]":
                level -= 1
                if level == 0:
                    break
                state = DEFAULT
            else:
                if state == STATE_1CLOSE_BRACE:
                    state = DEFAULT
                if s[cur] == "]":
                    state = STATE_1CLOSE_BRACE
            cur += 1
        if (cur == len(s)):
            return s[:i]
        s = f"{s[:i]}{s[cur + 1:]}"
        i = s.find(label, i)
    return s
