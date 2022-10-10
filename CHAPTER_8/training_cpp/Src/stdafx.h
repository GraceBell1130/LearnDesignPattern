#pragma once
#include <iostream>
#include <memory>
#include <Windows.h>

namespace std {
#ifdef UNICODE
	using tstring = wstring;
	using tstring_view = wstring_view;
	using tstringstream = wstringstream;
#define	tcout wcout
#else
	using tstring = string;
	using tstring_view = string_view;
	using tstringstream = stringstream;
	using tcout = ostream;
#define	tcout cout
#endif // UNICODE
}
