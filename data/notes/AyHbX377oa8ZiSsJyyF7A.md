
# Golang and irritating tests

I've been learning a lot of Go in recent times. I'm learning how Go web applications work. It's a bit overwhelming that there are so many things that you can use to build Go web applications. So far, I've seen the following libraries in use in real services:

* [Gorilla](https://www.gorillatoolkit.org/)
* [Goji](https://goji.io/)
* [net/http](https://pkg.go.dev/net/http)

The good thing is that they are all kinda similar at the core, so you're not really drowning in the multitude of ways to do the same thing.

I'm not a Go expert by any means, and I did hit an issue that I did not like. There's no good way to mock internal dependencies in tests in Go.

For example, let's take this Python test

```python
# code
def my_method():
    internal_method()

# tests
@patch('internal_method')
def test_my_method(mock_internal_method):
    my_method()
    mock_internal_method.assert_called_once()
```

There is no real Go equivalent to the `mock_internal_method.assert_called_once()`.
As I understand, you either need to make the `internal_method` something
that `my_method` takes as an input, so that your test can pass in a mock method.
There's a good [post](https://stackoverflow.com/questions/52381358/test-that-method-is-called-in-handler-in-golang)
on stack overflow about this. This does make things a bit more complicated than needed, but I gueuss Go is
opinionated and this is just one of those opinions.

The Go equivalent to the same test would be something like this.

```go
// code

// need to create this struct to wrap the real internalMethod
// so that we can inject a mock value for internalMethod in our tests
type internalMethodStruct struct {}

func (im *internalMethodStruct) InternalMethod() {
    internalMethod()
}

func MyMethod(im internalMethodStruct) {
    im.InternalMethod()
}

// tests
type spy struct {
    called boolean
}

func (s *spy) InternalMethod() {
    s.called = true
}

func TestMyMethod(t *testing.T) {
    spyObj := &spy{called: false}
    MyMethod(spyObj)
    assert.equal(true, spyObj.called)
}
```

See how much work that is! The fact that you have to create an interface,
make your method take the interface as input and then
create a spy in the test seems a bit too much to me.


# Write good documentation.

My team owns some docs that have been read by basically every team in the engineering org at this point. I spent last week identifying issues in those docs and then improving them by fixing those issues. There are a couple of interesting things I noticed that I've internalized as good things to keep in mind when writing documentation.

* If you're asking someone to do some work like migrating to a secure library you built instead of rolling their own code, you really really need to be very clear on why that work is important. If you don't get it across that the work is important, the person doing it will think "Why am I even doing this?!" the instant they find something confusing. You're basically setting your docs up for failure if the motivation of the work is not clear.

* You need to make things as obvious as possible. As much as possible, give the reader a clear default wherever they have to make a choice, with a link to other choices possible. Putting a list of choices in front of the reader is just asking for confusion.

  * **Good**: You need to do X. There are multiple ways to do it but we strongly recommend the way A. There are other ways to do it, see this linked supporting doc.

  * **Bad**: You need to do X. Based on your usecase, you can either do it in the A way or the B way or the C way.

  This example is overly simple, but the point still stands.

* The structure of your document is really important. You do not want to put things that the reader doesn't care about at the top and the meat of the content near the bottom. Doing this is basically an invitation asking people to not read your document carefully and just skim it.

# Things of interest

## India's population

https://www.economist.com/asia/2021/12/02/indias-population-will-start-to-shrink-sooner-than-expected

India's fertility rate has fallen below replacement level.

>This is big news not just for India but, seeing that its 1.4bn people are nearly a fifth of humanity, for the planet. The number of Indians will still grow, because many young women have yet to reach child-bearing age. But lower fertility means the population will peak sooner and at a lower figure: not in 40 years at more than 1.7bn, as was widely predicted, but probably a decade earlier, at perhaps 1.6bn.

## World Chess Championship

Magnus Carlsen defended his championship today, destroying Ian Nepomniachtchi 7.5 - 3.5, winning 4 games, drawing 7 and losing none. The first 5 games of the match were draws, but in game 6, Magnus won after playing a 136 move game that went on for ~8 hours. In the end, the game was a theoretical draw, but Magnus kept pushing until Nepomniachtchi made a losing mistake.

The psychological impact of this long game was really interesting to me, because after this, Nepomniachtchi crumbled, playing "below grandmaster level" (in his own words), and losing 3 games out of the 5 that were played after game 6. Computers don't have such psychological issues.

The 136 move game is one of the best chess games I've seen: https://www.youtube.com/watch?v=PmQs1KhB948
