# coding: utf-8
require 'sinatra'
require 'rack'
require 'rack/csrf'

require_relative '../../lib/upcoming_elections/us_states'
include UsStates

class ApplicationController < Sinatra::Base
  configure do
    set :public_folder, 'public'
    set :views, 'app/views'

    use Rack::Session::Cookie, :secret => "some unique secret string here"
    use Rack::Csrf, :raise => true
  end

  get '/' do
    erb :address_form, { :locals => {:us_states => UsStates::POSTAL_ABBREVIATIONS},
                         :layout => true }
  end

  post "/search" do
    status 204
  end
end
