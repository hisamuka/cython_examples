from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import platform


ext_modules = [
    Extension(
        "_tax",
        ["_tax.pyx"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-fopenmp"]
    )
]

setup(
    name='hello-parallel-world',
    ext_modules=cythonize(ext_modules),
)
