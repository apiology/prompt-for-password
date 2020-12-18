#!/bin/bash -e

# Get oldest supported version from here: https://www.python.org/downloads/
oldest_supported_python_versions=3.6.12
# Get latest version from here: https://www.python.org/downloads/
python_version=3.9.0

for ver in $oldest_supported_python_versions $python_version
do
  if [ "$(uname)" == Darwin ]
  then
    if [ "$(cut -d. -f1-2 "${ver:?}")" == 3.6 ]
    then
      # https://teratail.com/questions/309663
      brew install zlib bzip2 || true
      CFLAGS="-I$(brew --prefix zlib)/include -I$(brew --prefix bzip2)/include" LDFLAGS="-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --skip-existing --patch 3.6.12 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index=1)
    else
      pyenv install -s ${ver:?}
    fi

  else
    pyenv install -s ${ver:?}
  fi
done

pyenv virtualenv ${python_version:?} "$(cut -d' ' -f1 < .python-version)" || true
# Make sure we have a pip with the 20.3 resolver, and after the
# initial bugfix release
pip install 'pip>=20.3.1'
pip install -r requirements_dev.txt
pip install -e .
