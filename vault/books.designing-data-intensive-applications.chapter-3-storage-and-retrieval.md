---
id: cmf5o88ywjrzy9ihxttbogn
title: Chapter 3 Storage and Retrieval
desc: ""
updated: 1676281781303
created: 1676022986726
---

- Hash indexes
- Append only logs are good becasue appending and merging are sequential, hence faster than random writes.
- Concurrency and crash recovery is much easier if the files are append-only

- If we only append, we risk running out of storage
- One strategy is to divide data into segments, close segment when it reaches a certain size and perform compaction on these segments
- Compaction means throwing away duplicate keys in the log.

- Sorted String tables and Log-structured Merge Tree
- Keep sorted key-value files in storage
- Keep an index of some of the keys in memory.
- on retrieval, if the key is in memory, just get it from memory
- if not in memory, we get the closest and then start scanning storage from there.
- The index can be a balanced binary search tree (red-black or AVL) so that we insert randomly but can access in sorted order easily.

- B-Trees

- If an index stores the row value for the key inside the index (as opposed to storing a reference to the value), it's called a clustered index.
- If the index stores only some columns of the row inside the index, it's a covering index.
