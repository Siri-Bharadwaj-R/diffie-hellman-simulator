from flask import Flask, render_template, request
import random

app = Flask(__name__)

data = {"started": False}

def init_simulation(mode, message, eve_message):
    global data

    p = 997
    g = 5

    a = random.randint(1, 10)
    b = random.randint(1, 10)

    A = pow(g, a, p)
    B = pow(g, b, p)

    steps_msg = [
        "Initializing secure channel...",
        "Exchanging public keys...",
        "Computing shared secret...",
        "Checking for intrusion...",
        "Transmitting message...",
        "Verifying communication..."
    ]

    if mode == "secure" or mode == "auth":
        key_alice = pow(B, a, p)
        key_bob = pow(A, b, p)

        data = {
            "started": True,
            "mode": mode,
            "step": 1,
            "p": p, "g": g,
            "A": A, "B": B,
            "alice_key": key_alice,
            "bob_key": key_bob,
            "original": message,
            "modified": message,
            "final": message,
            "eve_active": False,
            "status": steps_msg
        }

    else:
        e1 = random.randint(1, 10)
        e2 = random.randint(1, 10)

        E1 = pow(g, e1, p)
        E2 = pow(g, e2, p)

        key_alice = pow(E1, a, p)
        key_bob = pow(E2, b, p)

        modified = eve_message if eve_message else message

        data = {
            "started": True,
            "mode": "attack",
            "step": 1,
            "p": p, "g": g,
            "A": A, "B": B,
            "E1": E1, "E2": E2,
            "alice_key": key_alice,
            "bob_key": key_bob,
            "original": message,
            "modified": modified,
            "final": modified,
            "eve_active": True,
            "status": steps_msg
        }


@app.route("/", methods=["GET", "POST"])
def home():
    global data

    if request.method == "POST":
        if "start" in request.form:
            init_simulation(
                request.form.get("mode"),
                request.form.get("message"),
                request.form.get("eve_message")
            )

        elif "next" in request.form:
            if data.get("started") and data["step"] < 6:
                data["step"] += 1

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
