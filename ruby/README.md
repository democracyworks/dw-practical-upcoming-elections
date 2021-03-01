# Upcoming Elections

This is a server-side web application written in Ruby using
[Sinatra][sinatra], [minitest][minitest], and [erb templates][erb].

## Prerequisites

- [ruby][ruby] version 2.0 or later
- [rake][rake]
- [bundler][bundler]
- [rbenv][rbenv] (optional)

## Quickstart

After checking out the repo, run `bundle install` to install dependencies.
Then, run `rake test` to run the tests. You can also run `bin/console`
for an interactive prompt that will allow you to experiment.

Start the webserver by running `rackup` in the project's toplevel directory.
In your browser, navigate to `http://localhost:9292` and enter an
address to see if there are currently any upcoming elections.

## Testing

`minitest` is used for unit tests. You can run the full test suite by
using `rake test`.

[sinatra]: https://github.com/sinatra/sinatra
[rubygems]: https://rubygems.org
[ruby]: https://github.com/ruby/ruby
[rake]: https://github.com/ruby/rake
[bundler]: https://bundler.io/
[rbenv]: https://github.com/rbenv/rbenv
[erb]: https://www.stuartellis.name/articles/erb/
[minitest]: https://github.com/seattlerb/minitest
