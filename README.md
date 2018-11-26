# 

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Build Status](https://travis-ci.com/KeisukeYamashita/pylogger.svg?branch=master)](https://travis-ci.com/KeisukeYamashita/pylogger)
[![pylogger 1.0.0](https://img.shields.io/badge/pylogger-1.0.0-blue.svg)](https://www.python.org/downloads/release/python-330/)
[![Python 3.3](https://img.shields.io/badge/python->3.3-blue.svg)](https://www.python.org/downloads/release/python-330/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Maintainability](https://api.codeclimate.com/v1/badges/a489ad892561ae5ece20/maintainability)](https://codeclimate.com/github/KeisukeYamashita/pylogger/maintainability)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

> Simple logger written in python mostly for command line interface tools.  


## Install

```shell
pip install pyplelogger
```

## Usage

### Simple usage

This is the atomic usage. Import this and print it out.

```python
from pylogger import Logger

log = Logger(__name__).build()
log.info("hogehoge")

INFO 2018-11-26 23:11:15,109 test.py:main in line 4: hogehoge
```

The default log level is `INFO` and you have to pass unique name for each handler. 

### Change default logger level

You can change logger level entire the project.

```python
import logging
from pylogger import Logger

Logger.set_default_log_level(logging.WARNING)

log = Logger(__name__).build()
log.info("hogehoge")

#=> Nothing is pritted out
```

And once you set teh default log level, it is valid in entire project.

The logger levels are defined in `logging` library.

| level | number |
|:----|:----|
| CRITICAL | 50 |
| ERROR | 40 |
| WARNING | 30 |
| INFO | 20 |
| DEBUG | 10 |
| NOTSET | 0 |

Let's say you have a `script1.py` and `script2.py`.

If you change defaul log level in `script1.py` like this,

```python
import logging
from pylogger import Logger

Logger.set_default_log_level(logging.WARNING)
```

it is valid in `script2.py` too.

```python
import logging
from pylogger import Logger

log = Logger(__name__).build()
log.info("hogehoge")

#=> Nothing is pritted out
```

### Change logger level

This is similier to changing default log level but this method changes log level for one logger.

Futhermore, the method to change default log level is a class method but, this method is a instance method, so it will only effect the instance.

```python
import logging
from pylogger import Logger

log = Logger(__name__).set_log_level(logging.WARNING).build()
log.info("hogehoge")

#=> Nothing is pritted out
```

### Change format

Specify format in string. The default format is `'%(levelname)s %(asctime)s %(module)s.py:%(funcName)s in line %(lineno)d: %(message)s'`.

```python
from pylogger import Logger

log_before = Logger(__name__).build()
log_after = Logger(__name__ + "after").set_format('%(levelname)s %(message)s').build()

log_before.info("before")
log_after.info("after")
```

Here is the output.

```shell
INFO 2018-11-26 23:11:15,109 test.py:main in line 4: before
INFO after
``` 

## With Argparse

This has good integration with [argparse](https://docs.python.jp/3/library/argparse.html), a library for creating cli tool.

### Verbose flag

This is just a simple example of the verbose flag.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')

args = parser.parse_args()
```

Now you can get number of `v` flags like 

- `-v`: 1
- `-vvv`: 3

You can convert to log level by Using `IncrementalLoggerLevel` IntEnum Class.

```python
# 1 is debug level

count = 1

log_level = IncrementalLoggerLevel.convert_logger_level(1)

log = Logger().set_log_level(log_level)
log.DEBUG("hoge")
```

Then you will see

```
#=> 
DEBUG 2018-11-26 23:11:15,109 test.py:main in line 3: hoge
```

The default level of logging is `INFO` in current version.

| level | number | count |
|:----|:----|:---|
| CRITICAL | 50 | - |
| ERROR | 40 | - |
| WARNING | 30 | - |
| INFO | 20 | 0 |
| DEBUG | 10 | 1 | 
| NOTSET | 0 | 2 |

## To contribute

We welcome for your contribution.

1. Fork this project
2. Give us a pull request

## Member

- KeisukeYamashita: Maintainer and creater