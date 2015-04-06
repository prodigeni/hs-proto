import re
import os
import shutil
import tempfile


RE_IMPORT_FROM = re.compile("from ([^ ]+) import ([^ ]+)(.*)")
RE_IMPORT = re.compile("import ([^ ]+)(.*)")

def relativize_file(base, path, out):
	dirname = os.path.dirname(path)

	if isinstance(out, str):
		with open(out, "w") as f_out:
			return relativize_file(base, path, f_out)

	with open(path, "r") as f:
		for line in f:
			m1 = RE_IMPORT_FROM.match(line.strip("\n\r"))
			m2 = RE_IMPORT.match(line.strip("\n\r"))

			if m1 is None and m2 is None:
				# not an import statement
				out.write(line)
				continue

			if m1 is not None:
				from_clause, what_clause, rest = m1.groups()
				what = from_clause + "." + what_clause

			if m2 is not None:
				what, rest = m2.groups()

			if what.startswith("."):
				# not touching relative imports
				out.write(line)
				continue

			# calculate filesystem path
			import_path = os.path.join(base, *what.split(".")) + ".py"

			if not os.path.exists(import_path):
				# probably not our module
				out.write(line)
				continue

			# found file or directory, find relative path to file/directory
			relpath = os.path.relpath(import_path, dirname)
			mod_dirname, mod_filename = os.path.split(relpath)
			relative_mod = "." + mod_dirname.replace("..", ".").replace(os.sep, ".")

			out.write("from {} import {}{}\n".format(relative_mod, mod_filename[:-3], rest))


def relativize_file_inplace(base, path):
	with tempfile.NamedTemporaryFile(mode="w", delete=False) as f_out:
		name = f_out.name
		relativize_file(base, path, name)

	shutil.move(name, path)


if __name__ == "__main__":
	import sys

	if len(sys.argv) < 3:
		sys.stderr.write("Usage: {0} <base-dir> [<file> ...]\n".format(sys.argv[0]))
		sys.stderr.write("Note: All files will be modified in-place!\n")
		sys.exit(1)

	base = os.path.abspath(sys.argv[1])
	for fn in map(os.path.abspath, sys.argv[2:]):
		print("Processing {}".format(fn))
		relativize_file_inplace(base, fn)
