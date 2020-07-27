   87  source venv-distributions/bin/activate
   88  python
   89  source venv-distributions/bin/activate
   90  python3
   91  exit
   92  source venv-distributions/bin/activate
   93  pip uninstall distributions
   94  pip3 install .
   95  python3
   96  cd ..
   97  python3 example_code.py
   98  deactivate
   99  exit
  100  source venv=distributions/bin/activate
  101  source venv-distributions/bin/activate
  102  cd..
  103  cd ..
  104  source venv-distributions/bin/activate
  105  pip install --upgrade .
  106  python -m unittest test
  107  pip install --upgrade .
  108  python -m unittest test
  109  pip install --upgrade .
  110  python -m unittest test
  111  pip install --upgrade .
  112  python -m unittest test
  113  history > test.sh
