import importlib
import os.path
import pkgutil
import demo_reader.compressed


def iter_namespace(ns_pkg):
    return pkgutil.iter_modules(
        ns_pkg.__path__,
        ns_pkg.__name__ + '.'
    )


compression_plugins = {
    importlib.import_module(module)
    for _, module, _ in iter_namespace(demo_reader.compressed)
}


extension_map = {
    module.extension: module.opener for module in compression_plugins
}


class MultiReader:
    def __init__(self, filename):
        ext = os.path.splitext(filename)[1]
        opener = extension_map.get(ext, open)
        self.f = opener(filename, 'rt')

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()
