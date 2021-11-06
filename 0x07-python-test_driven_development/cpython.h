#ifndef CPYTHON_H
#define CPYTHON_H

#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <longintrepr.h>
#include <floatobject.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <stdlib.h>
#include <assert.h>
#include <float.h>
#include <wchar.h>
#include <locale.h>

void print_python_string(PyObject *p);

#endif /* CPYTHON_H */
