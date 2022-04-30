class Annotations(object):
    bold = False
    italic = False
    strikethrough = False
    code = False
    color = "default"
    def __init__(self, bold=False, italic=False, strikethrough=False, code=False, color="default"):
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.code = code
        self.color = color

class RichText(object):
    plain_text = ""
    href = None
    annotations = Annotations()
    def __init__(self, plain_text, href=None, annotations=None):
        self.plain_text = plain_text
        self.href = href
        self.annotations = annotations

class Link(object):
    type = "url"
    url = ""
    def __init__(self, url=""):
        self.url = url

class Text(object):
    content = ""
    link = None
    def __init__(self, content, link=None):
        self.content = content
        self.link = link

class MENTION_TYPE(object):
    NONE = None
    USER = "user"
    PAGE = "page"
    DATABASE = "database"
    DATE = "date"
    LINK_PREVIEW = "link_preview"

class USER_TYPE(object):
    # https://developers.notion.com/reference/user#bots
    NONE = None
    PERSON = "person"
    BOT = "bot"

class BOT_OWNER_TYPE(object):
    # https://developers.notion.com/reference/user#bots
    NONE = None
    PERSON = "person"
    WORKSPACE = "workspace"

class BotOwner(object):
    # https://developers.notion.com/reference/user#bots
    type = BOT_OWNER_TYPE.NONE
    # Only true if OWNER_TYPE.person
    workspace = False
    user = None
    def __init__(self, type=BOT_OWNER_TYPE.NONE, workspace=False, user=None):
        self.type = type
        self.workspace = workspace
        self.user = user

class BotObject(object):
    # https://developers.notion.com/reference/user#bots
    owner = BotOwner()

class PersonObject(object):
    # https://developers.notion.com/reference/user#people
    email = ""
    def __init__(self, email=""):
        self.email = email

class UserObject(object):
    # https://developers.notion.com/reference/user
    # https://developers.notion.com/reference/user#all-users
    object = "user"
    id = None
    type = USER_TYPE.NONE
    name = ""
    avatar_url = ""
    # type = USER_TYPE.PERSON
    person = PersonObject()
    # type = USER_TYPE.BOT
    bot = BotObject()

class Mention(object):
    # https://developers.notion.com/reference/rich-text#mention-objects
    type = MENTION_TYPE.NONE
    value = None
    def __init__(self, type=MENTION_TYPE.NONE, value=None):
        self.type = type
        self.value = value

