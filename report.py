from flask import Flask, render_template_string

app = Flask(__name__)

TELEGRAM_CHANNEL = "https://t.me/redsecure"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ReportTool</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: #0b1120;
            color: #f8fafc;
        }

        .card {
            width: 100%;
            max-width: 420px;
            padding: 35px 25px;
            text-align: center;
            border: 1px solid #263449;
            border-radius: 18px;
            background: #111c2e;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.3);
        }

        .logo {
            width: 65px;
            height: 65px;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 16px;
            background: #2563eb;
            font-size: 28px;
            font-weight: bold;
        }

        h1 {
            margin-bottom: 10px;
            font-size: 28px;
        }

        p {
            color: #a9b8cc;
            line-height: 1.7;
            font-size: 15px;
        }

        .notice {
            margin: 25px 0;
            padding: 15px;
            border-radius: 10px;
            background: #1c2b41;
            font-size: 14px;
            line-height: 1.6;
        }

        .button {
            display: block;
            width: 100%;
            padding: 15px;
            border-radius: 10px;
            background: #229ed9;
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.2s;
        }

        .button:hover {
            background: #168ac2;
        }

        .footer {
            margin-top: 22px;
            font-size: 12px;
            color: #718096;
        }
    </style>
</head>
<body>
    <main class="card">
        <div class="logo">R</div>

        <h1>ReportTool</h1>

        <p>
            Welcome to ReportTool. Before proceeding, please visit
            our official Telegram channel for information and updates.
        </p>

        <div class="notice">
            <strong>Telegram access required</strong><br>
            Visit our Telegram channel before continuing.
            No other features are available on this screen.
        </div>

        <a class="button"
           href="{{ telegram_channel }}"
           target="_blank"
           rel="noopener noreferrer">
            Continue to Telegram
        </a>

        <div class="footer">
            ReportTool &bull; Official channel access
        </div>
    </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        telegram_channel=TELEGRAM_CHANNEL
    )

if __name__ == "__main__":
    app.run(debug=True)