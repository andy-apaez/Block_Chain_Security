# 🔗 Blockchain Security Demo

A simple Python project that implements a **basic blockchain** and demonstrates **security vulnerabilities** such as the **51% attack** and **double-spending attack**.  
It also simulates a small **network of nodes** to show how consensus can fail when an attacker controls the majority of mining power.  

---

## 🚀 Features
- 🧱 Core blockchain implementation (blocks, hashes, immutability).  
- 🔍 Chain validation to detect tampering.  
- ⚡ **51% Attack Simulation** – attacker builds a longer chain and overtakes honest nodes.  
- 💸 **Double-Spending Simulation** – attacker reverses transactions by releasing an alternative chain.  
- 🌐 **Multi-Node Network** – honest nodes initially agree, but adopt the attacker’s chain when it is longer.  

---

🖥️ Example Output

✅ Honest Network
=== Honest Network Simulation ===
===== Node 0 Blockchain =====
Block(index=0, hash=..., data=Genesis Block)
Block(index=1, hash=..., data=Transaction 0)
Block(index=2, hash=..., data=Transaction 1)
Block(index=3, hash=..., data=Transaction 2)
✅ Valid: True
...

⚠️ 51% Attack
⚠️ Attacker broadcasts longer chain! Honest nodes adopt it...

===== Node 1 Blockchain =====
Block(index=0, hash=..., data=Genesis Block)
Block(index=1, hash=..., data=Fake Tx 0)
Block(index=2, hash=..., data=Fake Tx 1)
Block(index=3, hash=..., data=Fake Tx 2)
...

💸 Double Spending
Honest Chain Transaction: Alice pays Bob 10 BTC
Attacker Chain Transaction: Alice pays Mallory 10 BTC

⚠️ Attacker's alternative chain is longer, network accepts it!
Bob never actually gets his 10 BTC... double-spend successful.

---

🛡️ Why This Matters

This project shows why real-world blockchains (Bitcoin, Ethereum, etc.) need:

* Large decentralized networks

* Difficulty adjustments

* Strong consensus mechanisms (Proof of Work, Proof of Stake, etc.)

Without these, attackers can:

* Rewrite history with a 51% attack.

* Erase transactions with double-spending.

---

⚠️ Disclaimer

This project is for educational purposes only.
It is a simplified blockchain and should not be used in production.
The goal is to demonstrate security risks and why consensus protocols matter.

