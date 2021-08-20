(ns clj-upcoming-elections.us-state-test
  (:require [clojure.test :refer [deftest is]]
            [clj-upcoming-elections.us-state :as us-state]))

(deftest postal-abbreviations-test
  (is (= 61 (count us-state/postal-abbreviations))
      "there are 61 postal abbreviations")
  (is (every? (set us-state/postal-abbreviations)
              #{"AR" "CA" "CO" "DC" "IL" "MN" "NY" "OR" "RI" "TN" "VA" "WA"})
      "including states and districts with a current Democracy Works employee"))
