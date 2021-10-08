#include "list.h"

/**
 * print_python_list_info -  print some basic info about Python lists
 * @p: pointer to the python object, treated as object in python
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *pl;
	Py_ssize_t i, j;

	pl = (PyListObject *)p;
	if (pl != NULL && PyList_Check(pl))
	{
		j = PyList_Size(p);
		printf("[*] Size of the Python List = %zd\n", j);
		printf("[*] Allocated = %zd\n", pl->allocated);
		for (i = 0; i < j; i++)
		{
			printf("Element %zd: ", i);
			printf("%s\n", pl->ob_item[i]->ob_type->tp_name);
		}
	}
}
