from distutils.core import setup, Extension

setup(name = 'oilstation', 
        version = '1.0',
        py_modules=['MapData', 'OilData', 'TelegramBot', 'KeyData', 'TermProject(0003, 0018)', 'image\\'],
        packages=['image', ''],
        package_data={
            'image' : ['*.png'],
            '' : ['data.json']
        }
        )