import wikiclean


def main():
    with open("snippet.txt") as f:
        content = f.read()
    print("Original:")
    print(content)
    print("=" * 100)
    print("WikiClean output:")
    print(wikiclean.clean(content))
    try:
        import unwiki
        print("=" * 100)
        print("UnWiki output:")
        print(unwiki.loads(content))
    except ImportError:
        pass
    try:
        import dewiki
        import dewiki.parser as parser
        print("=" * 100)
        print("DeWiki output:")
        print(parser.Parser().parse_string(content))
    except ImportError:
        pass


if __name__ == "__main__":
    main()
