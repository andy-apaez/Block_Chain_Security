from blockchain import Blockchain
import random

# ---- Helper: Print Chains ----
def print_network(nodes):
    for i, node in enumerate(nodes):
        print(f"\n===== Node {i} Blockchain =====")
        print(node)
        print("✅ Valid:", node.is_chain_valid())


# ---- Step 1: Honest Network ----
print("\n=== Honest Network Simulation ===")
nodes = [Blockchain() for _ in range(3)]  # 3 honest nodes

# All honest nodes mine the same transactions
for node in nodes:
    for i in range(3):
        node.add_block(f"Transaction {i}")

print_network(nodes)

# ---- Step 2: Attacker Joins ----
print("\n=== 51% Attack Simulation ===")
attacker = Blockchain()

# Attacker mines faster (longer chain)
for i in range(7):  # attacker has more power
    attacker.add_block(f"Fake Tx {i}")

print("\n===== Attacker's Chain =====")
print(attacker)
print("✅ Valid:", attacker.is_chain_valid())

# Honest nodes compare chains and adopt the longest (naive consensus)
print("\n⚠️ Attacker broadcasts longer chain! Honest nodes adopt it...")

for i in range(len(nodes)):
    if len(attacker.chain) > len(nodes[i].chain):
        nodes[i].chain = attacker.chain.copy()

print_network(nodes)

# ---- Step 3: Double-Spending Example ----
print("\n=== Double Spending Simulation ===")
honest_chain = Blockchain()
honest_chain.add_block("Alice pays Bob 10 BTC")

# Attacker secretly mines conflicting transaction
attacker_alt = Blockchain()
attacker_alt.add_block("Alice pays Mallory 10 BTC")

print("\nHonest Chain Transaction:", honest_chain.chain[1].data)
print("Attacker Chain Transaction:", attacker_alt.chain[1].data)

# Later attacker mines extra blocks to make alt chain longer
for i in range(3):
    attacker_alt.add_block(f"More fake tx {i}")

print("\n⚠️ Attacker's alternative chain is longer, network accepts it!")
print("Bob never actually gets his 10 BTC... double-spend successful.")
