#include <Python.h>

/**
* print_python_list_info - you know this 
* @p: well time to play
*/
void print_python_list_info(PyObject *p)
{
	int e, c, k;
	PyObject *o;

	e = Py_SIZE(p);
	c = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", e);
	printf("[*] Allocated = %d\n", c);

	for (k = 0; k < e; k++)
	{
		printf("Element %d: ", k);

		o = PyList_GetItem(p, k);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
