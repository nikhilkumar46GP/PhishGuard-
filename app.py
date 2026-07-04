from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>PhishGuard</h1><h3>Intelligent Phishing URL Detection System</h3>"
  
@app.route("/scan", methods=["POST"])
def scan():
    url = request.form.get("url", "")

    score = 0
    reasons = []

    if not url.startswith("https://"):
        score += 30
        reasons.append("HTTPS not found")

    if len(url) > 70:
        score += 20
        reasons.append("Long URL")

    if "@" in url:
        score += 30
        reasons.append("@ symbol found")

    if score >= 50:
        result = "🔴 PHISHING WEBSITE"
    elif score >= 20:
        result = "🟡 SUSPICIOUS WEBSITE"
    else:
        result = "🟢 SAFE WEBSITE"

    return f"""
    <h1>{result}</h1>
    <h2>Risk Score: {score}%</h2>
    <p>URL: {url}</p>
    <p>{"<br>".join(reasons)}</p>
    <br>
    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
  
