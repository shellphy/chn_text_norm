from chn_text_norm.text import Text

def main():
    raw_text = "13444440000"
    text = Text(raw_text=raw_text).normalize()
    print(text)

if __name__ == "__main__":
    main()
