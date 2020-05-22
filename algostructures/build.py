from cffi import FFI
ffi = FFI()

declaration_header_files = [
    "algostructures/search/array_search.h"
]

implementaion_c_files = [
    '#include "array_search.c"'
]

cdef_content = ""
for file in declaration_header_files:
    with open(file) as f:
        cdef_content += f.read()
ffi.cdef(cdef_content)

source = "\n".join(implementaion_c_files)
ffi.set_source(
    "algostructures._array_search",
    source,
    include_dirs=["algostructures/search/", "algostructures/include/"],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
)

if __name__ == "__main__":
    ffi.compile(verbose=True)
