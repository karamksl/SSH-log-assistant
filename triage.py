import re
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic
client = Anthropic()

with open("auth.log", encoding="utf-8", errors="ignore") as f:
    lines = [l for l in f if re.search(r"Failed password|Invalid user|Accepted", l)]

print(f"{len(lines)} relevant lines found")

prompt = f"""You are a security analyst. Review these SSH auth log lines and reply with JSON only:
{{"summary": str,
  "suspicious_ips": [{{"ip": str, "attempts": int, "severity": "low|medium|high", "reason": str}}],
  "recommendations": [str]}}

Logs:
{''.join(lines[-300:])}"""

resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": prompt}],
)
print(resp.content[0].text)