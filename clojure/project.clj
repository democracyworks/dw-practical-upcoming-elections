(defproject clj-upcoming-elections "0.1.0-SNAPSHOT"
  :description "An anonymous Democracy Works coding exercise"
  :min-lein-version "2.7.1"
  :dependencies [[org.clojure/clojure "1.10.3"]
                 [ring "1.9.4"]
                 [ring/ring-defaults "0.3.3"]
                 [compojure "1.6.2"]
                 [hiccup "1.0.5"]]
  :plugins [[lein-ring "0.12.5"]]
  :ring {:handler clj-upcoming-elections.core/handler})
