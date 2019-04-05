[![](https://www.ginar.io/wp-content/themes/ginar/assets/img/logo1.svg)](https://ginar.io)
# Statistical test
[![](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/ginarteam) [![](https://img.shields.io/badge/Telegram-Group-blue.svg)](https://t.me/GINAR_io) 


GINAR is a blockchain technology company specializing in providing a decentralized random number generator. Random Number Generation, or RNG, is a key component to applications that benefit from true randomness. GINAR is set to release a best-in-class decentralized.
- Random Number Generator (dRNG) that will change the financial, gambling, online gaming, and IOT industry by providing the fastest, most secure and easily verifiable service, ..

- For more detail about GINAR: Read our white-paper -> [![](https://img.shields.io/badge/docs-latest-af1a97.svg)](https://www.ginar.io/whitepaper-v2.0.pdf)

This is result of Dieharder statistical test suite for Random Number Generator (RNG) that apply to GINAR RNG    

# Dieharder Statistical Test Suite

  
> The dieharder suite is more than just the diehard tests cleaned up and given a pretty GPL'd source face in native C. Tests from the Statistical Test Suite (STS) developed by the National Institute for Standards and Technology (NIST) are being incorporated, as are new tests developed by rgb. Where possible or appropriate, all tests that can be parameterized ("cranked up") to where failure, at least, is unambiguous are so parameterized and controllable from the command line.

[Dieharder Statistical Test Suite](https://webhome.phy.duke.edu/~rgb/General/dieharder.php)

### Installation
You can install dieharder test suite directly from Linux Package Managesment. 
(Ubuntu)
```sh
$ sudo apt-get install dieharder
```

### Get data for random test

You need a dataset of random number for the test. We have built a function that help you get data from GINAR:
- Login your account  GINAR
- Initialize your session key
- Copy the init-session-key link (url)

This test suite requires a lot of numbers. We recommend using 70.000.000 numbers.

Or you can get the sample of random number that we provide on github.
- Clone the repository or just download zip file and all extended file (archive.*).
- unzip the file and you will get input.bin (the random-number-file gotten from GINAR).

### Run the test
```sh
$ dieharder -a -g 202 -f input.bin [-D default -D histogram]
```

### Output and visualization

You can read the result in output2.txt on github or read output of the test suite when you run the command above.

Sample of `result`:

```
#=============================================================================#
#            dieharder version 3.31.1 Copyright 2003 Robert G. Brown          #
#=============================================================================#
   rng_name    |           filename             |rands/second|
     file_input|                       input.bin|  6.03e+06  |
#=============================================================================#
#                         Histogram of test p-values                          #
#=============================================================================#
# Bin scale = 0.100000
#     20|    |    |    |    |    |    |    |    |    |    |
#       |    |    |    |    |    |    |    |    |    |    |
#     18|    |    |    |    |    |    |    |    |    |    |
#       |    |    |    |    |    |    |    |    |    |    |
#     16|    |    |    |    |    |    |    |    |    |    |
#       |    |    |    |    |    |    |    |    |    |    |
#     14|    |    |    |    |    |    |    |    |    |    |
#       |    |****|    |    |    |****|    |    |    |****|
#     12|    |****|****|    |    |****|    |    |    |****|
#       |    |****|****|    |    |****|****|    |    |****|
#     10|    |****|****|    |    |****|****|    |    |****|
#       |****|****|****|****|    |****|****|    |    |****|
#      8|****|****|****|****|    |****|****|    |****|****|
#       |****|****|****|****|    |****|****|****|****|****|
#      6|****|****|****|****|    |****|****|****|****|****|
#       |****|****|****|****|****|****|****|****|****|****|
#      4|****|****|****|****|****|****|****|****|****|****|
#       |****|****|****|****|****|****|****|****|****|****|
#      2|****|****|****|****|****|****|****|****|****|****|
#       |****|****|****|****|****|****|****|****|****|****|
#       |--------------------------------------------------
#       | 0.1| 0.2| 0.3| 0.4| 0.5| 0.6| 0.7| 0.8| 0.9| 1.0|
#=============================================================================#
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
   diehard_birthdays|   0|       100|     100|0.89925936|  PASSED  

```

