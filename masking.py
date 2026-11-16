import re

IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
USER_RE = re.compile(r"(?:invalid user |for )(\S+)(?= from)")


class Masker:

    def __init__(self):
        self.mapping = {}
        self._reverse = {}
        self._counts = {"IP": 0, "USER": 0}

    def _placeholder(self, prefix, value):
        if value not in self._reverse:
            self._counts[prefix] += 1
            placeholder = f"{prefix}_{self._counts[prefix]}"
            self.mapping[placeholder] = value
            self._reverse[value] = placeholder
        return self._reverse[value]

    def mask(self, text):
        text = USER_RE.sub(
            lambda m: m.group(0).replace(m.group(1), self._placeholder("USER", m.group(1))),
            text,
        )
        text = IP_RE.sub(lambda m: self._placeholder("IP", m.group(0)), text)
        return text

    def unmask(self, text):
        for placeholder in sorted(self.mapping, key=len, reverse=True):
            text = text.replace(placeholder, self.mapping[placeholder])
        return text