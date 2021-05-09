import setuptools

packages_src = 'src'

setuptools.setup(
    name='demo_reader_plugin_bz2',
    description='bz2 file reader plugin for demo_reader',
    version='0.0.1',
    packages=setuptools.find_packages(packages_src),
    package_dir={
        '': packages_src
    },

    entry_points={
        'demo_reader.compression_plugins': [
            'bz2 = demo_reader_plugin_bz2.bzipped'
        ]
    }
)
