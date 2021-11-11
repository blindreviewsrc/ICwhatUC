from distutils.core import setup

setup(
    name='ColabPlugin',
    version='1.0',
    author='Blind',
    author_email='blind@gmail.com',
    py_modules=['plugin', 'verilog.verilog', 'common.helper'],
    url='https://github.com/blindreviewsrc/ICwhatUC',
    license='LICENSE',
    description='Jupyter notebook plugin to run Verilog',
    # long_description=open('README.md').read(),
)
