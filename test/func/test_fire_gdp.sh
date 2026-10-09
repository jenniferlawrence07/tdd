test -e ssshtest || curl -s -o ssshtest https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_plot_runs python3 src/plot_fire_gdp.py \
    --co2 test/data/test_co2.csv \
    --gdp test/data/test_gdp.csv \
    --country Brazil \
    --out fire_gdp.png

assert_exit_code 0
assert_equal fire_gdp.png $(ls fire_gdp.png)
