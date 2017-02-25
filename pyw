#!/usr/bin/env bash

#NOTE: This only manages virtualenvs, not the python runtime itself
#TODO: Consider using docker if requested version not found

#Version 1.0-alpha

#Reset previous environment, if any
deactivate 1>&2 &>/dev/null || true

#Default to system python, but script name can indicate explicit version
if [[ "${BASH_SOURCE[0]}" != 'pyw' ]]; then
  PY_VERSION="$(echo "${BASH_SOURCE[0]}" | sed 's/^pyw//')"
else
  PY_VERSION="$(python --version 2>&1 | grep -Eo '[0-9]\.[0-9]+')"
fi

echo "Python version to use: ${PY_VERSION}"

PYW_WORKDIR="./.virtualenv"
PYW_INSTALL_LOG="./pip_install.log"

function __pip-min-version {
  #pip version is at least X
  [[ "$(pip --version | grep -Eo '[0-9]' | head -n1)" -ge $1 ]]
}

function __pip-failure {
  cat "${PYW_INSTALL_LOG}" 1>&2
  echo "pip install failed!"
  return 2
}

function pip-install {
  if __pip-min-version 6; then
    #Disable frivolous and obnoxious version warning introduced in pip 6.x
    pip --disable-pip-version-check --log ${PYW_INSTALL_LOG} install $@ \
      || __pip-failure
  else
    pip --log ${PYW_INSTALL_LOG} install $@ \
      || __pip-failure
  fi
}

export PIP_CONFIG_FILE="${PYW_WORKDIR}/pip.conf"

if [[ -x "${PYW_WORKDIR}/bin/python" ]]; then
  if ! ${PYW_WORKDIR}/bin/python --version 2>&1 | grep "^Python ${PY_VERSION}"; then
    echo "Current virtualenv at ${PYW_WORKDIR} is not requested python version!" 1>&2
    echo "Recreating virtualenv..."
    rm -rf "${PYW_WORKDIR}"
  fi
fi

if ! source "${PYW_WORKDIR}/bin/activate" 2>/dev/null; then
  if ! virtualenv "${PYW_WORKDIR}" --python="python${PY_VERSION}"; then
    echo "Python ${PY_VERSION} not found or had errors - aborting!" 1>&2
    return 3
  fi
  source "${PYW_WORKDIR}/bin/activate"
fi

#TODO: Use relative paths in case sourced from parent or subdirectory
if [[ -f requirements.txt ]]; then
  #Force upgrade if on pip 1.x, as it's too old to work with many modern conventions like ~=
  if pip --version | grep -q '^pip 1\.'; then
    echo "NOTE: Force upgrading pip as default version is too old"
    pip-install 'pip>=6.0'
  fi
  echo "Running pip install... (output in ${PYW_INSTALL_LOG})" 1>&2
  #Can't use exit in a sourced file as it will terminate the outer shell
  pip-install --requirement requirements.txt --quiet || return 1
  echo "requirements.txt installed successfully!" 1>&2
elif [[ -f setup.py ]]; then
  echo "Running pip install... (output in ${PYW_INSTALL_LOG})" 1>&2
  python setup.py -q install || return 1
  echo "setup.py installed successfully" 1>&2
else
  echo "WARNING: no dependencies file (setup.py or requirements.txt) found!"
fi
