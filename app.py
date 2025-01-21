import miniflux
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<url>/<key>")
def run(url, key):
    url = f"https://{url}"
    client = miniflux.Client(url, api_key=key)
    counts = client.get_feed_counters()['unreads']
    items = []
    for id, count in counts.items():
        icon = client.get_feed_icon(id)['data']
        items.append((icon, count))
    items = sorted(items, key=lambda x: x[1], reverse=True)
    return render_template('base.html', items=items, url=url)

