
https://www.youtube.com/watch?v=V0JdeRzVndI&list=PLK9Lwn4_TfLS3I9huJjd-k_FeMKiTkAff&index=2


# What is a blockchain?

4 layers

```
3   - User interface (web3)
2   - Applications (solidity, move, motoko)
1.5 - Compute Layer -- Blockchain computer
1   - Consensus Layer
```

Most of the exciting action is in the application layer.

## Layer 1 -- Consensus layer

* Public data structure (ledger) that provides
  * Persistence -- once added, data can never be removed (51% attack caveat)
  * Consensus -- ALl honest participants have the same data (eventual consistency**)
  * Liveness -- All honest participants can add data
  * Open -- Anyone can be a participant (some blockchains are open, some are permissioned)

Not a new problem: Google, Amazon etc run a large number of machines that need to see the same data. Problem is called State machine regulation.
Known number of servers, all are authorize.

Difference in blockchain: Anyone can participate.

### How are blocks added to the chain?


users can sign transactions, send to miners who add to blockchain, leader is elected, leader adds to chain, other miners validate, miner gets paid.

Leader decided on the order of transaction in the block.

For example: Who gets to sell first is decided by the miner, not good.

Not solved: how to do this in a way that no single miner has this control on the order of the transactions in the blockchain.

**Sybil attack**: Miners could try to get elected every time by pretending to be a thousand different miners, other miners would never get elected

Solve by forcing miners to commit resources.

Bitcoin, you have to solve problems requiring hardware (**proof-of-work**). energy is wasted, is very slow.

**Proof of stake**: force people to commit to funds instead of CPU.

**Proof of space**: Commit to disk space instead of compute power, doesn't take much energy.

## Layer 1.5 -- Blockchain computer

Write apps, post to the blockchain.
People send transactions to blockchain computer, apps running on the computer reply.
Running apps on the blockchain means
* all code is open-source and public. No secrets because every thing is based on trust.
* public verifiability -- anyone can verify state transitions on the blockchain computer. IRL, you have to trust banks / social media platforms etc.


## Running programs on a blockchain

* Create an app
* post code to the blockchain. Code is a transaction in the chain.
* Someone sends transaction to the application, state changes in the application.

* Want to touch the blockchain as little as possible for scalability.


## Execution environment
* Bitcoin -- Bitcoin script, limited instruction set (no loops for example)
* Ethereum -- General programming environment, solidity, web3
  * Storing things on the blockchain is expensive.
  * You have to pay to write today, will probably have to pay to store in the future.
  * Developers will need to spend most of the time in removing data, not writing to the chain.
* Modern blockchains are using WebAssembly -- write your app in favorite env, compile to WebAssembly, run on the blockchain.


## Decentralized Applications (dapps)
* Languages: Solidity, Move
* If you make a mistake, you can lock out millions of dollars. Mistakes are costly!

## Layer 4 - user facing servers

* Users talk to normal computers that talk to the blockchain.
* MakerDAO -- took Fed policy, implemented in an algorithm
* Compound -- Lending platform


# Cryptographic primitives

Blockchains are consumers of cryptography.

## Digital signatures + aggregation

* Physical signatures can't work in the digital world, because you can just copy the bits.
* Solution: Make the signature depend on the thing that you're signing. signing key + algorithm -> signature which can later be verified.
* Need your signing key to generate signatures.

### Signatures on the blockchain

* Txn authorization
* Governance vots
* Consensus protocol votes.

Note: ALL miners verify the signatures.

### Signature aggregation

Compression mechanism: Compress N signatures into 1, verify using all public keys + txn ids.

Example: blockchain called chia: takes a bunch of transactions, aggregates and stores the aggregate, less data on the blockchain.


## Merkle commitments

Cryptographic commitment: Emulates an envelope.

Sealed bid auction: every participant **commits** to its bid. Once all bids are in, auctioneer can see who wins the auction.

Commit(data) => (com, open)
Verify (data, com, open) => "accept" or "reject"

Sealed bid in a digital environment:
* You send `com` and `open` to the auction house.
* Then the auctioneer can verify that you actually did commit `data` before.


### Properties

Binding: Cannot produce two valid openings.
Hiding: `com` cannot tell you the data.

### Merkle tree

Succinct commitment / Merkle tree: commit to gigabytes of data in 32 bytes and open individual cells correctly
Write merkle commitment of 1000s of transactions in one block.

Applications:
* proof of payment by quick verification of commitments
* keeping state of chain: Database of account balances off chain. off-chain: servers with balances, on-chain: short commitment of balances, don't need to write entire database on the blockchain.


## Zero knowledge proof system

Anything that can be proved can also be proved in zero knowledge.


Prover wants to prove: "I have a signature on Txn, witness: signature" in zero knowledge without telling the signature
Prover gives the proof to the verifier and verifier verifies the proof.


SNARK // zkSNARK

Libraris for zkSnark: circom, zinc

Succinct proofs: put in a rollup server, so that miners only have to verify succinct proofs of the transactions instead of verifying all txns.

Application 2: Private data on a public blockchain. Currently, all txns are public.

Write only *commitments* to the blockchain,


## REMEMBER

* don't put data on the blockchain, it's not a database.
* Always ask: why not use a centralized system?
* Blockchains are best when there is NO single party that you can trust.
* very likely that we'll converge onto small number of architectures from the large number of blockchains.
