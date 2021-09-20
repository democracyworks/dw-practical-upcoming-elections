# Democracy Works Practical: Upcoming Elections

A web application written in Ruby using [Sinatra][sinatra],
[minitest][minitest], and [erb templates][erb].

## Setup

### Prerequisites

- [Ruby][ruby] version 2.3+
- [bundler][bundler]
- [rake][rake]
- [rbenv][rbenv] (optional)

### Installing the requirements

```sh
## Install the dependencies
bundle install

## Check that the tests run
rake test
```

## Running

From the same directory as this README:

```sh
bundle exec rackup
```

## Quickstart

After checking out the repo, run `bundle install` to install dependencies.
Then, run `rake test` to run the tests. You can also run `bin/console`
for an interactive prompt that will allow you to experiment.

Start the webserver by running `rackup` in the project's toplevel directory.
In your browser, navigate to `http://localhost:9292` and enter an
address to see if there are currently any upcoming elections.


## Testing

`minitest` is used for unit tests. You can run the full test suite with:

```
rake test
```

[sinatra]: https://github.com/sinatra/sinatra
[ruby]: https://github.com/ruby/ruby
[bundler]: https://bundler.io/
[rake]: https://github.com/ruby/rake
[rbenv]: https://github.com/rbenv/rbenv
[erb]: https://www.stuartellis.name/articles/erb/
[minitest]: https://github.com/seattlerb/minitest
