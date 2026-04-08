# Diffie-Hellman Secure Communication Simulator

A web-based simulation built using Python (Flask) that demonstrates how secure communication is established using the Diffie-Hellman key exchange protocol, along with a Man-in-the-Middle (MITM) attack and its prevention using authentication.

---

## Overview

This project provides a step-by-step visualization of the Diffie-Hellman key exchange process between two parties. It also demonstrates how the absence of authentication allows an attacker to intercept and modify communication, and how authenticated key exchange prevents such attacks.

---

## Features

* Step-by-step simulation of Diffie-Hellman key exchange
* Visualization of shared key generation
* Man-in-the-Middle (MITM) attack simulation with message interception and modification
* Authenticated key exchange to prevent impersonation
* Interactive interface with dynamic communication flow

---

## Concepts Demonstrated

* Diffie-Hellman Key Exchange
* Discrete Logarithm Problem
* Man-in-the-Middle (MITM) Attack
* Authentication in secure communication

---

## Tech Stack

* Python (Flask)
* HTML, CSS
* Cryptography fundamentals

---

## Project Structure

```id="3n0r4u"
diffie-hellman-simulator/
│  app.py
│  README.md
│
├── templates/
│     └── index.html
│
└── static/
```

---

## Running the Application

Install dependencies:

```id="zqk7pd"
pip install flask
```

Run the application:

```id="a5k1xy"
python app.py
```

Open in browser:

```id="u3q9lm"
http://127.0.0.1:5000
```

---

## Learning Outcome

This project helps in understanding how secure key exchange works over insecure channels, the vulnerabilities introduced by lack of authentication, and the role of authentication in ensuring secure communication.
