#include <Python.h>

/**
* print_python_list_info - so this too
* @p: my my this
*/
void print_python_list_info(PyObject *p)
{
	int e, a, n;
	PyObject *o;

	e = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", e);
	printf("[*] Allocated = %d\n", a);

	for (n = 0; n < size; n++)
	{
		printf("Element %d: ", n);

		o = PyList_GetItem(p, n);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
