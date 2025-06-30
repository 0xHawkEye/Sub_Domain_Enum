# Sub_Domain_Enum

![License: MIT](https://img.shields.io/github/license/AyushKr41/Sub_Domain_Enum
)
![Issues](https://img.shields.io/github/issues/AyushKr41/Sub_Domain_Enum
)
![Forks](https://img.shields.io/github/forks/AyushKr41/Sub_Domain_Enum
)
![Stars](https://img.shields.io/github/stars/AyushKr41/cllg_projects
)
![Last Commit](https://img.shields.io/github/last-commit/AyushKr41/Sub_Domain_Enum
)
![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

>🚀 A fast, multithreaded subdomain enumeration tool written in Python using a wordlist-based approach.
Useful for reconnaissance in ethical hacking and bug bounty hunting.

---
## **🧠 Features**
⚡ Fast performance with multithreading

✅ Progress bar for real-time scan updates

📂 Output saved to a text file

🔐 Silent error handling

🧾 Customizable wordlist support

---
## **🖥️ How It Works**

 - The script takes a target domain and brute-forces potential subdomains using a wordlist. If the subdomain resolves, it’s printed and saved.

---
## **📦 Requirements**

- Python 3.x
- requests module (pip install requests)

---

## **📦 Installation**

To get started with Sub_Domain_Enum, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/AyushKr41/Sub_Domain_Enum.git
cd Sub_Domain_Enum
pip install requests
```
---

## **🚀 Usage**
```bash
python sub.py
```
You’ll be prompted to enter the target domain:
```bash
[+]Enter the target URL: example.com
```
---
## **📁 Output**
Discovered subdomains are saved in:

```lua
output/<target>.txt
```
Example:
```bash
output/example.com.txt
```
---
## **📂 Project Structure**
```lua
sub.py
sorted_wordlist.txt
output/
```
---

## **⚖️ Legal Considerations**
**Sub_Domain_Enum** is intended for educational and authorized penetration testing purposes only.

By using this tool, you agree to the following:

✅ You will not use **Sub_Domain_Enum** to scan, probe, or interact with Domain without explicit permission from the owner.

✅ You are solely responsible for any misuse or unauthorized activity performed using this tool.

✅ The developer is not liable for any damage, legal consequences, or misuse resulting from the use of this tool.

>❗ Always obtain proper authorization before scanning or enumerating subdomains on any domain.

>This tool is intended for educational and authorized testing purposes only.

---
## **📄 License**
This project is licensed under the MIT License.

---
## **🛡️ Ethical Usage**
- Use in lab environments, CTFs, bug bounty, or client-approved pentests.
- Respect all terms of service and network usage policies.
---
## **🤝 Contributing**
Contributions are welcome! Feel free to submit pull requests or open issues to enhance the tool. Your feedback and contributions help improve Sub_Domain_Enum.

---

## **🙌 Credits**

    Developed by: Ayush Kumar
    Linkedin: https://www.linkedin.com/in/ayush-kumar-ak4422 