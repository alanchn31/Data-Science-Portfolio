## Intro to Numpy

* Numpy is a Python module that provides fast primitives for multidimensional arrays. It's well-suited to implementing numerical linear algebra algorithms, and for those can be much faster than Python's native list and dictionary types when you only need to store and operate on numerical data

## Indexing and slicing

* The usual 0-based slicing and indexing notation you know and love from lists is also supported for Numpy arrays. In the multidimensional case, including their natural multidimensional analogues with index ranges separated by commas.

* **Slices are views** - To help save memory, when you slice a Numpy array, you are actually creating a view into that array. That means modifications through the view will modify the original array.

* Two common ways to index a Numpy array are to use a boolean mask or to use a set of integer indices.  
    Article on boolean masking: https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html

## Dense matrix storage: Column-major versus row-major layouts
* For linear algebra, we will be especially interested in 2-D arrays, which we will use to store matrices. For this common case, there is a subtle performance issue related to how matrices are stored in memory.

* By way of background, physical storage---whether it be memory or disk---is basically one big array. And because of how physical storage is implemented, it turns out that it is much faster to access consecutive elements in memory than, say, to jump around randomly.

* A matrix is a two-dimensional object. Thus, when it is stored in memory, it must be mapped in some way to the one-dimensional physical array. There are many possible mappings, but the two most common conventions are known as the column-major and row-major layouts:

    <img src="./docs/row_column_major.PNG" width="500" height="500"><br/><br/>

## Requesting a layout in Numpy
* In Numpy, you can ask for either layout. The default in Numpy is row-major.

* Historically numerical linear algebra libraries were developed assuming column-major layout.  
    ```
    n = 5000
    A_colmaj = np.ones((n, n), order='F') # column-major (Fortran convention)
    A_rowmaj = np.ones((n, n), order='C') # row-major (C/C++ convention)
    ```

## Sparse matrix storage
* To reduce storage requirements, we can store sparse matrices in two forms, coordinate (COO) format or compressed sparse row (CSR) format

* **Coordinate Format (COO)** - In this format we store three lists, one each for rows, columns and the elements of the matrix.

    <img src="./docs/coo_format.PNG" width="700" height="500"><br/><br/>

* **Compressed Sparse Row Format (CSR)** - similar to the COO format except that it is much more compact and takes up less storage

    <img src="./docs/csr_format.PNG" width="700" height="500"><br/><br/>

## Scipy implementations:  
```
import numpy as np
import scipy.sparse as sp

A_coo_sp = sp.coo_matrix((coo_vals, (coo_rows, coo_cols)))
A_csr_sp = A_coo_sp.tocsr() # Alternatively: sp.csr_matrix((val, ind, ptr))
x_sp = np.ones(num_verts)

print ("\n==> COO in Scipy:")
%timeit A_coo_sp.dot (x_sp)

print ("\n==> CSR in Scipy:")
%timeit A_csr_sp.dot (x_sp)
```