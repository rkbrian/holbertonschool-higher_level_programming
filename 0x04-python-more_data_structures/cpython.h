#ifndef CPYTHON_H
#define CPYTHON_H

#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <stdlib.h>
#include <assert.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

#endif /* CPYTHON_H */
