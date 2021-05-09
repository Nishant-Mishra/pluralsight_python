import setuptools

packages_src = 'src'

setuptools.setup(
    name='demo_reader_plugin_gz',
    description='gz file reader plugin for demo_reader module',
    version='0.0.1',
    packages=setuptools.find_packages(packages_src),
    package_dir={
        '': packages_src
    },

    entry_points={
        'demo_reader.compression_plugins': [
            'gz = demo_reader_plugin_gz.gzipped'
        ]
    }
)
