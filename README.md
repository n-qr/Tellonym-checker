# TELLONYM CHECKER
<p align="center">
  <img src="https://media1.tenor.com/m/9X3jUkLs5IcAAAAC/cid.gif" width="600" alt="Shadow"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=900&size=44&pause=1000&center=true&vCenter=true&width=800&lines=TELLONYM+CHECKER" alt="Typing SVG"/>
</p>

<h3 align="center">FAST USERNAME FINDER</h3>

---

## 🧠 What is Tellonym Checker?

**Tellonym Checker** is a fast multithreaded username availability checker.  
It generates random usernames and checks if they are **available or taken** on Tellonym.

If a username is available → automatically saved to `good.txt`.

Built for:
- Username hunting  
- Automation research  
- Testing & learning  

---

## ⚙️ Features

- 🎲 Random username generator  
- 📏 Choose username length  
- ⚡ Multithreaded (very fast)  
- 🌐 Proxy support system  
- 📊 Live console stats  
- 📁 Auto-save available usernames  
- 🔁 Infinite checking until stopped  

---

## 💡 How It Works

The checker generates random usernames using:
- lowercase letters (a-z)
- numbers (0-9)


Response meaning:
- `200` → Username exists (taken)
- `404` → Username available → saved

Available usernames are saved inside:
good.txt


## 🌐 Proxy System Explained
tool accept mostly all type of proxy
Proxy type:
1 = HTTP (IP:Port or user:pass or user@pass)
2 = SOCKS4
3 = SOCKS5



---

## 📦 Requirements

Make sure you have:

- Python 3.10+
- Internet connection
- Optional proxies

---

## 🔧 Install Required Libraries

Open terminal / cmd:

```bash
pip install requests

