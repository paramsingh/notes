
[[engineering.infrastructure.mit6824]]

```
Input1 -> Map -> a,1 b,1
Input2 -> Map ->     b,1
Input3 -> Map -> a,1     c,1
                |   |   |
                |   |   -> Reduce -> c,1
                |   -----> Reduce -> b,2
                ---------> Reduce -> a,2
```

Paper: https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf

## Blog post notes

### What is mapreduce?

- A way to run large parallel jobs for processing large datasets easily.
- Paper by Jeffrey Dean and Sanjay Ghemawat

### Paradigm

- User writes simple map and reduce functions.
- The MapReduce implementation takes input, calls map over the input to
  create intermediate output and then calls reduce over this intermediate
  output to get the final form.

Let's show the canonical word count example:

map and reduce functions has the following signature

```go
type KeyValue struct {
    Key string
    Value string
}

func Map(string key, string value) []KeyValue {
}


func Reduce(string key, string[] values) string {
}
```

As we can see from the signatures:

- Map takes a key and a value as input, and then creates a list of key, value pairs from this input
- Reduce then takes all the values for each intermediate key, and uses these values to generate the final result for the key

For word count, let's set some background

TODO: BACKGROUND HERE

- files with lots of words.
- want to count the frequency of each word across the dataset

```go
func Map(string key, string contents) []KeyValue {
    // function to detect word separators.
	ff := func(r rune) bool { return !unicode.IsLetter(r) }

	// split contents into an array of words.
	words := strings.FieldsFunc(contents, ff)

	kva := []KeyValue{}
	for _, w := range words {
		kv := mr.KeyValue{w, "1"}
		kva = append(kva, kv)
	}
	return kva
}
```

TODO: Explain what map does here

```go
func Reduce(string key, string[] values) string {
    return strconv.Itoa(len(values))
}
```

TODO: Explain what reduce does here

### Implementation

TODO
