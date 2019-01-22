#include <Python.h>

static PyObject *helloworld(PyObject *self, PyObject *args)
{
    printf("Hello World\n");
    return Py_None;
}
static PyObject *nn_ave(PyObject *self, PyObject *args)
{
    PyObject *list;
    if (!PyArg_ParseTuple(args, "O", &list))
        return NULL;

    long len = PySequence_Size(list);
    double sum = 0;
    for (int i = 0; i < len; i++)
    {
        PyObject *a = PySequence_Fast_GET_ITEM(list, i);
        sum += PyFloat_AsDouble(a);
    }
    PyObject *out = Py_BuildValue("f", (sum / len));
    return out;
}
static PyMethodDef myMethods[] = {
    {"helloworld", helloworld, METH_NOARGS, "Prints Hello World"},
    {"nn_ave", nn_ave, METH_VARARGS, "Returns average"},
    {NULL, NULL, 0, NULL}};
static struct PyModuleDef myutil = {
    PyModuleDef_HEAD_INIT,
    "myutil",
    "Test Module",
    -1,
    myMethods};
PyMODINIT_FUNC PyInit_myutil(void)
{
    return PyModule_Create(&myutil);
}