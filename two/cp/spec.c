#include <Python.h>

static
PyObject *
spec_echo(PyObject *self, PyObject *args) {
	const char *command;
	int sts;

	if(!PyArg_ParseTuple(args, "s", &command)) {
		return NULL;
	}

	sts = 0;
	printf("%s\n", command);

	return Py_BuildValue("i", sts);
}

static PyMethodDef Spec_Methods[] = {
	{"echo", spec_echo, METH_VARARGS, "Echoes a text"}.
	{NULL, NULL, 0, NULL}
}

PyMODINIT_FUNC
initspec(void) {
	(void) PyInitModule("spec", Spec_Methods);
}