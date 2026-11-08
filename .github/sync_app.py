"""Copy the newest Reseller Desk app into the plugin.

Szymon's "Send updates to everyone" button writes the new version and its
Google Drive file id into a public Google Sheet. This reads that sheet and,
if the version is newer than the app in this repo, downloads the file,
checks it, saves it as the plugin's app and bumps the plugin version.
"""
import csv, io, json, os, re, sys, urllib.request

SHEET = "1sXc93RKZsp_G3q7vOIfu_kVuSEjIPxoxtxsQq4jNd8g"
APP = "plugins/reseller-desk/skills/open-app/assets/reseller-desk.html"
PLUGIN = "plugins/reseller-desk/.claude-plugin/plugin.json"
MARKET = ".claude-plugin/marketplace.json"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "reseller-desk-sync"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

url = f"https://docs.google.com/spreadsheets/d/{SHEET}/gviz/tq?tqx=out:csv&sheet=Sheet1&range=A2:B2&headers=0"
row = next(csv.reader(io.StringIO(get(url).decode("utf-8"))), [])
ver, fid = (row + ["", ""])[0].strip(), (row + ["", ""])[1].strip()
if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}\.\d+", ver) or not re.fullmatch(r"[\w-]{20,}", fid):
    sys.exit(f"Update sheet doesn't look right: {row!r}")

have = re.search(r'APP_VERSION = "([^"]+)"', open(APP, encoding="utf-8").read())
have = have.group(1) if have else "0"
key = lambda v: [int(x) for x in v.split(".")]
if key(ver) <= key(have):
    print(f"Up to date ({have})"); sys.exit(0)

page = get(f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t").decode("utf-8")
if "<title>Reseller Desk</title>" not in page or f'APP_VERSION = "{ver}"' not in page:
    sys.exit("The downloaded file isn't the Reseller Desk app for that version; nothing changed.")
open(APP, "w", encoding="utf-8").write(page)

def bump(v):
    a = [int(x) for x in v.split(".")]; a[2] += 1; return ".".join(map(str, a))
p = json.load(open(PLUGIN)); new = bump(p["version"]); p["version"] = new
json.dump(p, open(PLUGIN, "w"), indent=2); open(PLUGIN, "a").write("\n")
m = json.load(open(MARKET))
for x in m["plugins"]:
    if x["name"] == "reseller-desk": x["version"] = new
json.dump(m, open(MARKET, "w"), indent=2); open(MARKET, "a").write("\n")

with open(os.environ.get("GITHUB_ENV", os.devnull), "a") as f:
    f.write(f"MSG=App {ver} (plugin {new})\n")
print(f"Updated app {have} -> {ver}, plugin {new}")
