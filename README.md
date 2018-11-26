# pylogger

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Build Status](https://travis-ci.com/KeisukeYamashita/pylogger.svg?branch=master)](https://travis-ci.com/KeisukeYamashita/pylogger)
[![Python 3.3](https://img.shields.io/badge/python->3.3-blue.svg)](https://www.python.org/downloads/release/python-330/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Simple logger written in python mostly for command line interface tools.  

## Install

```shell
pip install pylogger
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

## Member

- KeisukeYamashita: Maintainer and creater