from setuptools import setup, find_packages

setup(
    name='core_iziBot',                 
    version='1.0.0',                     
    packages=find_packages(exclude=['rutina', 'utils']),            
    install_requires=[                   
        'pyautogui',                     
        'numpy',
        'opencv-python',
        'pytesseract'
    ],
    author='Jim Vásquez',
    author_email='jp.vasquez@outlook.com',
    description='Paquete de utilidades para control de pantalla y acciones',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/techeca/iziBot',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)