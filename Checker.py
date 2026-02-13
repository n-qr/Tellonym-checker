import requests
import random
import string
import time
import os
import threading
from urllib.parse import quote

class Tellonym:
    def __init__(self):
        self.checked = 0
        self.good = 0
        self.error = 0
        self.user = ""
        self.lock = threading.Lock()
        self.proxies = []
        self.use_proxy = None
        self.Mode_proxy2 = None
        self.ensure_files()
        self.ask_proxy()
        self.len = int(input("Username length:"))
        self.start()

    def ensure_files(self):
        if not os.path.exists("good.txt"):
            open("good.txt", "w").close()

    def ask_proxy(self):
        use = input("Use proxy? (y/n): ").lower()
        if use != "y":
            self.use_proxy = False
            return
        self.use_proxy = True
        self.Mode_proxy2 = input("Proxy type 1=http 2=socks4 3=socks5: ").strip()
        name = input("Proxy file name: ").strip() + ".txt"
        if not os.path.exists(name):
            open(name, "w").close()
        with open(name, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                px = self.parse_proxy(line.strip())
                if px and px != "Invalid proxy format":
                    self.proxies.append(px)

    def parse_proxy(self, raw):
        prx = raw.strip()
        if prx.lower().startswith("http://"):
            prx = prx[7:]
        elif prx.lower().startswith("https://"):
            prx = prx[8:]
        elif prx.lower().startswith("socks4://"):
            prx = prx[9:]
        elif prx.lower().startswith("socks5://"):
            prx = prx[10:]
        host = port = user = passwd = None
        if "@" in prx:
            left, right = prx.split("@", 1)
            def is_hostport(s: str):
                if ":" not in s: return False
                hp = s.split(":", 1)
                return hp[1].isdigit()
            if is_hostport(right):
                user, passwd = left.split(":", 1)
                host, port = right.split(":", 1)
            else:
                host, port = left.split(":", 1)
                user, passwd = right.split(":", 1)
        else:
            parts = prx.split(":", 3)
            if len(parts) == 2:
                host, port = parts
            elif len(parts) == 4:
                if parts[1].isdigit():
                    host, port, user, passwd = parts
                else:
                    user, passwd, host, port = parts
            else:
                return None
        if not host or not port:
            return None
        if user and passwd:
            user_enc = quote(user, safe="")
            pass_enc = quote(passwd, safe="")
            return f"http://{user_enc}:{pass_enc}@{host}:{port}"
        if self.Mode_proxy2 == '1':
            return f"http://{host}:{port}"
        if self.Mode_proxy2 == '2':
            return f"socks4://{host}:{port}"
        if self.Mode_proxy2 == '3':
            return f"socks5://{host}:{port}"
        return None

    def ruser(self):
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(self.len))

    def pick_proxy(self):
        if not self.use_proxy or not self.proxies:
            return None
        p = random.choice(self.proxies)
        return {"http": p, "https": p}

    def update(self):
        print(f'\rAttempts: {self.checked} | Good: {self.good} | username :{self.user}', end='', flush=True)

    def worker(self):
        while True:
            try:
                user = self.ruser()
                self.user = user
                url = f"https://tellonym.me/{user}"
                headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "cookie": f"__cf_bm=_{os.urandom(190).hex()}",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "naviguate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

                pr = self.pick_proxy()
                r = requests.options(url, headers=headers, proxies=pr, timeout=15)
                

                if r.status_code == 200:
                    with self.lock:
                        self.checked += 1

                elif r.status_code == 404:
                    with self.lock:
                        self.good += 1
                    print(f"\n\033[92mGOOD @{user}\033[0m")
                    with open("good.txt","a") as f:
                        f.write(user+"\n")

                self.update()

            except Exception:
                with self.lock:
                    self.error += 1
                self.update()
                continue

    def start(self):
        th = int(input("threads: "))
        for _ in range(th):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
        while True:
            time.sleep(999)

Tellonym()
