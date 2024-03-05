import re
def process_tex(tex):
    tex = tex.replace("&", r"\&")
    tex = tex.replace("’", r"'")
    tex = tex.replace("‘", r"`")
    tex = tex.replace("旻", r"{\CJKfontspec{STSong.TTF}旻}")
    tex = tex.replace("垚", r"{\CJKfontspec{STSong.TTF}垚}")
    tex = tex.replace("玥", r"{\CJKfontspec{STSong.TTF}玥}")
    tex = tex.replace("煒", r"{\CJKfontspec{STSong.TTF}煒}")
    return tex

def process_authors(authors: str):
    # captitalize the first letter of each word, if the word is not inside parentness
    # e.g. "John Doe (University of California)" -> "John Doe (University Of California)"
    # find all words inside parentness
    pattern = re.compile(r"\((.*?)\)")
    matches = pattern.findall(authors)

    # replace all words inside parentness with a placeholder
    for match in matches:
        authors = authors.replace(match, "placeholder", 1)

    # remove consecutive spaces
    authors = re.sub(r"\s+", " ", authors)
    if authors == " " or authors == "":
        return authors

    # capitalize the first letter of each word
    authors = " ".join([word.capitalize() for word in authors.split(" ")])

    # if the word is chinese, mv the last letter to the front
    # e.g. "旻垚" -> "垚旻"
    for match in re.finditer(r"[\u4e00-\u9fff ]{2,}", authors):
        name = match.group()
        flag = False
        if name[-1] == " ":
            flag = True
        name = name.replace(" ", "")
        name = name[-1] + name[:-1]
        if flag:
            name += " "
        authors = authors.replace(match.group(), name, 1)

    # character followed by dash should also be capitalized
    for match in re.finditer(r"-[a-z]", authors):
        authors = authors.replace(match.group(), match.group().upper())

    # replace the placeholder with the original word
    for match in matches:
        authors = authors.replace("placeholder", match, 1)
    return authors


