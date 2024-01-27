from BIMAIProject.src.blockchain_integration import Blockchain

def verify_blockchain_integrity(blockchain):
    for i in range(1, len(blockchain.chain)):
        current_block = blockchain.chain[i]
        previous_block = blockchain.chain[i - 1]

        # Check if the previous_hash field matches the hash of the previous block
        if current_block['previous_hash'] != blockchain.hash(previous_block):
            return False

    return True
