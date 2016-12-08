from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

import os
os.environ["CC"] = "clang-omp"

ext_modules = []
ext_modules += cythonize([Extension("pybm3d.bm3d",
                                    sources=["pybm3d/bm3d.pyx",
                                             "bm3d_src/mt19937ar.c",
                                             "bm3d_src/iio.c",
                                             "bm3d_src/bm3d.cpp",
                                             "bm3d_src/lib_transforms.cpp",
                                             "bm3d_src/utilities.cpp",
                                         ],
                                    language="c++",
                                    include_dirs = [np.get_include()],
                                    libraries=["png", "tiff", "jpeg", "fftw3", "fftw3f"],
                                    extra_objects=["/usr/local/lib/libiomp5.dylib"],
                                    extra_compile_args=["-fopenmp"])])

setup(
    name='pybm3d',
    ext_modules=ext_modules,
    version='1.0',
    description='Python wrapper around BM3d',
    author='Eric Jonas',
    author_email='jonas@ericjonas.com',
    url='https://github.com/ericmjonas/pybm3d',
    packages=['pybm3d']
)
