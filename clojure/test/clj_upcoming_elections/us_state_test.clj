(ns clj-upcoming-elections.us-state-test
  (:require [clojure.test :refer :all]
            [clj-upcoming-elections.us-state :refer :all]))

(deftest postal-abbreviations-test
  (testing "there are 61 states, territories, military abbreviations, etc."
    (is (= 61
           (count postal-abbreviations)))
    (testing "including states and districts with a current DW employee"
      (is (every? (set postal-abbreviations)
                  #{"CA" "CO" "DC" "IL" "KS" "KY" "MN" "NY" "RI" "VA" "WA"})))))
