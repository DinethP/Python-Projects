from distutils.core import setup, Extension
setup(name='myutil', version='1.0', ext_modules=[
      Extension('myutil', ['myutil.c'])])
